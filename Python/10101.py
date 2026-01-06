A = []
for i in range(3):
    a = int(input())
    A.append(a)
if len(set(A)) == 1 and A[0] == 60:
    print('Equilateral')
elif sum(A) == 180:
    if A[0] == A[1] or A[1] == A[2] or A[2] == A[0]:
        print('Isosceles') 
    else:
        print('Scalene')
else:
    print('Error')