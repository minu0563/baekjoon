while True:
    try:
        a = input()
        a = a.strip()
        print(a)
    except EOFError:
        break