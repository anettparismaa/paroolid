def readPasswords(path="all.txt"):
    passwords = set()
    with open(path) as f:
        for line in f:
            passwords.add(line.strip())
    return passwords

all_passwords = readPasswords("all.txt").union(readPasswords("out/all.txt"))

print(f"Total passwords: {len(all_passwords)}")
with open("all_passwords.txt", "w") as f:
    f.write("\n".join(all_passwords))