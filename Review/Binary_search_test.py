def binarySearch(array, item):
    nItems = len(array)
    low = 0
    high = nItems - 1
    iteration = 0

    while low <= high:
        middle = (low + high) // 2
        iteration += 1

        if array[middle] == item:
            return f"Item {item} found at index position {middle}.\nNumber of Iterations: {iteration}"
        elif array[middle] < item:
            low = middle + 1
        else:
            high = middle - 1
    return "Item not found."


numbers = []

for i in range(10):
    i += 1 
    numbers.append(i)

print(numbers)
print("Result:", binarySearch(numbers, 10))

"""The Binary Search algorithm implemented have a time complexity of O(log n), since the range of elements for the algorithm 
to search between is divided in half with each iteration. Inserting the length of the array i.e n in the O(log n), like O(log 10), 
the maximum of steps is calculated which is 4 steps."""

        