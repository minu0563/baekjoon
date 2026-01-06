a = int(input())
b = []
for i in range(a):
    c =input().split()
    c = [str(c[0]), int(c[1]), int(c[2]), int(c[3])]
    b.append(c)

b.sort(key= lambda x: (-x[3], -x[2],-x[1]))
print(b[0][0], b[-1][0], sep='\n')