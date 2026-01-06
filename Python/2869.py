# a, b, v = map(int, input().split())
# day = 0

# while True:
#     if v > 0:
#         v -= a
#         if v == 0:
#             day += 1
#             print(day)
#             break
#         else:
#             v += b
#             day += 1
#     elif v <= 0:
#         print(day)
#         break

a, b, v = map(int, input().split())

# 하루에 (a-b) 만큼 올라갈 수 있을 때, 최소 몇 일이 걸리는지 계산
day = (v - b - 1) // (a - b) + 1

print(day)
