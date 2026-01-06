ham = []
coke = []

for i in range(3):
    ham.append(int(input()))
for i in range(2):
    coke.append(int(input()))

ham.sort()
coke.sort()

print(ham[0]+coke[0]-50)