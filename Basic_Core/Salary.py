late=int(input("enter late"))
absent=int(input("enter absent"))

salary=int(input("enter salary"))
if late>5:
    salary=salary-salary*5/100
    if absent>2:
        salary=salary-salary*5/100

if late>10:
    salary=salary-salary*10/100
    if absent>2:
        salary=salary-salary*5/100

print(salary)

