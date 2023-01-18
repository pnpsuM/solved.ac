max = 0
index = 0
for i in range(1, 10):
    num = int(input())
    if num > max:
        max = num
        index = i
print(f'{max}\n{index}')