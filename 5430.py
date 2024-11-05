import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    ac = input().strip()
    a = int(input().strip())
    try:
        num = deque(map(int, input().strip()[1:-1].split(',')))
        #[1,2,3] ==> deque([1,2,3])
    except:
        num = []
    reverse_num = False
    error = False

    for i in ac:
        if i == 'R':
            reverse_num = not reverse_num
            #R은 여러번 가능(reverse_num = True 하면 안됨)
        elif i == 'D':
            if len(num) == 0:
                error = True
                break
            else:
                if reverse_num == False:
                    #reverse_num == False라면 반전 안된거임
                    num.popleft()
                else:
                    num.pop()
    
    if error:
        #error == True
        print('error')
    else:
        if reverse_num == True:
            num.reverse()
            print(f"[{','.join(map(str, num))}]")
            #deque([1,2,3]) ==> [1,2,3]으로 출력
        else:
            print(f"[{','.join(map(str, num))}]")