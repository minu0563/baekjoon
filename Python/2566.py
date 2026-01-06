a = []
row = 0
column = 0
max_number = 0

for _ in range(9):
    a.append(list(map(int, input().split())))

for i in a:
    if max(i) > max_number:
        max_number = max(i)
        column = i.index(max(i))+1
        row = a.index(i)+1
    


print(max_number)

if max_number != 0:
    print(row, column)
elif max_number == 0:
    print(9, 9)