import sys

sys.stdin.readline()
nums = sys.stdin.readline().rstrip().split()
sys.stdin.readline()
targets = sys.stdin.readline().rstrip().split()

for i in targets:
    if i in nums:
        print('1') 
    else: print('0')
    
    # 이진 탐색 시도할 것