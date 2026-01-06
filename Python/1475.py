import sys
input = lambda: sys.stdin.readline().rstrip()

l = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
six = 0
nine = 0
ans = 0

a = list(input())

for i in a:
    if i in l:
        if int(i) == 6 and six <= nine:
            l[i] += 1
            six += 1
        elif int(i) == 6 and six > nine:
            l['9'] += 1
            nine += 1
        elif int(i) == 9 and nine <= six:
            l[i] += 1
            nine += 1
        elif int(i) == 9 and nine > six:
            l['6'] += 1
            six += 1
        else:
            l[i] += 1

print(max(l.values()))