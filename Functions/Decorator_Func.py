import time

def time_tracker(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'{func.__name__} took {end-start} seconds')
        return result
    return wrapper

@time_tracker   
def complex_calculation(n):
    return sum(x**2 for x in range(n))

# Test
print(complex_calculation(10000))