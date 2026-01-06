import sys
input = lambda: sys.stdin.readline().rstrip()

a = list(input())
b = list(input())
ans = 0

if a == b: # a랑 b랑 같으면 0출력후 멈추기
    print(0)
    exit()
else:
    if sorted(a) != sorted(b): #만약 정렬했는데도 
        print(-1)
        exit()
    else:
        while a: #만약 밑에서 a[-1] != b[-1]이라는 조건을 통과하지 못해도 len(a)가 0이 아니라면 다시 한번더 돌리기
            while a and b and a[-1] == b[-1]:  #맨 뒤에가 같으면 안 옮겨도 됨 -> 없애기
                a.pop()
                b.pop()
            while a and a[-1] != b[-1]: # 맨 뒤에가 다르면 a에서만 지우기 == 다른 부분을 앞으로 옮겼다고 생각하기
                a.pop()
                ans += 1

print(ans)