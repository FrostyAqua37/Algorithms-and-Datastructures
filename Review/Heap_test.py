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
    values = [100, 80, 0, 10, 30, 60, 70, 20, 90, 50, 40]
    length = len(values)

    for i in range(int(length / 2) - 1, -1, -1):
        heapify(values, length, i)
    print("Min Heap:", end=" ")
    printList(values)

    heapSort(values, length)
    print("List in Descending Sorted Order:", end=" ")
    printList(values)