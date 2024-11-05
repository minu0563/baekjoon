import sys
input = sys.stdin.readline

num=[]
a = 0
b = {}
c = 0

for i in range(int(input())):
    num.extend(map(int, input().split()))
num.sort()


for i in num:
    a += i
j = a/len(num)
print(round(j))
print(num[len(num)//2])

for i in num:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1

maxi = max(b.values())
max_b = []
for i in b:
    if maxi == b[i]:
        max_b.append(i)

if len(max_b) == 1:
    print(max_b[0])
else:
    print(max_b[1])

print(max(num) - min(num))