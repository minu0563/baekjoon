n = int(input())

def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result+=int(i)
    return result

arr = []
for i in range(n):
    a = input()
    arr.append(a)

arr.sort(key = lambda x:(len(x), sum_num(x), x))
"""
key는 정렬을 하는 기준,
lambda x:는 arr의 요소 하나를 꺼내와서 x에 대입함,
x는 길이, 숫자의 합, 알파벳 사전순을 기준으로 정렬됨
"""

for i in arr:
    print(i)