import sys
input = lambda: sys.stdin.readline().rstrip()

a = input()
b = input()
b_len = len(b)
c = b[-1]
stack = []

for i in a:
    stack.append(i)

    if len(stack) >= b_len and ''.join(stack[-b_len:]) == b:
        del stack[-b_len:]

if len(stack) == 0:
    print('FRULA')
elif len(stack) != 0:
    print(''.join(stack))