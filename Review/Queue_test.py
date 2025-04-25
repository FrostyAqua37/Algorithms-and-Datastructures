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
        return f"Item {data} have been inserted at index position {self.__rear}"

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty!")
        index = self.__front
        data = self.__queue[self.__front]
        self.__queue[self.__front] = None
        self.__front += 1

        if self.__front == self.__maxSize:
            self.__front = 0
        self.__nItems -= 1
        return f"Item {data} have been removed index position {index}"

    def __len__(self):
        return self.__nItems

    def peek(self):
        return None if self.isEmpty() else self.__queue[self.__front]

    def __str__(self):
        output = "["
        for i in range(self.__nItems):
            if len(output) > 1:
                output += ", "
            j = i + self.__front
            if j >= self.__maxSize:
                j -= self.__maxSize
            output += str(self.__queue[j])
        return output + "]"

    def isEmpty(self):
        return self.__nItems == 0

    def isFull(self):
        return self.__nItems > self.__maxSize
    