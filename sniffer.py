from scapy.all import sniff

def process_packet(packet):
    try:
        print(packet.summary())
    except Exception as e:
        print("Error:", e)

print("Sniffer is initiating...")

sniff(iface="Wi-Fi", prn=process_packet, store=False)



"""


snif(): Listen to network traffic

iface: your current network card which you connect to the inernet

prn: when the packet captured this parameter triggered the functions

store = False: prevents RAM to filling up

"""