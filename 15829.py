n = int(input())
char = list(input())

for i in range(n):
    char[i] = ord(char[i]) - 96

c = 0
for i in range(n):
    c += (31 ** i) * int(char[i])

print(c  % 1234567891) 