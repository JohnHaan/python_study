## CIDR To IP Range

from netaddr import *
import pprint

R_FILENAME = 'azure_ips.json'
W_FILENAME = 'azure_ip_range.json'


if __name__ == '__main__':
    w = open(W_FILENAME, 'w')
    with open(R_FILENAME, 'r') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            i = i+1
            ip  = IPNetwork(line)
            ip_list = list(ip)
            if i % 20 == 0:
                w.write(str(ip_list[0])+"-"+str(ip_list[-1])+"\n")
            else:
                w.write(str(ip_list[0])+"-"+str(ip_list[-1])+",")

w.close()
