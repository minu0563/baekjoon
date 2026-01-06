while True:
    a = input()
    b = 0
    if 'END' in a:
        break

    b = a[::-1]
    print(b)