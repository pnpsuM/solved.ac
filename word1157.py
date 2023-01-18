def main():
    word = input()
    cnt = {}
    for char in word:
        char = char.upper()
        if char not in cnt.keys():
            cnt[char] = 1
        else:
            cnt[char] += 1
    print(most_often(cnt))

    return
def most_often(cnt: dict):
    max_v = 0
    key = None
    for k, v in cnt.items():
        if v > max_v:
            max_v = v
            key = k
        elif v == max_v:
            key = '?'
    return key    
    
if __name__ == '__main__':
    main()