sentence=input()
c=0
for char in sentence:
    if char in 'aeiouAEIOU':
        c+=1

print(c)