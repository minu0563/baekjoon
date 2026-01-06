l = []
for i in range(int(input())):
    l.append(int(input()))

b = 0
for i in l:
    if i % 2 != 0:
        b += 1
print(b)