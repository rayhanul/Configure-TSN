

```
python3 run-tsn-config-cnc.py   --ip 192.168.0.4   --user root   --cmd "tsntool st wrcl sw0p2 sw0p2.cfg"

```



To make the shell script executable:


```
chmod +x run_wrcl_100_times.sh

```



Now this the given amount of times using command :


```

./run_config_wrcl.sh 192.168.0.4 sw0p2 sw0p2.cfg

```


To plot result:

```
python result_manager.py wrcl_192.168.0.1_sw0p5_execution_times.csv wrcl_192.168.0.2_sw0p4_execution_times.csv wrcl_192.168.0.4_sw0p4_execution_times.csv
```



