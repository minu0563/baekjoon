a = input()

if '7' not in a and int(a) % 7 != 0:
    print(0)
elif '7' not in a and int(a) % 7 == 0:
    print(1)
elif '7' in a and int(a) % 7 != 0:
    print(2)
elif '7' in a and int(a) % 7 == 0:
    print(3)