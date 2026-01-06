import sys

def log10(x, pre = 1e-14):  # 상용로그용임
    low = 0
    high = 20
    
    while high - low >pre:
        mid = (low + high)/2
        try:
            ans = 10**mid
        except OverflowError:
            high = mid
            continue
        
        if ans < x:
            low = mid
        else:
            high = mid
            
    return (low + high) / 2

def ln(x, pre = 1e-14):  # 자연로그? 용암
    low = 0
    high = x
    
    while high - low >pre:
        mid = (low + high)/2
        ans = ex(mid)
        
        if ans < x:
            low = mid
        else:
            high = mid
            
    return (low + high) / 2

def ex(x, tem = 100):
    res = 1.0
    fac = 1.0
    pow = 1.0
    
    for i in range(1, tem):
        pow *= x
        fac *= i
        res += pow / fac
        if pow / fac < 1e-15:
            break
        
    return res

input = lambda: sys.stdin.readline().strip()
pi = 3.14159265358979323846

l = []
ln10 = ln(10)
log10_pi = log10(2 * pi)

for i in range(int(input())):
    a = int(input())
    loga = log10(a)
    awef = 0.5 * (log10_pi + loga)
    result = a * loga - a / ln10 + awef
    
    print(int(result) + 1)
    
    
# 자연로그, 상용로그 구현
# 테일러 급수 사용
# 이진 탐색 사용