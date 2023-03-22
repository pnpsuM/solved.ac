import sys
from collections import deque

loc, hide = tuple(map(int, sys.stdin.readline().split()))
time = 0
graph = {}
visited = []

def f(loc):
    loc += 1
    return loc

def b(loc):
    loc -= 1
    return loc

def t(loc):
    loc *= 2
    return loc

def node(loc):
    flag = loc >= 0 and loc <= 100000
    if loc < hide * 2 and loc not in graph.keys() and flag:
        graph[loc] = [t(loc), f(loc), b(loc)]
        node(t(loc))
        node(f(loc))
        node(b(loc))
        
def seek(loc, hide, cnt):
    q = deque()
    q.append(loc)
    cnt += 1
    visited.append(loc)
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

node(loc)
print(graph)
cnt = 0
print(seek(loc, hide, cnt))