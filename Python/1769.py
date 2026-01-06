a = input()
ans_1 = 0

while len(a) > 1:
    x = sum(int(i) for i in a)
    a = str(x)
    ans_1 += 1

if int(a) % 3 == 0:
    print(ans_1)
    print('YES')
else:
    print(ans_1)
    print('NO')
