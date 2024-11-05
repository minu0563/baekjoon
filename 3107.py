l = (input().split(':'))
b = []

for i in range(len(l)):
    if len(l[i]) != 4 and len(l[i]) != 0:
        l[i] = '0' * (4-len(l[i])) + l[i]

    elif len(l[i]) == 0:
        b.append(i)

if len(l) != 8:
    if len(b) == 1:
        l = l[:b[0]] + ['0000'] * (8-len(l) + 1) + l[b[0] + 1:]
    else:
        for i in range(len(b)-1, 0, -1):
            if b[i] - b[i -1] == 1:
                l = l[:b[i - 1]] + ['0000'] * (8-len(l) + 1) + l[b[i-1] + 1:]
                break

for i in range(len(l)):
    if l[i] == '':
        l[i] = '0000'

        
print(':'.join(l))