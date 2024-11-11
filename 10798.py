l = []
ans = []
max_len = 0

for _ in range(5):
    l.append(list(input()))

for y in l:
    if len(y) > max_len:
        max_len = len(y)

for i in range(max_len):
    for x in l:
        try:
            ans.extend(x[i])
        except:
            pass
            
print(''.join(ans))