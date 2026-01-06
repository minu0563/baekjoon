import math

def bino_coef_factorial(n, k):
    return math.factorial(n) // (math.factorial(n-k) * math.factorial(k))

n, k = map(int, input().split())
print(bino_coef_factorial(n, k))