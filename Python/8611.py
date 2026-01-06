def ans(n, q):
    base = ''

    while n > 0:
        n, mod = divmod(n, q)
        base += str(mod)

    rev_base = base[::-1]

    return base, rev_base

a = int(input())
l = []

for i in range(2, 11):
    num_1, num_2 = ans(a, i)
    if num_1 == num_2:
        l.append([i, num_2])

if len(l) == 0:
    print('NIE')
else:
    for i in l:
        print(i[0], i[1])