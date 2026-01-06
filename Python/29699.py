a = "WelcomeToSMUPC"
b = int(input())

while True:
    if b > len(a):
        b -= len(a)
    elif b <= len(a):
        print(a[b-1])
        break