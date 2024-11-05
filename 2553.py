import math
n = int(input())

fac = str(math.factorial(n))[::-1]

for i in fac:
    if i != '0':
        print(i)
        break