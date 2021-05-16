from scapy.all import *
from collections import Counter

import pandas as pd
import numpy as np
import glob


def readPcap(filepath):
  print('filenpath:', filepath)
  content = list()
  pcap = rdpcap(filepath)
  for i, p in enumerate(pcap):
    # check the ip is ipv4 or ipv6 or ...
    if IP in p:
      srcip = p[IP].src
      dstip = p[IP].dst
    elif IPv6 in p:
      srcip = p[IPv6].src
      dstip = p[IPv6].dst
    elif Dot3 in p:
      srcip = p[Dot3].src
      dstip = p[Dot3].dst
    elif ARP in p:
      ip_type = ARP
      srcip = p[ARP].psrc
      dstip = p[ARP].pdst
    else:
      print('number:', i)
    # extract srcip and dstip
    content.append({'srcip':srcip, 'dstip':dstip})
  data = pd.DataFrame(content)
  return data

def calDist(df):
  df = df.copy()
  df1 = df.groupby(['srcip','dstip']).size().reset_index(name='count')
  df1['percentage'] = df1['count'] / df1['count'].sum()
  v = df1['percentage'].values.max()
  return v


if __name__=='__main__':
  filepath = 'any.run/*.pcap'
  pcap_list = glob.glob(filepath)
  dist = list()
  for pcap in pcap_list:
    df = readPcap(pcap)
    v = np.round(calDist(df), decimals=1)
    dist.append(v)  
  stat = Counter(dist)
  print(stat)
