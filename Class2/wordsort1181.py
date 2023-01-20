import sys
import heapq as h
length = int(sys.stdin.readline().rstrip())

class Words():
    def __init__(self):
        self._word = []
        self.heap = []
    def add_word(self, word):
        self._word.append((len(word), word))
    
    def pop_all(self):
        self._word = set(self._word)
        while(self._word):
            h.heappush(self.heap, self._word.pop())
        while(self.heap):
            print(h.heappop(self.heap)[1])
heap = Words()
for i in range(length):
    heap.add_word(sys.stdin.readline().rstrip())
heap.pop_all()