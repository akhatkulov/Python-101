
def subdomain_enum(target):
    import requests
    import sys

    with open("data/wordlists/bitquark-subdomains-top100000.txt",'r') as f:
        sub_name_list = f.read()
    sub_name_list = sub_name_list.splitlines()

    for subname in sub_name_list:
        target_url = f"http://{subname}.{target}"

        try:
            requests.get(target_url)
        except requests.ConnectionError:
            pass
        else:
            print("--[+]--",target_url)

