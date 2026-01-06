a = int(input())
b = 0
c = 666

while True:
    if '666' in str(c):
        b += 1
    
    if b == a:
        break

    c += 1

print(c)