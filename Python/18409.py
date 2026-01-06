a = int(input())
b = input()
l = ['a', 'e', 'i', 'o', 'u']
c = 0

for i in l:
    if i in b:
        c += b.count(i)

print(c)