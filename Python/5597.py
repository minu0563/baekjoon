a = []
for i in range(31):
    a += [i]

for _ in range(28):
    a[int(input())] = 0
a.sort()
del a[:29]
print(*a,sep='\n')