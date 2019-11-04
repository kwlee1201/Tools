import dpkt
import socket
import datetime
import pandas as pd

def df_pcap(pcap):
    pcap_list = list()
    for ts, buf in pcap:
        info = list()
        try:
            time = str(datetime.datetime.utcfromtimestamp(ts))
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src_ip = socket.inet_ntoa(ip.src)
            src_port = ip.data.sport
            dst_ip = socket.inet_ntoa(ip.dst)
            dst_port = ip.data.dport
            pcap_list.append([time, src_ip, src_port, dst_ip, dst_port])
            # print("[+] ", time, src_ip, src_port, dst_ip, dst_port)
        except:
            pass
    return pd.DataFrame(pcap_list, columns=["Time","SrcIP","SrcPort","DstIP","DstPort"])


filename = "sample.pcap"
file = open(filename, "rb")
pcap = dpkt.pcap.Reader(file)
df_pcap_ = df_pcap(pcap)
