from connector import *

option = "Choose option:\n\n1.Sub-Enum\n2.Dir-Enum\n3.ARP Network Scan\n4.Port Scan>> "

option = input(option)

if option == "1":
    target = "enter a target domain name: "
    target = input(target)

    subdomain_enum(target)
elif option == "2":
    target = "enter a target domain name: "
    target = input(target)

    dir_enum(target)
elif option == "3":
    interface = input("Enter a interface: ")
    ip_range = input("Enter a ip range(10.10.X.X/24): ")
    arp_scan(interface,ip_range)
elif option == "4":
    target_ip = "enter a target ip"
    target_ip = input(target_ip)
    port_scan(target_ip)
