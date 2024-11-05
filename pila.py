class Stack:
    
    def __init__(self):
        self.elements =[]

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.elements) > 0:
            return self.elements[-1]
        else:
            return None

    def size(self):
        return len(self.elements)