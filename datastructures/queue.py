from collections import deque

class Queue:
    def __init__(self) -> None:
        self.queue = deque()
    
    def insert(self, x):
        self.queue.append(x)
    
    def remove(self):
        self.queue.popleft()

    def peek(self):
        return self.queue[0]