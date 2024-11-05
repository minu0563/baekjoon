def power(a,b):
    c = 0
    c += a*b
    return c

a, b = map(int,input().split())
print(power(a,b))