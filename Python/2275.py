for i in range(int(input())):
    k = int(input()) #층
    n = int(input()) #호
    people = [i for i in range(1, n+1)]

    for x in range(k):
        new = []
        for y in range(n):
            new.append(sum(people[:y+1]))
        people = new.copy()

    print(people[-1])