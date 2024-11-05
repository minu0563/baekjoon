x = int(input())

a = [64,32,16,8,4,2,1]
b = 0

for i in range(len(a)):
    if x >= a[i]:
        b += 1
        x -= a[i]
    
    if x == 0:
        break
print(b)