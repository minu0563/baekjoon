def power(a,b,c):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % c
            
        b //= 2
        a = (a*a) % c
    return result

a,b,c = map(int, input().split())
print(power(a,b,c))