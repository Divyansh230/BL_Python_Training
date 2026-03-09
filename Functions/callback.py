def callback_app(callback,lst):
    return [callback(x) for x in lst]

print(callback_app(lambda x:x**2,[1,2,3]))