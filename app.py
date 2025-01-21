from connector import *

option = "Choose option:\n\n1.Sub-Enum\n2.Dir-Enum\n3.ARP Network Scan\n4.Port Scan\n5. Hash Cracking(MD5)\n6.SSH BruteForce\n>> "

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
    target_ip = "enter a target ip: "
    target_ip = input(target_ip)
    port_scan(target_ip)
elif option == "5":
    text = input("Enter a hash: ")
    wl = input("Enter a wordlist location: ")
    hash_type = input("Enter a hash type: ")
    hash_cracker(text=text,wordlist=wl,hash_type=hash_type)
elif option == "6":
    usr = input("Enter a username: ")
    pass_file = input("Enter a passwords file: ")
    target_ip = input("Enter a target IP: ")
    port = input("Port: ")
    ssh_brute(username=usr,pass_file=pass_file,port=port,target_ip=target_ip)
