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
    
def identity(x):
    return x
    
class LinkedList(object):
    def __init__(self):
        self.__first = None

    def getFirst(self):
        return self.__first
    
    def setFirst(self, node):
        if node is None or isinstance(node, Node):
            self.__first = node
        else:
            raise Exception("Node needs to be 'None' or of type 'Node'")
        
    def getNext(self):
        return self.getFirst()
    
    def setNext(self, node):
        return self.setFirst(node)
    
    def first(self):
        if self.isEmpty():
            raise Exception("No items currently in the Linked List.")
        return self.getFirst().getData()

    def isEmpty(self):
        return self.getFirst() is None
    
    def traverse(self, func=print):
        output = "["
        node = self.getFirst()
        while node is not None:
            if len(output) > 1:
               output += ", " 
            output += node.getData()
            node = node.getNext()
        func(output + "]")
    
    def __len__(self):
        l = 0
        node = self.getFirst()
        while node is not None:
            l += 1
            node = node.getNext()
        return l
    
    def __str__(self):
        output = "["
        node = self.getFirst()
        while node is not None:
            if len(output) > 1:
                output += " > "
            output += str(node)
            node = node.getNext()
        return output + "]"           

    def insert(self, data):
        node = Node(data, self.getFirst())
        self.setFirst(node)
    
    def find(self, goal, key=identity):
        node = self.getFirst()
        while node is not None:
            if key(node.getData()) == goal:
                return node
            node = node.getNext()

    def search(self, goal, key=identity):
        node = self.find(goal, key)
        if node is not None:
            return node.getData()

    def insertAfter(self, goal, data, key=identity):
        node = self.find(goal, key)
        if node is None:
            return False
        new_node = Node(data, node.getNext())
        node.setNext(new_node)
        return True
    
    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("No nodes in the Linked List currently.")
        
        first = self.getFirst()
        self.setFirst(first.getNext())
        return first.getData()
    
    def delete(self, goal, key=identity):
        if self.isEmpty(self):
            raise Exception("No nodes in the Linked List currently.")
        
        previous = self
        while previous.getNext() is not None:
            node = previous.getNext()
            if goal == key(node.getData()):
                previous.setNext(node.getNext())
                return previous.getData()
            previous = node
            
        raise Exception("No items matching the key have been found.")


llist = LinkedList()

llist.insert("A")
llist.insert("B")
llist.insert("C")

print(llist.__str__())