def dir_enum(target):
    import requests
    
    with open("data/wordlists/directory-list-2.3-medium.txt",'r') as f:
        dir_list = f.read()

    dir_list = dir_list.splitlines()

    for dir_name in dir_list:
        target_link = f"http://{target}/{dir_name}"
        res = requests.get(target_link)

        if res.status_code==404:
            pass
        else:
            print(f"--[{res.status_code}]--",target_link)
