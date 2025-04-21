class Node(object):
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next
    
    def setData(self, data):
        self.__data = data

    def getData(self):
        return self.__data
    
    def setNext(self, node):
        if node is None or isinstance(node, Node):
            self.__next = node
        else:
            raise Exception("Node needs to be None or a type of the Node Class.")

    def getNext(self):   
        return self.__next     
    
    def isLast(self):
        return self.__next is None
    
    def __str__(self):
        return str(self.getData())
    
class LinkedList(object):
    def __init__(self):
        self.__first = None

    def getFirst(self):
        return self.__first

    def setFirst(self, node):
        if node is None or isinstance(node, Node):
            self.__first = node 
        else:
            raise Exception("Node needs to be None or a type of the Node Class.")

    def getNext(self):
        return self.getFirst()

    def setNext(self, node):
        return self.setFirst(node)

    def first(self):
        if self.isEmpty():
            raise Exception("No Nodes currently in Linked List.")
        return self.getFirst().getData()

    def isEmpty(self):
        return self.getFirst is None 
    
    def traverse(self):
        output = "["
        node = self.getFirst()

        while node is not None:
            if len(output) > 1:
                output += " > "
            output += node.getData()
            node = node.getNext()
        return output + "]"
    
    def __len__(self):
        length = 0
        node = self.getFirst()

        while node is not None:
            length += 1
            node = node.getNext()
        return length
    
    def __str__(self):
        output = "["
        node = self.getFirst()

        while node is not None:
            if len(output) > 1:
                output += ", "

            output += str(node)
            node = node.getNext()
        return output + "]"
    
    def insert(self, data):
        node = Node(data, self.getFirst())
        self.setFirst(node)

    def find(self, goal):
        node = self.getFirst()

        while node is not None:
            if node.getData() == goal:
                return node
            node = node.getNext()

    def search(self, goal):
        node = self.find(goal)
        if node is not None:
            return node.getData()
        else:
            return "No element found."

    def insertAfter(self, goal, data):
        node = self.find(goal)
        if node is None:
            return False
        
        new_node = Node(data, self.getNext())
        node.setNext(new_node)   
        return True     
