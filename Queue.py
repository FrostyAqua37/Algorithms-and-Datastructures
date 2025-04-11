class Queue(object):
     
    def __init__(self, size):  
        self.__maxSize = size
        self.__que = [None] * size
        self.__front = 1
        self.__rear = 0
        self.__nItems = 0

    def insert(self, item):
        if self.isFull():
            raise Exception("Queue is full!")
        self.__rear += 1

        if self.__rear == self.__maxSize:
            self.__rear = 0
        self.__que[self.__rear] = item
        self.__nItems += 1
        return f"Item {self.__que[self.__rear]} successfully inserted at index {self.__rear}"
        

    def remove(self):
        if self.isEmpty():
            raise Exception("Queue is Empty!")
        front = self.__que[self.__front]
        self.__que[self.__front] = None
        self.__front += 1

        if self.__front == self.__maxSize:
            self.__front = 0
        self.__nItems -= 1
        return f"Item {front} at index {self.__front} have been removed."

    def peek(self):
        return None if self.isEmpty() else self.__que[self.__front]
    
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
            j = i + self.__front
            if j >= self.__maxSize:
                j -= self.__maxSize
            output += str(self.__que[j])
        
        output += "]"
        return output

que = Queue(10)

for i in range(10):
    i += 1
    que.insert(i)

print(que.__str__())
print(f"Size of Queue: {que.__len__()}")
print(f"First element: {que.peek()}")

print(f"Is the Queue Full? \n {que.isFull()}")
print(f"Is the Queue Empty? \n {que.isEmpty()}")