def outer_funct():
    def inner_func(x):
        return x**2
    return inner_func

sq=outer_funct()
print(sq(5))