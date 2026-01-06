import sys
input = sys.stdin.readline

a, b = map(int, input().split())
name = []
l = []

for _ in range(a):
    name.append(input().strip())

for _ in range(b):
    l.append(input().strip())


for i in l:
    l_1 = []
    try:
        l_1.append(int(i)-1)
        print(name[l_1[0]])
    except:
        print(name.index(i)+1)