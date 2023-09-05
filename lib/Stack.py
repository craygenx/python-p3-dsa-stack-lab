class Stack:
    def __init__(self, items=None, capacity=None):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.capacity = capacity

    def push(self, item):
        if self.capacity is None or len(self.items) < self.capacity:
            self.items.append(item)
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        if self.capacity is None:
            return False
        return len(self.items) == self.capacity

    def search(self, target):
        for index, item in enumerate(self.items):
            if item == target:
                return len(self.items) - index - 1
        return -1

