num, target = list(map(int, input().split()))
candidates = list(map(int, input().split()))
max = 0
length = len(candidates)
for k in range(length):
    for i in range(length - 1, k + 1, -1):
        temp = candidates[k] + candidates[i]
        for j in range(k + 1, i):
            if temp + candidates[j] <= target and temp + candidates[j] > max:
                max = temp + candidates[j]
print(max)