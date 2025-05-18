#Methods for Heap: parent(), leftChild(), rightChild(), heapify(), heapSort(), insertMinHeap()


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

def min_heap(minheap, data):
    minHeap.append(data)
    i = len(minHeap) - 1

    while i > 0 and minheap[parent(i)] > minHeap[i]:
        minHeap[i], minHeap[parent(i)] = minHeap[parent(i)], minHeap[i] 
        i = parent(i)


    
if __name__ == "__main__":
    values = [10, 0, 30, 40, 100, 50, 70, 90, 80, 20, 60]
    minHeap = []
    length = len(values)
    
    for value in values:
        min_heap(minHeap, value)
    print("Min Heap:", minHeap)

    heapSort(values, length)
    print("List in Descending Order:", values)