l = list(map(int, input().split()))
l_1 = list(map(int, input().split()))
a = 0
b = 0

a = l[0]*3 + l[1]*20 + l[2]*120
b = l_1[0]*3 + l_1[1]*20 + l_1[2]*120

if a == b:
    print('Draw')
elif a < b:
    print('Mel')
elif a > b:
    print("Max")