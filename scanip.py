from __future__ import print_function
import subprocess
import types
from scapy.all import *
import os

def arp_scan(ipandsub):
   packet = Ether(dst = "ff:ff:ff:ff:ff:ff" )/ARP(pdst=ipandsub)
   ans,unans = srp(packet,timeout=2,iface="eth0")
   values=[]
   for s,r in ans:
      temp = r.sprintf("%Ether.src% <---------> %ARP.psrc%")
      values.append(temp)
   return values
	  
def calculate_network_id(ip_bin,subnet,net_addr):
   subnet_position = (subnet/8) 
   position_boundary = (subnet % 8) 
   calc_octet = ['0','b']
   if position_boundary > 0:
      for i in range(2,position_boundary+2):
         calc_octet.append(ip_bin[subnet_position][i])
      for i in range(position_boundary+2,10):
         calc_octet.append('0')
      ip_bin[subnet_position] = ''.join(calc_octet)
      if subnet_position < 3:
         for i in range(subnet_position+1,len(ip_bin)):
            ip_bin[i] = '0b00000000'
         
   if (position_boundary == 0 ):
      for i in range(subnet_position,len(ip_bin)):
         ip_bin[i] = '0b00000000'
   for i in range(0,4):
      net_addr.append(ip_bin[i])
   return net_addr
   
def start_scan():
   f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
   ip=f.read()
   ip_list = ip.split(".")
   ip_bin = []
   for i in ip_list:
      each_bin = str(bin(int(i))).lstrip("0b")
      if len(each_bin) < 10:
         if len(each_bin) < 8:
            for j in range(1,(9 - len(each_bin))):
               each_bin = '0'+str(each_bin)
         each_bin = '0b'+str(each_bin)
      ip_bin.append(each_bin)     	  

   proc = subprocess.Popen('ifconfig',stdout=subprocess.PIPE)
   while True:
      line = proc.stdout.readline()
      if 'HWaddr' in line:
         break
   mask = proc.stdout.readline().rstrip().split(b':')[-1]
   mask = mask.split(".")
   mask_bin = []
   subnet = 0
   net_addr = []
   for i in mask:
      bin_eq  = bin(int(i))
      mask_bin.append(bin_eq)
      for i in range(2,len(str(bin_eq))):
         if bin_eq[i] == "1":
            subnet += 1
   netid = calculate_network_id(ip_bin,subnet,net_addr)
   network_id = str(int(netid[0],2))+"."+str(int(netid[1],2))+"."+str(int(netid[2],2))+"."+str(int(netid[3],2))
   #print(network_id)
   ipandsub = network_id+"/"+str(subnet)
   values=[]
   values = arp_scan(ipandsub)
   for i in values:
      #print(i)
   #return values
if __name__ == "__main__":
   start_scan()

