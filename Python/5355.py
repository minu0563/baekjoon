#@ --> *3
#% --> +5
## --> -7

for i in range(int(input())):
    l = list(input().split())
    try :
        l[0] = int(l[0])
    except:
        l[0] = float(l[0])
    ans = 0

    for x in range(len(l)):
        if isinstance(l[x], int) or isinstance(l[x], float):
            ans += l[x]
        elif l[x] == '@':
            ans *= 3
        elif l[x] == '%':
            ans += 5
        elif l[x] == '#':
            ans -= 7

    print(f"{ans:.2f}")