from collections import deque

class Dequeue:
    def __init__(self) -> None:
        self.queue = deque()
    
    def insert(self, x):
        self.queue.append(x)
    
    def insert_front(self, x):
        self.queue.appendleft(x)
    
    def remove(self):
        self.queue.popleft()
    
    def remove_end(self):
        self.queue.pop()
    
    def peek_front(self):
        return self.queue[0]

    def peek_end(self):
        return self.queue[-1]