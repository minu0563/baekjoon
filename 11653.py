import math

N = int(input())    # 나누어지는 수
d = 2               # 나누는 수
sqrt = int(math.sqrt(N)) # 나누어지는 수의 제곱근

# 나누는 수가 제곱근이하인 동안
while d <= sqrt:
    if N % d != 0:  # 나누어 떨어지지 않으면
        d += 1      # 나누는 수 1 증가
    else:           # 나누어 떨어지면
        print(d)    # 소인수니까 출력하고
        N //= d     # 나누어지는 수도 갱신

# 제곱근까지 나누어떨어지지 않으면, 소수이므로 그대로 출력
if N > 1:
    print(N)