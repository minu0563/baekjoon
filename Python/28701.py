a = int(input())
b = 0
c = 0
d = 0
for i in range(1,a+1):
    b += i
    d += i**3

c += b ** 2
print(b)
print(c)
print(d)