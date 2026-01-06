a = input()
l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
i = 0
ans = 0

while i < len(a):
    if a[i:i+3] in l:
        ans += 1
        i += 3
    elif a[i:i+2] in l:
        ans += 1
        i += 2
    else:
        ans += 1
        i += 1

print(ans)