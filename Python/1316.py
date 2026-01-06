ans_1 = 0

for _ in range(int(input())):
    ans = []
    s = True
    a = input()

    for i in a:
        if i not in ans or ans[-1] == i:
            ans.append(i)
        else:
            s = False
            break
    
    if s:
        ans_1 += 1

print(ans_1)