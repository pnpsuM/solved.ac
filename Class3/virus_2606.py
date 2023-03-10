import sys

num_com = int(sys.stdin.readline())
num_lines = int(sys.stdin.readline())

graph = {}
visit = {}

def search(index, cnt):
    if index not in graph.keys():
        return cnt
    else:
        visit[index] = True
        for i in graph[index]:
            if i not in visit.keys():
                cnt += 1
                cnt = search(i, cnt)
        return cnt
    
for line in range(num_lines):
    head, tail = list(map(int, sys.stdin.readline().split()))
    if head in graph.keys():
        graph[head].append(tail)
    else:
        graph[head] = []
        graph[head].append(tail)
    if tail in graph.keys():
        graph[tail].append(head)
    else:
        graph[tail] = []
        graph[tail].append(head)
        
cnt = 0
print(search(1, cnt))