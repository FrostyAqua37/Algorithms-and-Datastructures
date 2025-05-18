#Methods for Node Class: __init__(), getNext(), setNext(), getData(), setData(), __str__(), isLast()
#Methods for Linked List Class: __init__(), getFirst(), setFirst(), getNext(), setNext(), first(), isEmpty(), traverse(),
#  __len__(), __str__(), insert(), find(), search(), insertAfter(), deleteFirst(), delete()

class Node(object):
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next
    
    def getNext(self):
        return self.__next
    
    def setNext(self, node):
        if node is None or isinstance(node, Node):
            self.__next = node
        else:
            raise Exception("Node needs to be 'None' or of type 'Node'.")
        
    def getData(self):
        return self.__data
    
    def setData(self, data):
        self.__data = data

    def __str__(self):
        return str(self.getData)
    
    def isLast(self):
        return self.getNext() is None

class LinkedList(object):
    def __init__(self):
        self.__first = None
    
    def getFirst(self):
        return self.__first
    
    def setFirst(self, node):
        if node is None or isinstance(node, Node):
            self.__first = node
        else:
            raise Exception("Node needs to be 'None' or of type 'Node'.")

    def getNext(self):
        return self.__first

    def setNext(self, node):
        return self.setFirst(node)
    
    def first(self):
        if self.isEmpty():
            raise Exception("Linked List is Empty.")
        return self.getFirst().getData()
    
    def isEmpty(self):
        return self.getFirst() is None
    
    def traverse(self):
        node = self.getFirst()
        output = ""

        while node is not None:
            output += f"[{str(node.getData())}]"
            if node.getNext() is None:
                break
            output += " > "
            node = node.getNext()
        print(output)
        return 

    def __len__(self):
        length = 0
        node = self.getFirst()

        while node is not None:
            length += 1
            node = node.getNext()
        return length

    def __str__(self):
        node = self.getFirst()
        output = "[" 

        while node is not None:
            if len(output) > 1:
                output += ", "
            output += str(node.getData())
            node = node.getNext()
        return output + "]"
    
    def insert(self, data):
        first = Node(data, self.getFirst())
        self.setFirst(first)

    def find(self, goal):
        node = self.getFirst()
        while node is not None:
            if node.getData() == goal:
                return node
            node = node.getNext()
        raise Exception("No Matching data value found.")

    def search(self, goal):
        node = self.find(goal)
        if node is not None:
            return node.getData()
    
    def insertAfter(self, position, data):
        node = self.find(position)
        if node is None:
            return False
        
        new_node = Node(data, node.getNext())
        node.setNext(new_node)
        return True
    
    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("Linked List is Empty.")
        
        first = self.getFirst()
        self.setFirst(first.getNext())
        first.setNext(None)
        print("First Node have been successfully deleted.")
        return 
    
    def delete(self, position):
        if self.isEmpty():
            raise Exception("Linked List is Empty.")

        previous = self
        while previous.getNext() is not None:
            node = previous.getNext()
            if position == node.getData():
                previous.setNext(node.getNext())
                node.setNext(None)
                return 
            previous = node
        raise Exception("No matching data value found.")
    
linked_list = LinkedList()
number = 100

for i in range(11):
    linked_list.insert(number)
    number -= 10

print("Linked List:")
linked_list.traverse()


