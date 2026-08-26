for i in {8..1}
do
    ssh -o StrictHostKeyChecking=no root@192.168.0.$i "mstpctl setvid2fid br0 0:2-255"
    ssh -o StrictHostKeyChecking=no root@192.168.0.$i "mstpctl setfid2mstid br0 0:2-255"
done


for i in {8..1}
do
    # ssh -o StrictHostKeyChecking=no root@192.168.0.$i "for i in {2..255}; do mstpctl deletetree br0 $i; done"
    for k in {2..36}
    do
        ssh -o StrictHostKeyChecking=no root@192.168.0.$i "mstpctl deletetree br0 $k"
    done
done


