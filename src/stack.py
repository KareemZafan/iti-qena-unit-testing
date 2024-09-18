
class Stack:
    def __init__(self):
        self.items = []

    def push(self,value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()       
    
    def get_size(self):
        return len(self.items)

    def get_current_stack(self):
        return self.items

    def get_peek(self):
        return self.items[-1]   