import sys

R = 31 # 26보다 큰 제일 작은 소수
M = 1234567891 # 큰 소수

length = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

sum = 0
for i, ch in enumerate(string, 0):
    sum += (ord(ch) - 96) * pow(R, i)
hash_code = sum % M

print(hash_code)