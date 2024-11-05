import sys
input = lambda: sys.stdin.readline().rstrip()

a = int(input())

for i in range(a):
    num_1, num_2 = map(int, input().split())

    num_1 = '0b'+ str(num_1)
    num_2 = '0b'+ str(num_2)
    
    num_1 = int(num_1, 2)
    num_2 = int(num_2, 2)
    
    ans = num_1 + num_2

    ans = bin(ans)
    ans = str(ans)[2:]

    print(ans)