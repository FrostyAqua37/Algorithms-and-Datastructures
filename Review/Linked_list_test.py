#Methods for Node Class: __init__(), getNext(), setNext(), getData(), setData(), __str__(), isLast()
#Methods for Linked List Class: __init__(), getFirst(), setFirst(), getNext(), setNext(), first(), isEmpty(), traverse(), __len__(), __str__(), insert(), find(), search(), insertAfter(), deleteFirst(), delete()

class Node(object):
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    def getNext(self):
        return self.__next
    
    def setNext(self, node):
        if node is None or isinstance(node, Node):
            self.__data = node
        else:
            raise Exception("Node need to be 'None' or of type class 'Node'.")
        
    def getData(self):
        return self.__data
    
    def setData(self, data):
        self.__data = data

    def __str__(self):
        return str(self.getData())
    
    def isLast(self):
        return self.__next is None

class LinkedList(object):
    def __init__(self):
        self.__first = None

    def getFirst(self):
        return self.__first
    
    def setFirst(self, node):
        if node is None or isinstance(node, Node):
            self.__first = node
        else:
            raise Exception("Node need to be 'None' or of type class 'Node'.")
    
    def getNext(self):
        return self.getFirst()
    
    def setNext(self, node):
        return self.setFirst(node)
    
    def first(self):
        if self.isEmpty():
            raise Exception("Linked List is currently Empty.")
        return self.getFirst().getData()

    def isEmpty(self):
        return self.__first is None
    
    def traverse(self):
        output = ""
        node = self.getFirst()
        while node is not None:
            output += f"[{str(node.getData())}]"
            if node.getNext() is None:
                break
            output += " > "
            node = node.getNext()
        print(output)
        return 

    def __str__(self):
        output = ""
        node = self.getFirst()
        while node is not None:
            output += f"[{str(node.getData())}]"
            if node.getNext() is None:
                break
            output += " --> "
            node = node.getNext()
        return output 

    def __len__(self):
        length = 0
        node = self.getFirst()
        while node is not None:
            length += 1
            node = node.getNext()
        return length
    
    def insert(self, data):
        node = Node(data, self.getNext())
        self.setFirst(node)
        print(f"Data item {node} have been successfully inserted.")

    def find(self, goal):
        node = self.getFirst()
        while node is not None:
            if node.getData() == goal:
                return node
            node = node.getNext()
        raise Exception("No matching node found.")

    def search(self, goal):
        node = self.find(goal)
        if node is not None:
            return node.getData()

    def insertAfter(self, goal, data):
        node = self.find(goal)
        if node is None:
            return False
        new_node = Node(data, node.getNext())
        node.setNext(new_node)
        print(f"Data item ({data}) successfully inserted after node ({node.getData()})")
        return

    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("Linked List is currently Empty.")
        
        first = self.getFirst()
        self.setFirst(first.getNext())
        first.setNext(None)
        print("Successfully removed the first Node.")
        return

    def delete(self, goal):
        if self.isEmpty():
            raise Exception("Linked List is currently Empty.")
        
        previous = self
        while previous.getNext() is not None:
            node = previous.getNext()
            if goal == node.getData():
                previous.setNext(node.getNext())
                print(f"Node ({node}) have been successfully removed from the Linked List.")
                return 
            previous = node
        raise Exception("No Matching Node found.")


linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)

linked_list.traverse()