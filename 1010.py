import math

T = int(input())

resultList = []
for i in range(T):
    N, M = map(int, input().split())
    result = math.comb(M, N)  # 조합 계산
    resultList.append(result)

for i in range(len(resultList)):
    print(resultList[i])
