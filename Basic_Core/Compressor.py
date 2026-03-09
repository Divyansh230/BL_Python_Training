number=int(input())

minutes=0
while number>0:
    if number%2==0:
        number=number//2
        minutes=minutes+1
    else:
        break
print(minutes)