class BinarySearch(object):
    def __init__(self, array):
        self.__a = array
        self.__nItems = len(array)

    def binary_search(self, target):
        low = 0
        high = self.__nItems - 1
        iteration = 0

        while low <= high:
            middle = (low + high) // 2
            iteration += 1

            if self.__a[middle] == target:
                return f"Data value ({target}) have been found at index position {middle}.\nNumber of Iterations(s): {iteration}."
            elif self.__a[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        return "No matching item found."

numbers = []

for i in range(50):
    i += 1
    numbers.append(i)

search = BinarySearch(numbers)    
print(search.binary_search(1))   
        