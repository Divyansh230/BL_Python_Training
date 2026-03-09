def filter_and_map(map_func,filter_func,lst):
    return [map_func(x) for x in lst if filter_func]

print(filter_and_map(lambda x:x**2,lambda x:x%2==0,[1,2,3]))