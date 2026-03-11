def even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def squares(nums):
    for n in nums:
        yield n * n

for i in squares(even(5)):
    print(i)