# Not quite sure what this program will be quite yet

import socket


def main():
    print(greeting())
    lanScan()


def greeting():
    print(""" _   _   ___       _____      
    | | | | /   |     |  _  |     
    | |_| |/ /| |_   _| |/' | ___ 
    |  _  / /_| \ \ / /  /| |/ __|
    | | | \___  |\ V /\ |_/ / (__ 
    \_| |_/   |_/ \_/  \___/ \___|
    """)
    print("Wifi pentesting suite")
    input("Press enter to continue")
    print("\n"
          "1. LAN Scan - Enumerate devices on your local network\n"
          # "# 2. Port scan -  \n"
          "\n"
          "\n")


def lanScan():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localAddress = socket.gethostbyname(socket.gethostname())
    print("Local IP: " + localAddress)
    input()
