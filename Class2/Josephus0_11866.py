import sys

num, index = tuple(map(int, sys.stdin.readline().split()))
seat = []
for i in range(1, num + 1):
    seat.append(i)

index -= 1
start = 0
print('<', end = '')
while seat:
    loc = (index + start) % num
    if len(seat) > 1:
        print(f'{seat.pop(loc)}, ', end = '')
    else:
        print(f'{seat.pop(loc)}>')
    start = loc
    num = len(seat)