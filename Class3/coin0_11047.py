import sys

coin, target = list(map(int, sys.stdin.readline().split()))
types = []
for i in range(coin):
    types.append(int(sys.stdin.readline()))
types.sort(reverse = True)
cnt = 0

for type in types:
    if target // type:
        cnt += target // type
        target %= type

print(cnt)