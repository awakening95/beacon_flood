from scapy.all import *

for i in range(5):
    sendp(RadioTap() /
          Dot11(addr1="ff:ff:ff:ff:ff:ff",
                addr2="11:11:11:11:11:11",
                addr3="11:11:11:11:11:11") /
          Dot11Beacon() /
          Dot11Elt(ID="SSID", info=b"KYJ1"),
          iface="mon0", loop=0)

    sendp(RadioTap() /
          Dot11(addr1="ff:ff:ff:ff:ff:ff",
                addr2="22:22:22:22:22:22",
                addr3="22:22:22:22:22:22") /
          Dot11Beacon(cap="ESS", timestamp=1) /
          Dot11Elt(ID="SSID", info=b"KYJ2"),
          iface="mon0", loop=0)

    sendp(RadioTap() /
          Dot11(addr1="ff:ff:ff:ff:ff:ff",
                addr2="33:33:33:33:33:33",
                addr3="33:33:33:33:33:33") /
          Dot11Beacon() /
          Dot11Elt(ID="SSID", info=b"KYJ3") /
          Dot11Elt(ID="Rates", info='\x00\x00\x00\x01'),
          iface="mon0", loop=0)
