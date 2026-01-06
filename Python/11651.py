num = []

for i in range(int(input())):
    x, y = map(int, input().split())
    num.append((x, y))

#y 좌표를 먼저, x좌표를 두번째로 정렬하기
num.sort(key=lambda x: (x[1], x[0]))

for x, y in num:
    print(x, y)