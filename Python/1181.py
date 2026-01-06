N = int(input())
b = []
c = []
for i in range(N):
    a = input()
    b.append(a)

for x in b:
    if (len(x),x) in c:
        set(x)
    else:
        c.append((len(x),x))
    
c.sort()

for j in c:
    print(j[1])