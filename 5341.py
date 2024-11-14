while True:
    a = int(input())
    b = 0

    if a == 0:
        break

    for i in range(1,a+1):
        b += i
    
    print(b)