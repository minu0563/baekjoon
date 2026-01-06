import sys
input = lambda: sys.stdin.readline().rstrip()

a = list(str(input()))
l = []
ans = []
ans_f = ""

for i in a:
    l.append(ord(i))

s = l[0]
ans.append(s)

for i in range(1, len(l)):
    if s < l[i]:
        ans.reverse()
        ans.append(l[i])
        ans.reverse()
    else:
        s = l[i]
        ans.append(l[i])

for i in reversed(ans):
    ans_f += chr(i)

print(ans_f)