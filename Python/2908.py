a, b = input().split()
a = a[2]+a[1]+a[0]
b = b[2]+b[1]+b[0]

if a>b:
    print(int(a))
elif a<b:
    print(int(b))