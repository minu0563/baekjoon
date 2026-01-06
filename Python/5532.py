l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = 0
f = 0

while True: 
    if a > 0:
        a -= c
        e += 1
    elif a <= 0:
        break
    
while True:  
    if b > 0:
        b -= d
        f += 1
    elif b <= 0:
        break

if e > f:
    print(l-e)
else:
    print(l-f)