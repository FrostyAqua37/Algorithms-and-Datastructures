def binarySearch(list, goal):
    low = 0
    high = len(list) - 1

    while low <= high:
        middle = (low + high) // 2

        if list[middle] == goal:
            print(f"Item {goal} found at index position {middle}.")
            return 
        elif list[middle] < goal:
            low = middle + 1
        else:
            high = middle - 1
    raise Exception("No matching value found.")

values = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
            

binarySearch(values, 10)

"""
The Binary Search Algorithm have an time complexity of O(log n), since at each iteration it 
divides the range of element to be searched in half, until it finds the value or runs out of 
elements to divide. For instance, in the code above we want to search for the value 10. 
On the 1st iteration, it divides the range to be from the original range down to 0 to 40, 
since the middle element 50 is greater than 10. 

On the 2nd iteration, it shortens the range down to 0 and 20.
On the 3rd iteration, it find the element we are searching for since it is the middle element
"""
