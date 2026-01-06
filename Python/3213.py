# pizza = []

# for i in range(int(input())):
#     pizza.append(input())
#     ans = 0

# while True:
#     if len(pizza) == 0:
#         break

#     if pizza.count('1/2') // 2 >= 1 and pizza.count('1/2') % 2 >= 0:
#         ans += pizza.count('1/2') // 2
#         if pizza.count('1/2') % 2 != 0:
#             count_1 = pizza.count('1/2')-1
#         else:
#             count_1 = pizza.count('1/2')
#         for _ in range(count_1):
#             pizza.remove('1/2')
#             continue
#     elif '3/4' in pizza and '1/4' in pizza:
#         ans += 1
#         pizza.remove('3/4')
#         pizza.remove('1/4')
#     elif pizza.count('1/4') // 4 >= 1 and pizza.count('1/4') % 4 >= 0:
#         ans += pizza.count('1/4') // 4
#         if pizza.count('1/4') % 2 != 0:
#             count_2 = pizza.count('1/4')-1
#         else:
#             count_2 = pizza.count('1/4')
#         for _ in range(count_2):
#             pizza.remove('1/4')
#     elif '1/2' in pizza and pizza.count('1/4') == 2:
#         ans += 1
#         pizza.remove('1/2')
#         pizza.remove('1/4')
#         pizza.remove('1/4')
#     elif '1/2' not in pizza and '3/4' not in pizza and '1/4' in pizza:
#         ans += 1
#         for _ in range(pizza.count('1/4')):
#             pizza.remove('1/4')
#     else:
#         ans += len(pizza)
#         pizza.clear()

# print(ans)

pizza = []

# 입력 받기
for _ in range(int(input())):
    pizza.append(input())

# 피자 조각 개수 세기
count_3_4 = pizza.count('3/4')
count_1_2 = pizza.count('1/2')
count_1_4 = pizza.count('1/4')

ans = 0

# '3/4' 피자 처리
ans += count_3_4
count_1_4 = max(0, count_1_4 - count_3_4)

# '1/2' 피자 처리
ans += count_1_2 // 2
if count_1_2 % 2:
    ans += 1
    count_1_4 = max(0, count_1_4 - 2)

# '1/4' 피자 처리
ans += count_1_4 // 4
if count_1_4 % 4:
    ans += 1

print(ans)
