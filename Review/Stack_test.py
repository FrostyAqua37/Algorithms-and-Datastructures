#Methods for Stack Class: __init__(), push(), pop(), peek(), isEmpty(), isFull(), __len__(), __str__()

class Stack(object):
    def __init__(self, size):
        self.__stack = [None] * size
        self.__maxSize = size
        self.__top = -1
        self.__nItems = 0

    def push(self, item):
        if self.isFull():
            raise Exception("Stack is full.")
        
        self.__top += 1
        self.__stack[self.__top] = item
        self.__nItems += 1
        print(f"Item {item} have been successfully inserted in the Stack.")
        return 
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty.")
        
        item = self.__stack[self.__top]
        self.__stack[self.__top] = None
        self.__top -= 1
        self.__nItems -= 1
        print(f"Item {item} have been successfully removed from the Stack.")
        return 
    
    def peek(self):
        return None if self.isEmpty() else self.__stack[self.__top]
    
    def isEmpty(self):
        return self.__nItems == 0
    
    def isFull(self):
        return self.__nItems == self.__maxSize
    
    def __len__(self):
        return self.__nItems
    
    def __str__(self):
        output = "["
        for i in range(self.__nItems):
            if len(output) > 1:
                output += ", "
            output += str(self.__stack[i])
        return output + "]"
    

stack = Stack(10)

for i in range(10):
    i += 1
    stack.push(i)

print(stack.__str__())
print("Top Item:", stack.peek())
print("Length of Stack:", stack.__len__())
stack.pop()
print("Top Item:", stack.peek())
