def binarySearch(list, goal):
    length = len(list)
    low = 0
    high = length - 1

    while low <= high:
        middle = (low + high) // 2

        if list[middle] == goal:
            return (f"Data value {goal} found at Index Position {middle}.") 
        elif list[middle] < goal:
            low = middle + 1
        else:
            high = middle - 1
    return "Item not found."
        
numbers = []
for i in range(20):
    i += 1
    numbers.append(i)

print(f"List: {numbers}")
print(f"Result: {binarySearch(numbers, 201)}")

"""
The Binary Search Algorithm have a time complexity of O(log n), since the range of element being search is divided in half
with each iteration done. For instance the code starts with the range 1 to 20, then divides the searchable range to 10 t0 20,
then 16 to 20, then 19 to 20, then finally finds the element at the last index position 19. 
"""

        