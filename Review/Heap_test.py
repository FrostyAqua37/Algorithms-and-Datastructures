#Methods for Heap: parent(), leftChild(), rightChild(), heapify(), heapSort()
def parent(i):
    return (i + 1) // 2

def leftChild(i):
    return i * 2 + 1

def rightChild(i):
    return i * 2 + 2

def heapify(list, length, i):
    smallest = i
    left = leftChild(i)
    right = rightChild(i)

    if left < length and list[left] < list[smallest]:
        smallest = left

    if right < length and list[right] < list[smallest]:
        smallest = right

    if smallest != i:
        list[i], list[smallest] = list[smallest], list[i]
        heapify(list, length, smallest)

def heapSort(list, length):
    for i in range(int(length / 2) - 1, -1, -1):
        heapify(list, length, i)
    
    for i in range(length - 1, -1, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)

def printList(list):
    print(list)
    
values = [90, 40, 60, 10, 30, 0, 20, 100, 70, 50, 80]
length = len(values)

for i in range(int(length / 2) - 1, -1, -1):
    heapify(values, length, i)

print("Min Heap:", end=" ")
printList(values)

heapSort(values, length)
print("List in descending order:", end=" ")
printList(values)


"""
The Methods parent(), leftChild() and rightChild() have a time complexity of O(1), since their operation is not dependent on the input size.
The Heapify() method have a time complexity of O(log n), since the a height of a heap is O(log n).
The first loop of the heapSort() method is O(n), since making a min heap from a unsorted list takes O(n) time and it iterates through the list, 
even although the heapify method is only O(log n).
The second loop of the method() iterates through the list starting at the end, thus having a time of O(n) complexity.

Taking all these time complexities into account, the overall time complexity of this heap program is O(n log n) by applying the rules of Big O Notation.
"""