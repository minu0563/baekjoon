def Fibonacci(n):
    if n < 1:
        return 0
    elif n < 2 and n >= 1:
        return 1
    else:
        fb = [0]*(n+1)
        fb[0], fb[1] = 0, 1
        for i in range(2, n+1):
            fb[i] = Fibonacci(i-1) + Fibonacci(i-2)
        return fb[n]
    
print(Fibonacci(int(input())))