#입력 '(' 후 입력이 ']'이라면 0
#입력 '(' 후 입력이 ')'이라면 2
#입력 '[' 후 입력이 ']'이라면 3
a = input()
stack = []
count = 0

for i in range(len(a)):
    if a[i] == '(' or a[i] == '[': #입력이 '(' 또는 '[' 일때
        stack.append(a[i])
    elif a[i] == ')': #만약 입력이 ')' 라면
        if not stack or stack[-1] == '[': #조건 1) 스택이 비어있지 않고 전에 입력되있는게 '['이라면
            count = 0 #옳지 않은 괄호 => 0
            break
        elif stack[-1] == '(': #전에'(' 이 입력되있었다면
            stack.pop() #'('을 지우고 그 위치에
            stack.append(2) # () == 2 을 넣기
        else:
            value = 0
            while stack and isinstance(stack[-1], int): #stack != 0 and stack[-1] == 정수형인지
                value += stack.pop()    #맞다면 calue에 값을 넣음
            if not stack or stack[-1] != '(': #입력이 ')'인 조건인데 원래 입력되었던게 '('이 아니라면 옳지 않음
                count = 0
                break
            stack.pop()
            stack.append(value * 2)
    elif a[i] == ']': #위에랑 똑같음
        if not stack or stack[-1] == '(':
            count = 0
            break
        elif stack[-1] == '[':
            stack.pop()
            stack.append(3)
        else:
            value = 0
            while stack and isinstance(stack[-1], int):
                value += stack.pop()
            if not stack or stack[-1] != '[':
                count = 0
                break
            stack.pop()
            stack.append(value * 3)

# 최종 계산
result = 0
for item in stack:
    if isinstance(item, int): #ex) 입력이 (()[[]])([])일때 stack = [22, 6]이 됨
        result += item #만약 item 이 정수이면 result에 item을 더해주고
    else:
        result = 0 #아니면 (['('] 또는 ['['] 이라면) 옳지 않은 코드라는 것
        break

print(result)