import sys

set = []
def set_add(set:list, value):
    if check(set, value):
        return
    else:
        set.append(value)
        return set

def set_remove(set:list, value):
    if check(set, value):
        set.remove(value)
        return set
    else:
        return

def check(set:list, value):
    if value in set:
        return 1
    else:
        return 0
    
def set_toggle(set:list, value):
    if check(set, value):
        set.remove(value)
        return set
    else:
        set.append(value)
        return set
    
def set_all(set:list):
    set = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    return set

def set_empty(set:list):
    set = []
    return set
    
commands = int(sys.stdin.readline().rstrip())
for i in range(commands):
    line = sys.stdin.readline().rstrip().split()
    if line[0] == 'add':
        set_add(set, line[1])
    elif line[0] == 'remove':
        set_remove(set, line[1])
    elif line[0] == 'check':
        print(check(set, line[1]))
    elif line[0] == 'toggle':
        set_toggle(set, line[1])
    elif line[0] == 'all':
        set = set_all(set)
    elif line[0] == 'empty':
        set = set_empty(set)