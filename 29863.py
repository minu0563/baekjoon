a = int(input())
b = int(input())
c = 0
while True:
    if a < 24 and a >= 12:
        a += 1
        c += 1
    elif a == 24:
        print(c + b)
        break
    elif a < 12:
        print(b - a)
        break