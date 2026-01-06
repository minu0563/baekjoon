import sys
a = sys.stdin.readline().rstrip()
n = sorted(a, reverse=True)
print(''.join(n))