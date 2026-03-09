def func(a,b=None):
    if b is None:
        b={}
    b[a]=a**2
    return b

print(func(2))
