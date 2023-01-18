loop = int(input())
for i in range(loop):
    ans = ''
    itr, string = input().split()
    for ch in string:
        for j in range(int(itr)):
            ans += ch
    print(ans)