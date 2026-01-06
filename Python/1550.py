a = input()  # 예: F1
l = [10, 11, 12, 13, 14, 15]
l_1 = ['A', 'B', 'C', 'D', 'E', 'F']
ans = 0

for i, char in enumerate(a[::-1]):
    if char in l_1:
        b = l[l_1.index(char)]
        ans += b * (16 ** i)
    else:
        ans += int(char) * (16 ** i)

print(ans)
