a = 0
while True:
    try:
        N = list(map(int, input().split()))
        a += 1
        if N[0] != 0:
            print(f"Case {a}: Sorting... done!")
        else:
            break
    except:
        break