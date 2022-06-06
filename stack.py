class StackTopn:

    def __init__(self):
        self.items = []

    def __str__(self):
        return ' '.join([str(i) for i in self.items])

    def isEmpty(self):
        return self.items == []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()#
    def peek(self):
        return self.items[len(self.items)-1]
    def length(self):
        return f"stacked items => {len(self.items)}"
    def display_all_items(self):
        return [str(i) for i in self.items]

class StackTop0:

    def __init__(self):
        self.items = []

    def __str__(self):
        return ' '.join([str(i) for i in self.items])

    def isEmpty(self):
        return self.items == []
    def push(self, item):
        return self.items.insert(0, item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def length(self):
        return f"stacked items => {len(self.items)}"
    def display_all_items(self):
        return [str(i) for i in self.items]

f = StackTopn()

f.push('FIRST')
f.push('SECOND')
f.push('THIRD')
f.push('FOURTH')

print(f.pop())

print(f.display_all_items())

print(f.length())
print(f.peek())
print(f.isEmpty())