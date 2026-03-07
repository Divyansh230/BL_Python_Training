correct_pin=input("Enter your PIN: ")

flag=1
while True:
    if flag>3:
        break
    pin=input(f"attempt {flag}")
    if pin == correct_pin:print("ACCESS GRANTED")
    print("LOCKED")

