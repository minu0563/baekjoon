import sys
input = lambda: sys.stdin.readline().rstrip()

ans = 0
ans_1 = 0
for _ in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        ans_1 += b

    if c == 'A+':
        ans += b*4.5
    elif c == 'A0':
        ans += b*4.0
    elif c == 'B+':
        ans += b*3.5
    elif c == 'B0':
        ans += b*3.0
    elif c == 'C+':
        ans += b*2.5
    elif c == 'C0':
        ans += b*2.0
    elif c == 'D+':
        ans += b*1.5
    elif c == 'D0':
        ans += b*1.0
    elif c == 'F':
        ans += b*0.0
    elif c == 'P':
        pass

print(ans/ans_1)