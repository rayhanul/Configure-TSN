import paramiko
import time
from previous.src.cnc.model import *
from previous.src.cnc.tools import *
from tqdm import tqdm
import os
import argparse
import glob


class Time:

    def __init__(sec, nsec) -> None:
        sec = sec
        nsec = nsec


class Entity_ssh_info:

    def __init__(self) -> None:
        self.ip = None
        self.username = None
        self.password = None


class SSH_Agent:

    def __init__(self) -> None:
        self.ssh_conn = None
        self.sftp_conn = None

        self.log_file = open("log.txt", "w")

    def exec_command(self, command):
        # self.ssh_conn.exec_command(command)
        stdin, stdout, stderr = self.ssh_conn.exec_command(command)
        output = stdout.read()
        error = stderr.read()

        ## Record the command and the output
        self.log_file.write(command + "\n")
        if output:
            self.log_file.write(output.decode("utf-8") + "\n")
        if error:
            self.log_file.write(error.decode("utf-8") + "\n")

        while not stdout.channel.exit_status_ready():
            time.sleep(0.3)
        return output.decode("utf-8")

    def close(
        self,
    ):
        self.ssh_conn.close()


class Controller:

    def __init__(self, cnc: CNC) -> None:
        self.cnc = cnc
        self.ssh_info = {}
        self.conn = {}
        self.sftp_conn = {}

        net_config = load_json("conf.json")

        for entity in self.cnc.Entities:
            self.ssh_info[entity.id] = Entity_ssh_info()
            self.ssh_info[entity.id].ip = net_config[entity.name]["ip"]
            self.ssh_info[entity.id].username = net_config[entity.name]["username"]
            self.ssh_info[entity.id].password = net_config[entity.name]["password"]

    def connect(
        self,
    ):
        for entity in self.cnc.Entities:
            entity_id = entity.id
            ip = self.ssh_info[entity_id].ip
            username = self.ssh_info[entity_id].username
            password = self.ssh_info[entity_id].password

            ssh_agent = SSH_Agent()

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, username=username, password=password)
            ssh_agent.ssh_conn = ssh
            self.conn[entity.id] = ssh_agent

    def disconnect(
        self,
    ):
        for entity in self.cnc.Entities:
            self.conn[entity.id].close()

    def add_vlan(self):
        for entity in tqdm(self.cnc.Entities, desc="Add VLAN"):
            for _, link in entity.links.items():
                for flow in link.flows:
                    VLAN_id = flow + 2
                    start = link.start
                    end = link.end
                    ## Three conditions (ES, SW) -> (SW, SW) -> (SW, ES)
                    ## This function is so ugly, I will refactor it later
                    if (
                        "es" in self.cnc.Entities[start].name
                        and "sw" in self.cnc.Entities[end].name
                    ):
                        self.conn[start].exec_command(vlan_add_talker(VLAN_id))
                        self.conn[end].exec_command(
                            vlan_add_bridge(
                                self.cnc.Entities[end]
                                .links[f"({end}, {start})"]
                                .e_port,
                                VLAN_id,
                            )
                        )

                    elif (
                        "sw" in self.cnc.Entities[start].name
                        and "sw" in self.cnc.Entities[end].name
                    ):
                        self.conn[start].exec_command(
                            vlan_add_bridge(
                                self.cnc.Entities[start]
                                .links[f"({start}, {end})"]
                                .e_port,
                                VLAN_id,
                            )
                        )
                        self.conn[end].exec_command(
                            vlan_add_bridge(
                                self.cnc.Entities[end]
                                .links[f"({end}, {start})"]
                                .e_port,
                                VLAN_id,
                            )
                        )
                    elif (
                        "sw" in self.cnc.Entities[start].name
                        and "es" in self.cnc.Entities[end].name
                    ):
                        self.conn[start].exec_command(
                            vlan_add_bridge(
                                self.cnc.Entities[start]
                                .links[f"({start}, {end})"]
                                .e_port,
                                VLAN_id,
                            )
                        )
                        self.conn[end].exec_command(vlan_add_listener(VLAN_id))
                    else:
                        print("[ERROR]: Something wrong with the link")

    def reset_vlan(
        self,
    ):
        for entity in tqdm(self.cnc.Entities, desc="Reset VLAN"):
            if "sw" in entity.name:
                self.conn[entity.id].exec_command(delete_all_vlan_sw())
            elif "es" in entity.name:
                self.conn[entity.id].exec_command(delete_all_vlan_es())
            else:
                print("[ERROR]: Something wrong with the entity name")

    def add_mstp(
        self,
    ):
        for entity in tqdm(self.cnc.Entities[::-1], desc="Add MSTP INS"):
            if "sw" in self.cnc.Entities[entity.id].name:
                self.conn[entity.id].exec_command(set_mstid())
                for flow in self.cnc._flow_set:
                    VLAN_id = flow + 2
                    start = entity.id
                    self.conn[start].exec_command(add_tree(VLAN_id))
                vid2fid = {flow + 2: [flow + 2] for flow in self.cnc._flow_set}
                fid2mstid = {flow + 2: [flow + 2] for flow in self.cnc._flow_set}
                self.conn[start].exec_command(add_vid2fid_map(vid2fid))
                self.conn[start].exec_command(add_fid2mstid_map(fid2mstid))

    def set_mstp_root(
        self,
    ):
        """
        Make the first hop to be the root
        """

        for flow in self.cnc.Flows:
            path = flow.path
            first_hop = eval(path[0])[1]
            first_hop_entity = self.cnc.Entities[first_hop]
            link_after_first_hop = path[1]
            self.conn[first_hop].exec_command(assign_mstp_root(flow.id + 2))
            # print(f"Set sw {first_hop_entity.name} tree {flow.id+2} root")

        # assigned = set()
        # for entity in tqdm(self.cnc.Entities, desc='Assign MSTP Root'):
        #     for _, link in entity.links.items():
        #         for flow in link.flows:
        #             if flow in assigned:
        #                 continue
        #             VLAN_id = flow + 2
        #             start = link.start
        #             end = link.end
        #             if 'sw' in self.cnc.Entities[
        #                     start].name and 'sw' in self.cnc.Entities[end].name:
        #                 self.conn[start].exec_command(
        #                     assign_mstp_root(VLAN_id))
        #                 assigned.add(flow)

    def set_mstp_pathcost(
        self,
    ):
        """Set un-used port with cost 5000000"""
        for flow in self.cnc.Flows:
            path = flow.path
            last_hop = eval(path[-1])[0]
            last_hop_entity = self.cnc.Entities[last_hop]
            link_before_last_hop = path[-2]
            port = last_hop_entity.ingress_ports[link_before_last_hop]
            if port == 4:
                self.conn[last_hop].exec_command(
                    set_tree_port_cost(5, flow.id + 2, 5000000)
                )
            elif port == 5:
                self.conn[last_hop].exec_command(
                    set_tree_port_cost(4, flow.id + 2, 5000000)
                )

        # for entity in tqdm(self.cnc.Entities, desc='Set MSTP Pathcost'):
        #     if 'sw' not in entity.name:
        #         continue
        #     flow_to_port = {}
        #     for _, link in entity.links.items():

        #         for flow in link.flows:
        #             start = link.start
        #             end = link.end
        #             port = self.cnc.Entities[start].links[
        #                 f"({start}, {end})"].e_port
        #             flow_to_port[flow] = port

        #         ## Set the unused port with cost 5000000
        #         for flow in flow_to_port.keys():
        #             for port in [2, 3, 4, 5]:
        #                 if port != flow_to_port[flow]:
        #                     ## Tree_ID == VLAN_ID
        #                     self.conn[entity.id].exec_command(
        #                         set_tree_port_cost(port, flow + 2, 5000000))
        #                     print(
        #                         f"Set sw {entity.name} tree {flow+2} port {port} cost 5000000"
        #                     )

    def reset_mstp(
        self,
    ):
        for entity in tqdm(self.cnc.Entities[::-1], desc="Reset MSTP"):
            if "sw" in entity.name:
                self.conn[entity.id].exec_command(reset_vid2fid_map())
                self.conn[entity.id].exec_command(reset_fid2mstid_map())
                for tree_id in range(2, 2 + len(self.cnc._flow_set) + 1):
                    self.conn[entity.id].exec_command(delete_tree(tree_id))

    def set_gcl(
        self,
    ):
        for entity in tqdm(self.cnc.Entities, desc="Add GCL"):
            for link_name, link in entity.links.items():
                if "sw" in entity.name and link.active:
                    port = link.e_port
                    local_configs = "./configs/"
                    file_name = f"{entity.name}_{port}.cfg"
                    with open(local_configs + file_name, "w") as f:
                        f.writelines(gcl_to_cfg(link.GCL, link.cycle))

                    os.system(
                        "scp "
                        + f"{local_configs + file_name} {self.ssh_info[entity.id].username}@{self.ssh_info[entity.id].ip}:~/{file_name}"
                    )
                    self.conn[entity.id].exec_command(apply_gcl(entity.id, port))

    def reset_gcl(
        self,
    ):
        for entity in tqdm(self.cnc.Entities, desc="Clear GCL"):
            for link_name, link in entity.links.items():
                if "sw" in entity.name and link.active:
                    port = link.e_port
                    self.conn[entity.id].exec_command(reset_gcl(port))

    def find_pcp_mapping(
        self,
    ):
        """
        All flows assign PTP starts from 0 + 2
        If collusion occurs, add 1 to the PTP
        """
        pcp_mapping = {flow: 2 for flow in self.cnc._flow_set}
        success = False

        while not success:
            success = True
            for entity in tqdm(self.cnc.Entities, desc="Find PTP Mapping"):
                if "sw" in entity.name:
                    _mapping_check = {}
                    for link_id, link in entity.links.items():
                        for flow in link.flows:
                            queue = self.cnc.Flows[flow].queue[link_id]
                            prev_link_id = self.cnc.Flows[flow].get_prev_link(link_id)
                            pcp = pcp_mapping[flow]

                            ## PCP mapping is set on ingress port
                            for s_link_id, port in entity.ingress_ports.items():
                                _mapping_check.setdefault(port, {})
                                if s_link_id == prev_link_id:
                                    if pcp not in _mapping_check[port]:
                                        _mapping_check[port][pcp] = queue
                                    elif _mapping_check[port][pcp] != queue:
                                        success = False
                                        pcp_mapping[flow] += 1
                                        break
                            if not success:
                                break
                        if not success:
                            break
                    if not success:
                        break
        for flow, pcp in pcp_mapping.items():
            self.cnc.Flows[flow].PCP = pcp

    def set_pcp_mapping(
        self,
    ):
        ## Duplicate Mapping check
        for entity in tqdm(self.cnc.Entities, desc="Set PCP Mapping"):
            if "sw" in entity.name:
                _mapping_check = {}  ## {port: {PCP: queue}}
                for link_id, link in entity.links.items():
                    for flow in link.flows:
                        queue = self.cnc.Flows[flow].queue[link_id]
                        prev_link_id = self.cnc.Flows[flow].get_prev_link(link_id)
                        pcp = self.cnc.Flows[flow].PCP

                        ## PCP mapping is set on ingress port
                        for s_link_id, port in entity.ingress_ports.items():
                            _mapping_check.setdefault(port, {})
                            if s_link_id == prev_link_id:
                                if pcp not in _mapping_check[port]:
                                    _mapping_check[port][pcp] = queue
                                elif _mapping_check[port][pcp] != queue:
                                    print(
                                        f"[ERROR]: PCP {pcp} has been mapped to queue {queue} and {_mapping_check[port][pcp]}"
                                    )
                                    raise ValueError()
                                self.conn[entity.id].exec_command(
                                    add_pcp2queue_map(pcp, queue, port)
                                )

    def reset_pcp_mapping(
        self,
    ):
        for entity in tqdm(self.cnc.Entities, desc="Clear PCP Mapping"):
            if "sw" in entity.name:
                for port in [2, 3, 4, 5]:
                    self.conn[entity.id].exec_command(reset_pcp2queue_map(port))

    def clean_logs(
        self,
    ):
        for entity in tqdm(self.cnc.Entities, desc="Clean Logs"):
            if "es" in entity.name:
                self.conn[entity.id].exec_command(clean_logs())

    def set_sync(
        self,
    ):
        for entity in tqdm(self.cnc.Entities, desc="Set PTP"):
            if "es" in entity.name:
                self.conn[entity.id].exec_command(disable_ntp())
                self.conn[entity.id].exec_command(start_ptp4l("i210"))
                time.sleep(1)

        for entity in tqdm(self.cnc.Entities, desc="Set PHC"):
            if "es" in entity.name:
                self.conn[entity.id].exec_command(start_phy2sys("i210"))
                time.sleep(1)

    def end_sync(
        self,
    ):
        for entity in tqdm(self.cnc.Entities, desc="Set Sync"):
            if "es" in entity.name:
                self.conn[entity.id].exec_command(end_sync())

    def set_qdisc(
        self,
    ):
        for entity in tqdm(self.cnc.Entities, desc="Set Qdisc"):
            if "es" in entity.name:
                self.conn[entity.id].exec_command(config_qdisc("i210", "300000"))

    def reset_qdisc(
        self,
    ):
        for entity in tqdm(self.cnc.Entities, desc="Reset Qdisc"):
            if "es" in entity.name:
                self.conn[entity.id].exec_command(reset_qdisc("i210"))

    def start_tas(self, scheduled_time):

        for entity in tqdm(self.cnc.Entities, desc="Start TAS"):
            for link in entity.links.values():
                if "sw" in entity.name and link.active:
                    port = link.e_port
                    self.conn[entity.id].exec_command(
                        start_tas(port, link.cycle, scheduled_time, 0)
                    )
                    # print(f"Enable TAS on {entity.name} port sw0p{port}")

    def start_flow(self, scheduled_time):
        for entity in tqdm(self.cnc.Entities, desc="Start Flow"):
            if "es" in entity.name:
                for link in entity.links.values():
                    for flow in link.flows:
                        self.conn[entity.id].exec_command(
                            start_client(
                                expid=self.cnc.exp,
                                idd=flow,
                                interface="vlan" + str(flow + 2),
                                ip=f"192.168.{flow + 2}.2",
                                port=10000 + flow + 2,
                                period=self.cnc.Flows[flow].period * 10,
                                size=self.cnc.Flows[flow].size - 46 - 204,
                                sec=scheduled_time,
                                nsec=self.cnc.Flows[flow].period
                                - self.cnc.Flows[flow].offset,
                                pcp=self.cnc.Flows[flow].PCP,
                            )
                        )
                        print(f"SEND flow {flow} on {entity.name}")

        for flow in self.cnc.Flows:
            self.conn[flow.dst].exec_command(
                start_server(
                    expid=self.cnc.exp,
                    idd=flow.id,
                    interface="vlan" + str(flow.id + 2),
                    port=10000 + flow.id + 2,
                )
            )
            print(f"RECV flow {flow.id} on {self.cnc.Entities[flow.dst].name}")

    def stop_flow(
        self,
    ):
        for entity in tqdm(self.cnc.Entities, desc="Stop Flow Send"):
            if "es" in entity.name:
                self.conn[entity.id].exec_command(terminate_client())

        for flow in tqdm(self.cnc.Flows, desc="Stop Flow Recv"):
            self.conn[flow.dst].exec_command(terminate_server())

    def get_current_time(
        self,
    ):
        current_time = self.conn[0].exec_command("date +%s.%N")
        return int(current_time.split(".")[0])


def find_unique_file(folder, pattern):
    files = glob.glob(os.path.join(folder, pattern))
    if len(files) == 1:
        return files[0]
    elif len(files) == 0:
        raise FileNotFoundError(
            f"No files matching pattern '{pattern}' found in folder '{folder}'"
        )
    else:
        raise ValueError(
            f"Multiple files matching pattern '{pattern}' found in folder '{folder}': {files}"
        )


if __name__ == "__main__":
    try:
        # Parse command-line arguments
        parser = argparse.ArgumentParser(description="CNC Controller")
        parser.add_argument(
            "--topology",
            type=str,
            default="conf.json",
            help="Path to the topology file (conf.json)",
        )
        parser.add_argument(
            "--stream",
            type=str,
            default="stream.csv",
            help="Path to the stream file (stream.csv)",
        )
        parser.add_argument(
            "--schedule_folder",
            type=str,
            required=True,
            help="Path to the folder containing schedule files",
        )
        parser.add_argument(
            "--exp", type=str, default="Experiment", help="Experiment name"
        )

        args = parser.parse_args()

        EXP = args.exp

        cnc = CNC()
        cnc.exp = EXP
        cnc.init_topo(topology_file=args.topology)
        cnc.assign_flows(
            flow_path=args.stream,
            offset_path=find_unique_file(args.schedule_folder, "*-OFFSET.csv"),
            route_path=find_unique_file(args.schedule_folder, "*-ROUTE.csv"),
            queue_path=find_unique_file(args.schedule_folder, "*-QUEUE.csv"),
        )

        cnc.assign_GCL(gcl_path=find_unique_file(args.schedule_folder, "*-GCL.csv"))

        ## Init controller
        controller = Controller(cnc)
        controller.connect()
        controller.clean_logs()

        # # ###Unit test: Configure Qdisc ------------------------------------------
        print("[DEBUG]: Qdisc configuring")
        controller.reset_qdisc()
        time.sleep(3)
        controller.set_qdisc()
        time.sleep(3)
        # # # #### --------------------------------------------------------------------------

        # # #### Unit test: Configure all devices for VLAN ------------------------------------------
        print("[DEBUG]: VLAN configuring")
        controller.reset_vlan()
        time.sleep(3)
        controller.add_vlan()
        time.sleep(3)
        # # # #### --------------------------------------------------------------------------

        # # #### # Unit test: Configure all devices for MSTP ------------------------------------------
        controller.reset_mstp()
        print("[DEBUG]: MSTP configuring")
        controller.add_mstp()
        time.sleep(3)
        controller.set_mstp_root()
        time.sleep(3)
        controller.set_mstp_pathcost()
        #### --------------------------------------------------------------------------

        ### Unit test: Start SYNC ------------------------------------------
        print("[DEBUG]: Start network-wide synchronization")
        controller.end_sync()
        time.sleep(3)
        controller.set_sync()
        time.sleep(3)
        ## --------------------------------------------------------------------------

        # ###Unit test: Write PCP ------------------------------------------
        print("[DEBUG]: Configuring PCP")
        controller.reset_pcp_mapping()
        time.sleep(3)
        controller.find_pcp_mapping()
        controller.set_pcp_mapping()
        time.sleep(3)
        # # ###--------------------------------------------------------------------------

        ##Unit test: Write GCL ------------------------------------------
        print("[DEBUG]: Configuring GCL")
        controller.reset_gcl()
        time.sleep(3)
        controller.set_gcl()
        time.sleep(3)
        #### --------------------------------------------------------------------------

        # Unit test: Start flow ------------------------------------------
        WAITIME = 10
        RUNTIME = 100
        current_time = controller.get_current_time()
        print("[DEBUG]: The experiment will start at ", current_time + WAITIME)
        controller.start_tas(current_time + WAITIME)
        controller.start_flow(current_time + WAITIME)
        time.sleep(WAITIME + RUNTIME)
        # --------------------------------------------------------------------------

        ##### Unit test: Stop flow ------------------------------------------
        controller.stop_flow()
        controller.end_sync()
        time.sleep(3)
        ### --------------------------------------------------------------------------

        ## Disconnect controller
        controller.disconnect()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        controller.disconnect()
