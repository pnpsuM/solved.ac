import sys

while(1):
    num1, num2, num3 = tuple(map(int, sys.stdin.readline().rstrip().split()))
    if not num1 and not num2 and not num3:
        break
    num1 **= 2
    num2 **= 2
    num3 **= 2
    hypotenuse = max(num1, num2, num3) # 빗변
    if num1 + num2 + num3 - hypotenuse == hypotenuse:
        print('right')
    else:
        print('wrong')