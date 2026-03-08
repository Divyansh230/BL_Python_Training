# create list of first 10 positive integers
lst = list(range(1, 11))

print("Original List:", lst)

# remove elements at indices 2, 4, 6
lst.pop(6)
lst.pop(4)
lst.pop(2)

# insert 99 at index 5
lst.insert(5, 99)

print("Modified List:", lst)