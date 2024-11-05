n = int(input())
a = 0

while True:
    if n %5 == 0:
        a += n//5
        break
    else:
        n -= 2
        a += 1

    if n < 0:
        break

if n< 0:
    print(-1)
else:
    print(a)