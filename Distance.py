distance=int(input())

fare=distance*2

age=int(input())

if age>60:
    fare=fare*0.7
if age<12:
    fare=fare*0.5

print(fare)