import sys

queue = []
def is_empty(queue:list):
    if len(queue):
        return 0
    else:
        return 1

def pop(queue:list):
    if is_empty(queue):
        return -1
    else:
        return queue.pop(0)

def front(queue:list):
    if is_empty(queue):
        return -1
    else:
        return queue[0]
    
def back(queue:list):
    if is_empty(queue):
        return -1
    else:
        return queue[-1]
    
commands = int(sys.stdin.readline().rstrip())
for i in range(commands):
    line = sys.stdin.readline().rstrip().split()
    if line[0] == 'push':
        queue.append(line[1])
    elif line[0] == 'pop':
        print(pop(queue))
    elif line[0] == 'front':
        print(front(queue))
    elif line[0] == 'back':
        print(back(queue))
    elif line[0] == 'size':
        print(len(queue))
    elif line[0] == 'empty':
        print(is_empty(queue))