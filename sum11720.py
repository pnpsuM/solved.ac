length = int(input())
ans = 0
num = int(input())
for i in range(length):
    decimal_div = num % 10
    ans += decimal_div
    num //= 10
print(ans)