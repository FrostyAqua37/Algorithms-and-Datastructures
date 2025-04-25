class Stack(object):
    def __init__(self, size):
        self.__stack = [None] * size
        self.__maxSize = size
        self.__top = -1
        self.__nItems = 0

    def push(self, item):
        if self.isFull():
            raise Exception("Stack is Full!")
        self.__top += 1
        self.__nItems += 1

        self.__stack[self.__top] = item

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty!")
        
        top = self.__stack[self.__top]
        self.__stack[self.__top] = None
        self.__top -= 1
        self.__nItems -= 1
        return top
    
    def peek(self):
        if not self.isEmpty():
            return self.__stack[self.__top]

    def __len__(self):
        return self.__nItems

    def isFull(self):
        return self.__nItems == self.__maxSize

    def isEmpty(self):
        return self.__nItems == 0

    def __str__(self):
        output = "["
        for i in range(self.__nItems):
            if len(output) > 1:
                output += ", "

            output += str(self.__stack[i])
        return output + "]"