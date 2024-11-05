# a = int(input())
# b = list(map(int,input().split()))
# t, p = map(int,input().split())
# shr = 0
# pen = 0
# pen_1 = 0

# for i in b:
#     if i <= t and i != 0:
#         shr += 1
#     elif i == 0:
#         continue
#     else:
#         while True:
#             if i % t == 0:
#                 shr += i//t
#                 break
#             else:
#                 i -= t
#                 shr += 1
#                 if i <= 0:
#                     break
# if a % p == 0:
#     pen += a // p
# else:
#     while True:
#         if a % p == 0:
#             pen += a//p
#             break
#         else:
#             a -= 1
#             pen_1 += 1
#             if a <= 0:
#                 break

# print(shr)
# print(pen, pen_1)

a = int(input())
b = list(map(int, input().split()))
t, p = map(int, input().split())

shr = sum(i // t + (1 if i % t != 0 else 0) for i in b if i != 0)

pen = a // p
pen_1 = a % p

print(shr)
print(pen, pen_1)