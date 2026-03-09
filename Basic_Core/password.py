password=input("enter your password")

if len(password)>8:
    exit()

isCap=False
isDigit=False
for ch in password:
    if ch.isdigit():isDigit=True
    if ch.isupper():isCap=True

if isCap and isDigit:
    print("STRONG")
else:
    print("WEAK")