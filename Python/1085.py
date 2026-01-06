x, y, w, h = map(int, input().split())

a = x
b = y
x = w-x
y = h-y

print(min(a,b,x,y))