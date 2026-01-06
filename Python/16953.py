a, b = map(int, input().split())
count = 0

while True:
    if b == a:
        print(count+1)
        break
    elif b < a:
        print(-1)
        break

    if b %2 == 0:
        b //= 2
        count += 1
    elif b  % 10 == 1: #10으로 나누었을때
        b //=10        #나머지가 1이라면
        count +=1      #b의 마지막수는 1임       
    else:
        print(-1)
        break