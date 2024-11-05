# while True:
#     a = list(map(int, input().split()))
#     max = 0

#     if a[0] == 0 and a[1] == 0 and a[2] == 0:
#         break
#     else:
#         f = max(a)
#         a.remove(f)
#         if f**2 == a[0]**2 + a[1]**2:
#             print('right')
#         else:
#             print('wrong')


while True:
    a = list(map(int, input().split()))

    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    else:
        max_val = max(a)
        a.remove(max_val)
        if max_val**2 == a[0]**2 + a[1]**2:
            print('right')
        else:
            print('wrong')


