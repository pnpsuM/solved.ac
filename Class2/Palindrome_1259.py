while (1):
    num = int(input())
    if num == 0: break
    original = num
    rev = 0
    while num:
        rev *= 10
        rev += num % 10
        num //= 10
    if rev == original:
        print('yes')
    else:
        print('no')