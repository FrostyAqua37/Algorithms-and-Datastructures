class Node(object):
    def __init__(self, data, next=None):
        self.__next = next
        self.__data = data

    def getData(self):
        return self.__data
    
    def setData(self, data):
        self.__data = data
        
    def getNext(self):
        return self.__next

    def setNext(self, node):
        if node is None or isinstance(node, Node):
            self.__next = node
        else:
            raise Exception("Next node must be a type of Node or None")
        
    def isLast(self):
        return self.__next is None
    
    def __str__(self):
        return str(self.getData())
    
class LinkedList(object):
    def __init__(self):
        self.__first = None

    def isEmpty(self):
        return self.__first == None
    
node = Node(10)
print("[" + node.__str__() + "]")