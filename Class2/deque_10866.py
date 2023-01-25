import sys
from collections import deque

dq = deque()

def is_empty(dq:deque):
    if len(dq):
        return 0
    else:
        return 1
    
def front(dq:deque):
    if is_empty(dq):
        return -1
    else:
        return dq[0]
    
def back(dq:deque):
    if is_empty(dq):
        return -1
    else:
        return dq[-1]
    
commands = int(sys.stdin.readline().rstrip())
for i in range(commands):
    line = sys.stdin.readline().rstrip().split()
    if line[0] == 'push_front':
        dq.appendleft(line[1])
    elif line[0] == 'push_back':
        dq.append(line[1])
    elif line[0] == 'pop_front':
        if is_empty(dq):
            print(-1)
        else:
            print(dq.popleft())
    elif line[0] == 'pop_back':
        if is_empty(dq):
            print(-1)
        else:
            print(dq.pop())
    elif line[0] == 'front':
        print(front(dq))
    elif line[0] == 'back':
        print(back(dq))
    elif line[0] == 'size':
        print(len(dq))
    elif line[0] == 'empty':
        print(is_empty(dq))