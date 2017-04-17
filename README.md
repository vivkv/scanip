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
***Finished to send 256 packets.
*...
Received 7 packets, got 4 answers, remaining 252 packets
('xx:xx:xx:xx:xx:xx', '192.168.0.1')
('xx:xx:xx:xx:xx:xx', '192.168.0.27')
('xx:xx:xx:xx:xx:xx', '192.168.0.34')
('xx:xx:xx:xx:xx:xx', '192.168.0.12')
```

hint:
```python
import sys; import scanip; del sys.modules['scanip']; import scanip; scanip.start_scan();
```
