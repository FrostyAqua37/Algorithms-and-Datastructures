class BinarySearch(object):
    def __init__(self, array):
        self.__nItems = len(array)
        self.__array = array

    def find(self, item):
        low = 0
        high = self.__nItems - 1
        steps = 0
        list = ""
    
        while low <= high:
            middle = (low + high) // 2
            steps += 1

            if self.__array[middle] == item:
                return f"Item ({item}) found at index position {middle}.\nNumber of steps: {steps}"
            elif self.__array[middle] < item:
                low = middle + 1
            else:
                high = middle - 1
        return "No matching item found."
    
array = []
for i in range (50):
    i += 1
    array.append(i)

print(array)
binary = BinarySearch(array)
print(binary.find(5))

"""The time complexity of the binary search algorithm implemented is of O(log n), because with each iteration, 
the range of elements to between is divided in half. So given that the range of the array at the start is 1 to 50, 
after the first iteration, the range is shortened to 1 to 25, since the target element is less than 50. 
Then it shortens to 1 to 12 (12.5), then 1 to 6, then 4 to 6, then 4 to 5, then finally finds the target element at 4.
The number of steps i.e iterations is 5, which is the same number as putting 50 as n in O(log n)"""


