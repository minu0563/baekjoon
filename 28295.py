import sys
input = sys.stdin.readline

x = 1080

for _ in range(10):
    a = int(input())

    if a == 1:
        x += 90
    elif a == 2:
        x += 180
    elif a == 3:
        x -= 90
x //= 90
x %= 4

if x == 0:
    print('N')
elif x == 1:
    print('E')
elif x == 2:
    print('S')
else:
    print('W')