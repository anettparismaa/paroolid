import sys
from re import match

regex = r"[\w\d.]*@\w+\.ee\:(.+)"

def readPasswords(path="all.txt"):
    passwords = set()
    with open(path) as f:
        for line in f:
            passwords.add(line.strip())
    return passwords

if __name__ == "__main__":
    dump  = sys.argv[1]
    passwords = readPasswords()
    newPasswords = set()

    with open(dump,  encoding="iso-8859-1") as f:
        for line in f:
            matchObj = match(regex, line)
            if matchObj:
                newPasswords.add(matchObj.group(1))

    with open(f"{dump.replace('.txt', '.out.txt')}", "w") as f:
        f.write("\n".join(newPasswords))

    with open("all.txt", "w") as f:
        f.write("\n".join(passwords.union(newPasswords)))

    print(f"Found {len(newPasswords)} new passwords")
    print(f"Total passwords: {len(passwords.union(newPasswords))}")
                
