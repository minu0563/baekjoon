# for i in range(int(input())):
#     a = list(input())
#     sum = 0

#     for x in range(len(a)):
#         if a[x] == '(':
#             sum += 1
#         else:
#             sum -= 1

#         if a[-1] == '(':
#             sum -= 2
            
#     if sum < 0 or sum >0:
#         print('NO')
#     else:
#         print('YES')

for i in range(int(input())):
    a = list(input())
    sum = 0
    is_valid = True

    for x in range(len(a)):
        if a[x] == '(':
            sum += 1
        else:
            sum -= 1
        
        if sum < 0:
            is_valid = False
            break

    if sum != 0:
        is_valid = False
    
    if is_valid:
        print('YES')
    else:
        print('NO')