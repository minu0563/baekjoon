n = 1000 - int(input())
a = [500, 100, 50, 10, 5, 1]

b = 0

for i in a:
    while n >= i:
        n -= i
        b += 1

print(b)