def readPasswords(path="all_password_patterns.txt"):
    passwords = set()
    with open(path) as f:
        for line in f:
            passwords.add(line.strip())
    return passwords

patterns = readPasswords()
allowed_char = "SÖUVÄLNXN"
i = 0
invalid = set()
for pwd in patterns:
    for char in pwd:
        if char not in patterns:
            print(f"Invalid character {char} in password {pwd}")
            i += 1
            invalid.add(char)
print(i)
print(invalid)

lowercase = ''
uppercase = ''
other = ''


passwords = readPasswords("all_passwords.txt")
for pwd in passwords:
    for char in pwd:
        if char in list(invalid):
            if char.islower() and char not in lowercase:
                lowercase += char
            elif char.isupper() and char not in uppercase:
                uppercase += char
            else:
                if char not in other and char not in lowercase and char not in uppercase:
                    other += char
            print(f"Invalid character {char} in password {pwd}")
            break

print(f"Lowercase: {lowercase}")
print(f"Uppercase: {uppercase}")
print(f"Other: {other}")
#{'Ї', 'ќ', 'ў', 'Њ', 'ґ', 'љ', 'џ', 'ѕ', 'Џ', 'І', 'є', 'і', 'µ', 'ѓ', 'Ѓ', 'Ќ', 'Є', 'ђ', 'њ', 'ј', '³', 'Ђ', 'Ћ', 'Ѕ', 'ї', 'ћ'}