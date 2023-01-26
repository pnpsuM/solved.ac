import sys, math

len = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

def find_p(x):
    for i in range(2, math.floor(math.sqrt(x)) + 1):
            if x % i == 0:
                return 0
    return 1
# 목표의 제곱근까지 순회하면 모든 약수를 찾을 수 있다.

cnt = 0
for target in nums:
    if target != 1:
        cnt += find_p(target)
    
print(cnt)