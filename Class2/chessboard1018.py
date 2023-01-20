import sys

def white_start(board : list, s):
    cnt = 0
    for i, line in enumerate(board):
        for j, ch in enumerate(line[s:s+8]):
            if i % 2 == 0: # WB ~
                if j % 2 == 0: # W
                    cnt, ch = color_w(cnt, ch)
                else:
                    cnt, ch = color_b(cnt, ch)
            else: # BW ~
                if j % 2 == 0:
                    cnt, ch = color_b(cnt, ch)
                else:
                    cnt, ch = color_w(cnt, ch)
    return cnt

def black_start(board : list, s):
    cnt = 0
    for i, line in enumerate(board):
        for j, ch in enumerate(line[s:s+8]):
            if i % 2 == 0: # BW ~
                if j % 2 == 0: # B
                    cnt, ch = color_b(cnt, ch)
                else:
                    cnt, ch = color_w(cnt, ch)
            else: # WB ~
                if j % 2 == 0:
                    cnt, ch = color_w(cnt, ch)
                else:
                    cnt, ch = color_b(cnt, ch)
    return cnt

def color_w(cnt, ch):
    if ch != 'W':
        ch = 'W'
        cnt += 1
    return cnt, ch

def color_b(cnt, ch):
    if ch != 'B':
        ch = 'B'
        cnt += 1
    return cnt, ch

board = []
W_cnt = 987987987
B_cnt = 987987987
row, col = map(int, sys.stdin.readline().rstrip().split())
for line in range(row):
    board.append(sys.stdin.readline().rstrip())
for i in range(row - 7):
    for j in range(col - 7):
        temp = white_start(board[i:i+8], j)
        W_cnt = min(temp, W_cnt)
        temp = black_start(board[i:i+8], j)
        B_cnt = min(temp, B_cnt)

print(min(W_cnt, B_cnt))