vowel = ['a', 'e', 'i', 'o', 'u']
accept = ['ee', 'oo']
is_acceptable = True

while True:
    password = input()
    if password == "end":
        break
    
    for i in range(0, len(password)):
        is_acceptable = False
        if password[i] in vowel:
            is_acceptable = True
            break
    
    if not is_acceptable:
        print(f"<{password}> is not acceptable.")
        is_acceptable = True
        continue

    for i in range(0, len(password)-1):
        if password[i] == password[i+1] and password[i:i+2] not in accept:
            is_acceptable = False
            break

    if not is_acceptable:
        print(f"<{password}> is not acceptable.")
        is_acceptable = True
        continue

    for i in range(0, len(password)-2):
        if (password[i] in vowel and password[i+1] in vowel and password[i+2] in vowel) or (password[i] not in vowel and password[i+1] not in vowel and password[i+2] not in vowel):
            is_acceptable = False
            break

    if not is_acceptable:
        print(f"<{password}> is not acceptable.")
        is_acceptable = True
        continue

    print(f"<{password}> is acceptable.")