# scanip
IP and Mac address scanner ‒ Ubuntu

## dependencies
- tcpdump
- Python 2.7
  - scapy
- sudo

## test
```python
import scanip
scanip.start_scan()
```

```
Begin emission:
.**Finished to send 256 packets.
***..................................
Received 40 packets, got 5 answers, remaining 251 packets
xx:xx:xx:xx:xx:xx <---------> 192.168.0.1
xx:xx:xx:xx:xx:xx <---------> 192.168.0.34
xx:xx:xx:xx:xx:xx <---------> 192.168.0.12
xx:xx:xx:xx:xx:xx <---------> 192.168.0.11
xx:xx:xx:xx:xx:xx <---------> 192.168.0.14
```
