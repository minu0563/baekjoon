a = int(input())

for i in range(a):
    a, b = input().split()
    text = ''
    for i in range(len(b)):
        text += int(a)*b[i]
    print(text)