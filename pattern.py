from re import sub
file = "all_passwords.txt"
with open(file) as f:
    with open("all_password_patterns.txt", "w") as outfile:
        for line in f:
            word_pattern = sub("[A-Z]", 'S', line.strip())
            word_pattern = sub("[ÄÕÖÜŽŠ]", 'Ö', word_pattern)
            word_pattern = sub("[А-ЯЁЃЂЊІЅЋЏЌЄЇ]", 'U', word_pattern)
            word_pattern = sub("[a-z]", 'V', word_pattern)
            word_pattern = sub("[äõöüžš]", 'Ä', word_pattern)
            word_pattern = sub("[а-яà-ÿёїѓµћјђґєњљіўѕќџ]", 'L', word_pattern)      
            word_pattern = sub("[0-9]", 'N', word_pattern)
            word_pattern = sub('[\W\_ ³]', 'X', word_pattern)
            outfile.write(f"{word_pattern}\n")
        

with open(file) as f:
    with open("all_password_patterns_alt.txt", "w") as outfile:
        for line in f:
                word_pattern = sub("[A-ZŽŠÄÕÖÜА-ЯЁЃЂЊІЅЋЏЌЄЇ]", 'S', line.strip())
                word_pattern = sub("[a-zžšäõöüа-яà-ÿёїѓµћјђґєњљіўѕќџ]", 'V', word_pattern)    
                word_pattern = sub("[0-9]", 'N', word_pattern)
                word_pattern = sub('[\W\_ ³]', 'X', word_pattern)
                outfile.write(f"{word_pattern}\n")
        