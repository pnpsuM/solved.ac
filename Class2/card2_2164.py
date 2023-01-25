from collections import deque

N = int(input())
deck = deque()
for i in range(1, N+1):
    deck.appendleft(i)
for i in range(1, N):
    deck.pop()
    deck.appendleft(deck.pop())
print(deck[0])