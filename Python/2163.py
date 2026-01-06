h, m ,s = map(int, input().split())
fs = int(input())

j = s//60 #몫
k = s%60 #나머지
m += m+j
k += s+k
if s + k > 60:
    m += (s+k)//60
    s += ((s+k)//60)*60-s
elif s + k == 0:
    s -= 60
    m += 1
else:
    s= s+k

if m > 60:
    h += m//60
    m = (m//60)*60 - m
elif m == 60:
    h += 1
    m -= 60

if h > 24:
    h -= 24
    abs(h)

print(h, m, s)