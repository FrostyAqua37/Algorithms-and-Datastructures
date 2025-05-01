#Methods for the Queue Class: __init__(), enqueue(), dequeue(), peek(), __len__(), __str__(), isFull(), isEmpty()
class Queue(object):
    def __init__(self, size):
        self.__queue = [None] * size
        self.__maxSize = size
        self.__front = 1
        self.__rear = 0
        self.__nItems = 0

    def enqueue(self, data):
        if self.isFull():
            raise Exception("Queue is Full!")
        self.__rear += 1

        if self.__rear == self.__maxSize:
            self.__rear = 0
        self.__queue[self.__rear] = data
        self.__nItems += 1
        print(f"Item {data} have been inserted at index position {self.__rear}.")
        return 
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty!")
        item = self.__queue[self.__front]
        index = self.__front

        self.__queue[self.__front] = None
        self.__front += 1
        if self.__front == self.__maxSize:
            self.__front = 0
        self.__nItems -= 1

        print(f"Item {item} have been removed from index position {index}.")
        return

    def peek(self):
        return None if self.isEmpty() else self.__queue[self.__front]
    
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
            output += str(self.__queue[j])
        print(output + "]")
        return 

    def isFull(self):
        return self.__nItems == self.__maxSize
    
    def isEmpty(self):
        return self.__nItems == 0
    
queue = Queue(20)

for i in range(20):
    i += 1
    queue.enqueue(i)

queue.__str__()
print(queue.__len__())
queue.dequeue()
print(queue.peek())