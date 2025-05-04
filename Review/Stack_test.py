#Methods for Stack Class: __init__(), push(), pop(), peek(), isEmpty(), isFull(), __len__(), __str__()

class Stack(object):
    def __init__(self, size):
        self.__stack = [None] * size
        self.__maxSize = size
        self.__top = -1
        self.__nItems = 0

    def push(self, data):
        if self.isFull():
            raise Exception("Stack is Full.")
        
        self.__top += 1
        self.__stack[self.__top] = data
        self.__nItems += 1
        print(f"Data item {data} have been successfully inserted at index position {self.__top}")
        return 
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty.")
        
        item = self.__stack[self.__top]
        index = self.__top
        self.__stack[self.__top] = None
        self.__top -= 1
        self.__nItems -= 1
        print(f"Data Item ({item}) have been successfully remove from index postion {index}.")
        return 

    def peek(self):
        return "Stack is Empty" if self.isEmpty() else self.__stack[self.__top]

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
    

#stack = Stack(10)
#
#for i in range(10):
#    stack.push(i)
#
#print(stack.__str__())
