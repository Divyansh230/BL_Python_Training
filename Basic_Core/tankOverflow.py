n = int(input())
inflows = list(map(int, input().split()))

tank = 0

for i in range(n):
    tank += inflows[i]

    if tank > 1000:
        print(i + 1)
        break