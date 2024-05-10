import os
import sys
from re import match
import codecs
#https://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php

regex = r"[\w\d.]*@\w+\.ee\:(.+)"
path = "../BreachCompilation/data"
#newPasswords = set()
#fname = []
password = set()

def readPasswords(path="out/all.txt", regex=r"[\w\d.]*@\w+\.ee\:(.+)"):
    newPasswords = set()
    with open(path, encoding="utf-8", errors='ignore') as f:
        for line in f:
            matchObj = match(regex, line)
            if matchObj:
                newPasswords.add(matchObj.group(1))
    return newPasswords

def writeAllPasswords(passwords):
    with open("out/all.txt", "w") as f:
            f.write("\n".join(passwords))

def writeNewPasswords(f_path, passwords):
    f_name = f_path.split("/")[-1]
    f_dir = f_path.split("/")[-2]
    with open(f"out/{f_dir}_{f_name}_out", "w") as f:
            f.write("\n".join(passwords))

for root,d_names,f_names in os.walk(path):      
    for f in f_names:
        f_path = os.path.join(root, f)
        #fname.append(f_path)
        #print(f_path)
        newPasswords = readPasswords(f_path)
        password = password.union(newPasswords)
        if	len(newPasswords) > 0:
            writeNewPasswords(f_path, newPasswords)
    print(f"Total passwords: {len(password)} passwords {f_path}")

writeAllPasswords(password)


