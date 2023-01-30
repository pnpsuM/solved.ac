import sys

# hash map
num_cards = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
    
num_target = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

map_ = {}
for card in cards:
    if card in map_:
        map_[card] += 1
    else:
        map_[card] = 1
        
for target in targets:
    if target in map_:
        print(map_[target], end=' ')
    else:
        print('0', end=' ')