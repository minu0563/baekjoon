b = []

for i in range(9):
    a = int(input())
    b.append(a)
    
c = max(b)
print(c)
print(b.index(max(b))+1)