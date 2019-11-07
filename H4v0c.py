# Not quite sure what this program will be quite yet
# https://www.raspberrypi.org/forums/viewtopic.php?t=188615
# print(os.popen("ip -4 route show default").read().split()) --- Enter in python CLI, examine further
import socket
import os
import sys
import threading

from debian.debtags import output


def greeting():
    print("""
     _   _   ___       _____      
    | | | | /   |     |  _  |     
    | |_| |/ /| |_   _| |/' | ___ 
    |  _  / /_| \ \ / /  /| |/ __|
    | | | \___  |\ V /\ |_/ / (__ 
    \_| |_/   |_/ \_/  \___/ \___|
    """)
    print("     Wifi pentesting suite")
    input("     Press enter to continue")
    print("\n"
          "     1. LAN Scan - Enumerate devices on your local network\n"
          # "# 2. Port scan -  \n"
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

    target = input("\nPlease enter the target IP or range:  ")
    targetIP = socket.gethostbyname((target))
    startRange = input("Define port range start: ")
    endRange = input("Define port range end: ")
    print("Working...\n")

    try:
        for port in range(int(startRange), int(endRange)):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((targetIP, port))
                if result == 0:
                    print("Port: " + str(port) + " is open: ")
                    try:
                        print(socket.getservbyport(port) + "\n")
                    except OSError:
                        print("Unknown service\n")

                else:
                    pass
    except KeyboardInterrupt:
        print("\nYou pressed Ctrl+C")
        sys.exit()



greeting()
lanScan()
