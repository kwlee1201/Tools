import os
import dpkt
import socket
import datetime
import pandas as pd
import numpy as np


def arpProcess(eth):
    arp = eth.arp
    src_ip = socket.inet_ntoa(arp.spa)
    src_port = np.nan
    dst_ip = socket.inet_ntoa(arp.tpa)
    dst_port = np.nan
    return [src_ip, src_port, dst_ip, dst_port]


def normalProcess(eth):
    ip = eth.data
    src_ip = socket.inet_ntoa(ip.src)
    src_port = ip.data.sport
    dst_ip = socket.inet_ntoa(ip.dst)
    dst_port = ip.data.dport
    # print("[+] ", src_ip, src_port, dst_ip, dst_port)
    return [src_ip, src_port, dst_ip, dst_port]


def df_pcap(pcap):
    pcap_list = list()
    for ts, buf in pcap:
        info = list()
        time = str(datetime.datetime.utcfromtimestamp(ts))
        eth = dpkt.ethernet.Ethernet(buf)
        try:
            if eth.type == 2054:
                pcap_list.append([time]+self.arpProcess(eth))
            else:
                pcap_list.append([time]+self.normalProcess(eth))
        except:
            pass
    return pd.DataFrame(pcap_list, columns=["Time","Source","SrcPort","Destination","DstPort"])


if __name__=='__main__':
    filename = "sample.pcap"
    file = open(filename, "rb")
    pcap = dpkt.pcap.Reader(file)
    df_pcap_ = df_pcap(pcap)
    print("the shape of the df_pcap_ is:", df_pcap_.shape)
    print("the samples of the df_pcap_ are:", df_pcap_.head(5))