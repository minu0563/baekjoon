N=int(input())
ar=[]
for _ in range(N):
    arr=list(input())
    if arr[0]=='O':
        ar.append(1)
    else:
        ar.append(0)
    for i in range(1,len(arr)):
        if arr[i]=='O':
            if ar[i-1]>0:
                ar.append(ar[i-1]+1)
            else:
                ar.append(1)
        else:
            ar.append(0)
    print(sum(ar))
    ar=[]