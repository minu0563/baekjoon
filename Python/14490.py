from math import gcd

a = input()
num1, num2 = a.split(':')
ans = gcd(int(num1), int(num2))
print(str(int(int(num1)/ans)) + ':' + str(int(int(num2)/ans)))