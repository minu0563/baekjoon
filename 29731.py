import sys

l = ['Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you', 'Never gonna stop']
l_1 = []
for i in range(int(input())):
    l_1.append(input())

for x in l_1:
    if x in l:
        pass
    elif x not in l:
        print('Yes')
        sys.exit()

print('No')