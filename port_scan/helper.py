def port_scan(target_ip):
    import sys
    import socket
    
    open_ports = []

    ports = range(1,65535)

    def check(ip,port, res=1):
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(0.5)
            r = sock.connect_ex((ip,port))
            if r == 0:
                res = 0 
            sock.close()
        except:
            pass
        return res 

    for port in ports:
        sys.stdout.flush()
        res = check(target_ip,port)
        if res == 0: open_ports.append(port)

    if open_ports: 
        print ("Open Ports are: ") 
        print (sorted(open_ports)) 
    else: 
        print ("Looks like no ports are open :(")
