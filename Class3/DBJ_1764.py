import sys
import heapq as h

(D, B) = map(int, sys.stdin.readline().split())
names = []
for i in range(D + B):
    name = sys.stdin.readline().rstrip()
    hash_code = hash(name)
    h.heappush(names, (name, hash_code))
code = 0
cnt = 0
ans = []
while len(names):
    name, hash_code= h.heappop(names)
    if code != hash_code:
        code = hash_code
    else:
        cnt += 1
        ans.append(name)
print(cnt)
while len(ans):
    print(ans.pop(0))