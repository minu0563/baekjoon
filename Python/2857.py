b = []

for i in range(5):
    a = input()
    if 'FBI' in a:
        b.append(i+1)
    
if len(b) > 0:
    for x in b:
        print(x)
else:
    print('HE GOT AWAY!')