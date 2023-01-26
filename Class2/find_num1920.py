import sys
import heapq as h

def binary_search(start, end, nums, target):
    while end - start >= 0:
        mid = (start + end) // 2
        if nums[mid] == target:
            return 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

len = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
sys.stdin.readline()
targets = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = len - 1

nums = sorted(nums)
for target in targets:
    print(binary_search(start, end, nums, target))