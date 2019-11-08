# Network diagnostic/ pentesting/ whatever tool written by Christian Geer - https://github.com/H4l0g3n
# Still in development
# Resources:
# https://www.raspberrypi.org/forums/viewtopic.php?t=188615
# https://stackoverflow.com/questions/13368659/how-can-i-loop-through-an-ip-address-range-in-python
# https://docs.python.org/3/library/socket.html

import socket
import os
import ipaddress


def greeting():
    print("""
     _   _   ___       _____      
    | | | | /   |     |  _  |     
    | |_| |/ /| |_   _| |/' | ___ 
    |  _  / /_| \ \ / /  /| |/ __|
    | | | \___  |\ V /\ |_/ / (__ 
    \_| |_/   |_/ \_/  \___/ \___|
    """)
    print("     Wifi penetration testing suite")
    input("     Press enter to continue ")
    print("\n"
          "     1. LAN Scan - Enumerate and scan devices on the local network\n"
          "\n"
          "\n")


def lanScan():
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ipaddr = s.getsockname()[0]
    gateway = gw[2]
    host = socket.gethostname()
    print("--------------------------------------")
    print("LOCAL")
    print("--------------------------------------")
    print("IP:", ipaddr, " GW:", gateway, " Host:", host)
    print("--------------------------------------")

    rangeStart = int(ipaddress.IPv4Address(input("\nIP range start: ")))
    rangeEnd = int(ipaddress.IPv4Address(input("IP range end:   ")))
    startRange = int(input("\nPort range start: "))
    endRange = int(input("Port range end: "))
    print("Working...\n")

    for ip in range(rangeStart, rangeEnd):
        print("-" * 50)
        response = os.system("ping -c 1 " + str(ip) + "\n")
        if response == 0:
            print("\n" + str(ipaddress.IPv4Address(ip)))
            for port in range(startRange, endRange):
                # print(port)    Uncomment this for diagnostic purposes
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((str(ip), port))
                if result == 0:
                    print("Port: " + str(port) + " is open: ")
                    try:
                        print(socket.getservbyport(port) + "\n")
                    except OSError:
                        print("Unknown service\n")
                        continue
                    continue
        else:
            pass


greeting()
lanScan()

input("Press enter to exit. :)")
