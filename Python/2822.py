sc = [int(input()) for i in range(8)]
sc_1 = sorted(sc)
sc_1 = sc_1[3:8]
sc_2 = sum(sc_1)

print(sc_2)
for i in sc:
    if i in sc_1:
        print(sc.index(i)+1, end=' ')