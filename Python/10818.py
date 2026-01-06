import sys
input = sys.stdin.readline

N = int(input())
*a, = map(int, input().split())
print(min(a), max(a))