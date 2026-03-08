from random import randint

lst = [randint(1,10) for i in range(10)]

print(lst)

lst.sort()        # correct way
print(lst)

lst = list(set(lst))
print(lst)