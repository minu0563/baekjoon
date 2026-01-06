while True:
    try:
        a, b = map(int, input().split())
        a += 1
        c = b/a
        print(int(c))
    except:
        break