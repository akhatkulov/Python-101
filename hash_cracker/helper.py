
def hash_cracker(text,wordlist,hash_type):
    import hashlib 
    print('--[-]--')
    with open(wordlist,'r') as f:
        for l in f.readlines():
            if hash_type == "md5":
                hash_ob = hashlib.md5(l.strip().encode())
                hash_res = hash_ob.hexdigest()
            elif hash_type == "sha256":
                hash_ob = hashlib.sha256(l.strip().encode())
                hash_res = hash_ob.hexdigest()
            
            if hash_res == text:
                print("--[+]--",l)
                exit(0)
            else:
                print("--[x]--",l)
