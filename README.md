# scanip
IP and Mac address scanner ‒ Ubuntu

## dependencies
- tcpdump
- Python 2.7
  - scapy
- sudo

## test
```console
$ sudo python2 scanip.py
Begin emission:
Finished to send 256 packets.

Received 6 packets, got 3 answers, remaining 253 packets
xx:xx:xx:xx:xx:xx   192.168.0.1
xx:xx:xx:xx:xx:xx   192.168.0.34
xx:xx:xx:xx:xx:xx   192.168.0.12
```

```console
$ sudo python2
Python 2.7.13 (default, Dec 21 2016, 07:16:46) 
[GCC 6.2.1 20160830] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import scanip
>>> scanip.start_scan()
[('xx:xx:xx:xx:xx:xx', '192.168.0.1'), ('xx:xx:xx:xx:xx:xx', '192.168.0.34'), ('xx:xx:xx:xx:xx:xx', '192.168.0.12')]

```
