import sys
input = lambda: sys.stdin.readline().rstrip()

stack = []

a = int(input())-1
l = list(map(int, input().split()))

while a >= 1:
  if l:
    num = min(l)
    for i in l:
      if i > num:
        stack.append(i)
      elif i == num:
        l.remove(i)
        break
  
    for i in stack:
      if i in l:
        l.remove(i)

    for i in range(len(stack)):
        if l:
            if min(stack) > min(l):
                break
            elif min(stack) < min(l):
                stack.remove(min(stack))
        else:
            break

    a -= 1
  else:
    break

for i in range(len(stack)):
  num = min(stack)
  if stack[-1] == num:
    stack.pop()
  else:
    break

if len(stack) == 0:
  print("Nice")
elif len(stack) != 0:
  print("Sad")