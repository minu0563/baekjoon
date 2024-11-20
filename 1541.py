import sys
input = lambda: sys.stdin.readline().rstrip()

a = input().split('-')
first_part = sum(map(int, a[0].split('+')))
rest_part = sum(sum(map(int, part.split('+'))) for part in a[1:])

print(first_part - rest_part)