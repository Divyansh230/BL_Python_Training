def is_Prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

a=int(input("enter first number"))
b=int(input("enter second number"))

for i in range(a,b+1):
    if is_Prime(i):print(i)

