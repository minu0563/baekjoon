while True:
    a = input()

    if int(a) == 0:
        break

    if a == a[::-1]:
        print('yes')
    elif a != a[::-1]:
        print('no')