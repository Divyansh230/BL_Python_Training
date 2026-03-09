amount=int(input())

if amount>=5000:
    amount=amount-amount*1/5
elif amount>=3000:
    amount=amount-amount*1/10
elif amount>=1000:
    amount=amount-amount*1/20
else:
    print("Not possible")
print(amount)