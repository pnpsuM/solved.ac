import sys

num = int(sys.stdin.readline())
# 1부터 시작해서 역방향으로
d = [0] * (num+1) # 0부터 n번 인덱스 포함 리스트

for i in range(2,num+1): # 2 ~ num

    d[i] = d[i-1]+1 # +1 연산
    if i%3 == 0:
        d[i] = min(d[i],d[i//3]+1) # //3 연산
    if i%2 == 0:
        d[i] = min(d[i],d[i//2]+1) # //2 연산

print(d[num])

# original #
# memo = {}

# memo[num] = 0

# def make_one(num):
#     cnt = memo[num] + 1
    
#     ans = num - 1
#     try: memo[ans] = min(cnt, memo[ans])
#     except: memo[ans] = cnt
#     ans = num // 2
#     if num % 2 == 0:
#         try: memo[ans] = min(cnt, memo[ans])
#         except: memo[ans] = cnt
#     ans = num // 3
#     if num % 3 == 0:
#         try: memo[ans] = min(cnt, memo[ans])
#         except: memo[ans] = cnt
#     return num - 1

# for i in range(num):
#     num = make_one(num)