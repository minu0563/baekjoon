for i in range(3):
    a = list(map(int,input().split()))
    # print(a[3]-a[0], a[1]-a[4], a[2]-a[5])
    b = a[3]-a[0]
    c = a[4]-a[1]
    d = a[5]-a[2]
    
    if c < 0:
        b -= 1
        c = (60-a[1])+a[4]
    if d < 0:
        if c > 0:
            c -= 1
            d = (60-a[2])+a[5]
        elif c <= 0:
            b -= 1
            c = 59
            d = (60-a[2])+a[5]
    print(b, c, d)