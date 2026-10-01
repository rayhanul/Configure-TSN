Why your results don't show TSN's guarantees yet
TSN bounds latency, jitter and loss from switch port to switch port, for frames that arrive inside their scheduled gate window. Your current measurement adds two parts TSN doesn't control:

The sender, a Python sleep loop. It releases frames tens to hundreds of µs off their window, while the windows are a few µs wide. A late frame waits for the next cycle (latency, deadline misses), and a burst can overflow a queue (the sw02 drops).
The receiver, Python threads. They timestamp late and lose packets when their buffers fill (S2's 56% delivery and 27 ms latency).
So most of what the table shows comes from the end hosts, not the network.

What to change, in order of impact
1. Measure at the NIC, not in Python (needed for any valid TSN result)

Use hardware TX and RX timestamps (SO_TIMESTAMPING), so latency runs from the moment the sender's NIC sends to the moment the receiver's NIC receives. Both NIC clocks are PTP-synced to about ±100 ns.
Software delays then drop out of the latency and jitter numbers.
2. Stop receiver loss on S2 (fixes most of the loss)

Raise socket buffers: sysctl -w net.core.rmem_max=33554432 and set SO_RCVBUF per socket. That's quick, but it only hides the lag.
The real fix is fewer, faster receivers: one epoll loop per node instead of 21 threads, or a single raw capture that reads all flows with hardware timestamps.
Check after a run that nstat UdpRcvbufErrors didn't grow.
3. Release frames exactly on schedule (fixes deadline misses and the switch drops)

Use SO_TXTIME with the etf qdisc and offload on the I210. The NIC itself sends each frame at basetime + psi_ns, accurate to tens of ns, and Python's timing stops mattering.
This is the step from my earlier answer. The base time and TAI offset it needs are now in place.
The I210 has launch time only on queues 0 and 1, so map pcp 7 to queue 0 and pcp 6 to queue 1.
4. Then check the network itself

With steps 1–3 in place, any remaining loss or deadline miss is a real network or schedule problem.
Watch the switch Q DROP counters (ethtool -S sw0pX) before and after each run.
Look into the 249 ns grid offset on 11 of the 27 switch ports.
Check the schedule's assumptions (proc_delay_ns 2000, prop_delay_ns 0) against measured per-hop delay.
5. Host tuning (only if needed after step 3)

Pin the generator to a dedicated CPU, run it with real-time priority (SCHED_FIFO), and turn off CPU power-saving states.
What to expect: after steps 1–3, flows should show 0 loss and latency close to the schedule's e2e_ns. For example, flow 1 should be about 8.6 µs, with jitter in the sub-µs range. If not, the report will point at a specific switch or schedule problem rather than at Python.

I'd do 1 and 2 first, because they show how good the network already is, then 3. Should I start? Each step ends with a rerun of run_experiment.py, into a new dated results folder.





