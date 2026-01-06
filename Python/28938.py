a = int(input())
l = list(map(int, input().split()))
b = 0

for i in l:
    b += i

if b <= -1:
    print('Left')
if b == 0:
    print('Stay')
if b >= 1:
    print("Right")