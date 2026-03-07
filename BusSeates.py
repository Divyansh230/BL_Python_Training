n = int(input())

seats = 40

for _ in range(n):
    req = int(input())

    if req <= seats:
        print("CONFIRMED")
        seats -= req
    else:
        print("WAITLISTED")