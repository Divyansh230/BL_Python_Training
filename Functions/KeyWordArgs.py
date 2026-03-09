def filter_integers(**kwargs):
    return {k:v for k,v in kwargs.items() if isinstance(v,int)}

print(filter_integers(a=1, b='two', c=3, d=4.5))  # {'a': 1, 'c': 3}
print(filter_integers(x=10, y='yes', z=20))