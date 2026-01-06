A, B = input().split()
c = 0

for i in range(len(A)):
    for j in range(len(B)):
        c += int(A[i])* int(B[j])

print(c)