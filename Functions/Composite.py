def compose(f,g):
    return lambda x:f(g(x))

f=lambda x:x+1
g=lambda x:x**2

c=compose(g,f)
print(c(5))
print(f(5))