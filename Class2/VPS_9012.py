import sys

# Valid Parenthesis String
length = int(sys.stdin.readline().rstrip())

for i in range(length):
    stack = []
    flag = False
    line = sys.stdin.readline().rstrip()
    for ch in line:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            try:
                s = stack.pop()
                if s != '(':
                    flag = True
            except IndexError:
                flag = True
    if len(stack) or flag:
        print('NO')
    else:
        print('YES')