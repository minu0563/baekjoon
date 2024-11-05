for _ in range(int(input())):
    a = []
    for i in range(int(input())):
        a.append(input())
    ans = 0
    found_palindrome = False

    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                s = a[i] + a[j]
                if s == s[::-1]:
                    print(s)
                    found_palindrome = True
                    break            
        if found_palindrome:
            break
    if not found_palindrome: #found뭐시기가 False인 경우 참
        print(0)