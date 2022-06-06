#Creating a stack

class StackTopn:

    def __init__(self):
        self.items = []

    def __str__(self):
        return ' '.join([str(i) for i in self.items])

    # to check whether stack is item
    def isEmpty(self):
        return self.items == []

    # adding items to the stack
    def push(self, item):
        return self.items.append(item)
    
    #removing items from the stack
    def pop(self):
        return self.items.pop()

    # check the last added items in the stacks
    def peek(self):
        return self.items[len(self.items)-1]

    # check number of items in stack
    def length(self):
        return f"stacked items => {len(self.items)}"

    # display the items in the stack
    def display_all_items(self):
        return [str(i) for i in self.items]


# implementing stack flow reversed
class StackTop0:

    def __init__(self):
        self.items = []

    def __str__(self):
        return ' '.join([str(i) for i in self.items])

    # to check whether stack is item
    def isEmpty(self):
        return self.items == []

    # adding items to the stack
    def push(self, item):
        return self.items.insert(0, item)

    # adding items in a stack
    def pop(self):
        return self.items.pop(0)

    # check the last added items in the stacks
    def peek(self):
        return self.items[0]

    # check number of items in stack 
    def length(self):
        return f"stacked items => {len(self.items)}"

    # display the items in the stack
    def display_all_items(self):
        return [str(i) for i in self.items]

