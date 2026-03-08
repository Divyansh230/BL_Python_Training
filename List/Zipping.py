# create two lists of same length
list1 = [1, 2, 3, 4]
list2 = ['A', 'B', 'C', 'D']

# combine using zip
result = list(zip(list1, list2))

print("List 1:", list1)
print("List 2:", list2)
print("Zipped List:", result)