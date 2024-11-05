import sys

t = 1000000
N = int(sys.stdin.readline())
circle = [int(sys.stdin.readline()) for _ in range(N)]
list = [0]*(t+1) # circle 요소들 개수 세는 리스트 
cnt = [0]*(t+1) # 머리 툭툭 치는 횟수 저장하는 리스트 

for c in circle:
    list[c] += 1

for i in range(1,t+1):
    if list[i]: # list[i] != 0일 때 
        cnt[i] += list[i]-1 # 1을 뺀 것은 자기 자신을 제외하기 위함
        for j in range(i+i,t+1,i): # 2*i, 3*i, 4*i, ... 는 i의 배수이므로 j의 cnt에 i 개수를 더해준다. 
            cnt[j] += list[i]

answer = ""
for i in circle:
    answer += str(cnt[i]) + "\n"
print(answer)