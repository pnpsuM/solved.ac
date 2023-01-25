import sys
length = int(sys.stdin.readline())
nums = []
for i in range(length):
    num = int(sys.stdin.readline())
    if num:
        nums.append(num)
    else:
        nums.pop()
print(sum(nums))