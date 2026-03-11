def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

fibonacci=fib(10)
print(next(fibonacci))
print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))


x=(x**2 for x in range(10))



