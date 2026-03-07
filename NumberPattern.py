num = input()

flag = True

for i in range(len(num) - 1):
    if num[i] >= num[i + 1]:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")