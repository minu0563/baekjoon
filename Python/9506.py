while True:
    x = int(input())
    divisor_set = set()

    if x == -1:
        break
    #int(x**0.5) + 1 --> x의 제곱근까지의 범위
    for divisor in range(1, int(x**0.5) + 1):
        if x % divisor == 0:
            divisor_set |= {divisor, x // divisor}
    divisor_set = list(divisor_set)
    divisor_set.remove(x)
    divisor_set.sort()
    sum_num = sum(divisor_set)

    if sum_num == x:
        print(f'{x} = {" + ".join(map(str, divisor_set))}')
    else:
        print(f'{x} is NOT perfect.')