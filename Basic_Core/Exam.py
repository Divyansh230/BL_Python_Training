m1, m2, m3, m4, m5 = map(int, input().split())

marks = [m1, m2, m3, m4, m5]

if any(mark < 35 for mark in marks):
    print("FAIL")
else:
    avg = sum(marks) / 5

    if avg >= 75:
        print("DISTINCTION")
    else:
        print("PASS")