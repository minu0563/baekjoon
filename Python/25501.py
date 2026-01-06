def recursion(s, l, r):
    if l >= r: 
        return 1, 1
    elif s[l] != s[r]: 
        return 0, 1
    else: 
        result, count = recursion(s, l + 1, r - 1)
        return result, count + 1

def isPalindrome(s):
    result, count = recursion(s, 0, len(s) - 1)
    return result, count

for i in range(int(input())):
    a = input()
    result, count = isPalindrome(a)
    print(result, count)