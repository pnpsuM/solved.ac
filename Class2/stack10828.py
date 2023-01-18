import sys

stack = []
def is_empty(stack:list):
    if len(stack):
        return 0
    else:
        return 1

def pop(stack:list):
    if is_empty(stack):
        return -1
    else:
        return stack.pop()

def top(stack:list):
    if is_empty(stack):
        return -1
    else:
        return stack[-1]
    
commands = int(sys.stdin.readline().rstrip())
for i in range(commands):
    line = sys.stdin.readline().rstrip().split()
    if line[0] == 'push':
        stack.append(line[1])
    elif line[0] == 'pop':
        print(pop(stack))
    elif line[0] == 'top':
        print(top(stack))
    elif line[0] == 'size':
        print(len(stack))
    elif line[0] == 'empty':
        print(is_empty(stack))