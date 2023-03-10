import sys

N = int(sys.stdin.readline())
paper = []

for col in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

def split_paper(paper, len, cnt_W, cnt_B, y, x):
    len //= 2
    for index_y, index_x in [(0, 0), (0, len), (len, -len), (0, len)]:
        y += index_y
        x += index_x
        # print(f'x, y: {x, y}')
        sum_ = 0
        for row in paper[y:y + len]:
            # print(row[x:x + len])
            sum_ += sum(row[x:x + len])
        # print(f'sum_:{sum_}')
        if sum_ == 0:
            cnt_W += 1
            # print(f'W: {cnt_W}')
        elif sum_ == len ** 2:
            cnt_B += 1
            # print(f'B: {cnt_B}')
        else:
            cnt_W, cnt_B = split_paper(paper, len, cnt_W, cnt_B, y, x)
            # print(f'W: {cnt_W}')
            # print(f'B: {cnt_B}')
            
    return cnt_W, cnt_B

cnt_B = 0
cnt_W = 0
sum_ = 0

for row in paper:
    sum_ += sum(row)
if sum_ == 0:
    cnt_W += 1
elif sum_ == N ** 2:
    cnt_B += 1
else:
    cnt_W, cnt_B = split_paper(paper, N, cnt_B, cnt_W, 0, 0)
print(cnt_W)
print(cnt_B)