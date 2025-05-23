#Methods for Heap: parent(), leftChild(), rightChild(), heapify(), heapSort()
def parent(i):
    return (i - 1) // 2

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
        list[0], list[i] = list[i], list[0]
        heapify(list, i, 0)

def printList(list):
    print(list)


if __name__ == "__main__":
    values = [10, 0, 30, 40, 100, 50, 70, 90, 80, 20, 60]
    length = len(values)

    for i in range(int(length / 2) - 1, -1, -1):
        heapify(values, length, i)
    
    print("Min Heap:", end=" ")
    printList(values)

    heapSort(values, length)
    print("List in Descending Order:", end=" ")
    printList(values)

"""
The Methods parent(), leftChild(), rightChild() and print() have an time complexity of O(1), since the operations is not affected
by how big the input size is. The heapify() method is O(log n) time complexity, since the height of the heap is O(log n).
In the HeapSort() method, the first loop takes O(n), since making a min heap from a unsorted list in this way is O(n), although
the heapify method is only O(log n) in worst case. The 2nd loop takes O(n) for iterating through, and the heapify takes 
O(log n) time complexity, meaning it the time complexity for the method is O(n log n), 
by applying the rules of prioritizing higher order terms in Big O Notation. 

Taking every time complexity in to account, the overall time complexity of the program is O(n log n), which is one of the 
algorithms with slow efficiency and faster growth rate. Building the min heap takes O(n), while extracting and sorting values 
take O(n log n)
"""