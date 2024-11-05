a = int(input())
b = int(input())
c = int(input())
s = str(a*b*c)
d = 0

for i in range(10):
    print(s.count(str(i))) 