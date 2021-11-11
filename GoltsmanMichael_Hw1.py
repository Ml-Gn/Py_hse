com_emails = 0
for i in range(0, 999):
    email = input()
    if email == "STOP":
        break
    email_stripped = email.strip()
    if (email_stripped.count('@') != 1) or (email_stripped.count('.') < 2):
        print(f"invalid email {email}, please try again:")
    else:
        non_cyrillic_email = email_stripped.replace("с", "c")
        if non_cyrillic_email.rfind('.com') == len(non_cyrillic_email) - 4:
            com_emails += 1
print(com_emails)
