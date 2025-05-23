class MergeSort(object):
    def __init__(self, list):
        self.__list = list
        length = len(list)
        self.__work = [None] * length
        self.mergeSort(0, length)

    def mergeSort(self, low, high):
        if low + 1 >= high:
            return 

        middle = (low + high) // 2
        self.mergeSort(low, middle)
        self.mergeSort(middle, high)
        self.merge(low, middle, high)

    def merge(self, low, middle, high):
        n = 0
        indexLow = low
        indexHigh = middle

        while (indexLow < middle and indexHigh < high):
            itemLow = self.__list[indexLow]
            itemHigh = self.__list[indexHigh]
        
            if itemLow <= itemHigh:
                self.__work[n] = itemLow
                indexLow += 1
            else:
                self.__work[n] = itemHigh
                indexHigh += 1
            n += 1
        
        while indexLow < middle:
            self.__work[n] = self.__list[indexLow]
            indexLow += 1
            n += 1

        while n > 0:
            n -= 1
            self.__list[low + n] = self.__work[n]


values = [90, 10, 0, 30, 60, 20, 70, 80, 50, 40, 100]

print(f"Initial List: {values}")
print("Number of values:", len(values))

MergeSort(values)

print(f"Sorted List with Mergesort: {values}")


"""
The Time complexity of the Mergesort algorithm implemented above is O(n log n). 
"""