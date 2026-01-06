a = int(input())
b = list(map(int, input().split()))

c = max(b)

d = [(i)/c*100 for i in b]
print(sum(d)/a)