#!/usr/bin/env python3
import os
import random

INTERFACE = "wlan0"  # Change if your Wi-Fi interface is different

def random_mac():
    """Generate a random, locally administered MAC address."""
    mac = [0x02,  # locally administered
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(f"{x:02x}" for x in mac)

def change_mac():
    new_mac = random_mac()
    print(f"Changing {INTERFACE} MAC to {new_mac}")
    os.system(f"ip link set {INTERFACE} down")
    os.system(f"ip link set {INTERFACE} address {new_mac}")
    os.system(f"ip link set {INTERFACE} up")

if __name__ == "__main__":
    change_mac()
