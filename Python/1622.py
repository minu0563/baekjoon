try :
    while True :
        ans = []
        a = input()
        b = input()
        
        for s in a :
            if s in b :
                ans += [s]
                b = b.replace(s, '', 1)  # s를 ''으로 1개만 대체함
        ans.sort()
        print(''.join(ans))
except :
    pass