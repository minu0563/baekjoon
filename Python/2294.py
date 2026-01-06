n,k = map(int,input().split())
coins = list(int(input()) for _ in range(n))
dp = [100001]*(k+1) #동전의 가치는 100,000 보다 작거나 같음
dp[0] = 0 # k에 맞춰 dp인덱스 번호 맞추기

for coin in coins: #coins에 입력받은 값으로 k를 조져야됨
    for i in range(coin,k+1): #i = 정렬해둔 dp에 인덱스 값 (dp[i] = i)
        dp[i] = min(dp[i], dp[i-coin]+1)#두개중에 더 작은 값으로 dp[i] 변경

if dp[-1] == 100001: #마지막 인덱스가 100,001 이라면 변하지 않은것임
    print(-1)
else :
    print(dp[-1])