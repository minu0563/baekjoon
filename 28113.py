a, b, c = map(int, input().split())
if b == c:
    print('Anything')
elif b < c:
    print('Bus')
elif a <= c:
    if c < b:
        print('Subway')