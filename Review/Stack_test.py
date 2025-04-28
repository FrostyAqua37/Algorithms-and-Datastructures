#Methods for Stack Class: __init__(), push(), pop(), peek(), isEmpty(), isFull(), __len__(), __str__()

class Stack(object):
    def __init__(self, size):
        self.__stack = [None] * size
        self.__maxSize = size
        self.__top = -1
        self.__nItems = 0
    
    def push(self, data):
        if self.isFull(self):
            raise Exception("Stack is Full.")
        self.__top += 1
        self.__stack[self.__top] = data
        self.__nItems += 1
        print(f"Data value {data} have been push to position {self.__top}.")
        return 
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        data = self.__stack[self.__top]
        self.__stack[self.__top] = None
        self.__top -= 1
        self.__nItems -= 1
        print(f"Data value {data} have been removed.")
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
        if self.isEmpty():
            raise Exception("Stack is Empty.")
        output = "["
        for i in range(self.__nItems):
            if len(output) > 1:
                output += ", "
            output += str(self.__stack[i])
        return output + "]"
#stack = Stack(10)
#
#for i in range(10):
#    stack.push(i)
#
#print(stack.__str__())
