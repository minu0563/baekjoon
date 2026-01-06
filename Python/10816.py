import sys
from collections import Counter
input = sys.stdin.readline

# 입력 처리
a = int(input())
b = list(map(int, input().split()))
c = int(input())
lst = list(map(int, input().split()))

# Counter를 사용하여 리스트 b의 요소 개수를 셈
counter_b = Counter(b)

# 결과를 저장할 리스트
num = []

# lst의 각 요소에 대해 개수를 찾아서 num에 추가
for i in lst:
    num.append(counter_b[i])

# 결과 출력
print(*num, end='')
