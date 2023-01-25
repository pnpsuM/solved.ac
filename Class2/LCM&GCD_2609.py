import sys

# 유클리드 호제법
def EUC_GCD(A, B):
    flag = A % B
    if flag:
        return EUC_GCD(B, flag)
    else: 
        return B
    
num1, num2 = tuple(map(int, sys.stdin.readline().rstrip().split()))
GCD = EUC_GCD(num1, num2)
LCM = num2 * num1 // GCD
print(GCD)
print(LCM)