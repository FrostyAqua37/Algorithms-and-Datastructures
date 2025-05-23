#Methods for Mergesort: __init__(), mergesort(), merge()
class Mergesort(object):
    def __init__(self, list):
        self.__list = list
        length = len(list)
        self.__work = [None] * length
        self.mergesort(0, length)
    
    def mergesort(self, low, high):
        if low + 1 >= high:
            return 
        
        middle = (low + high) // 2
        self.mergesort(low, middle)
        self.mergesort(middle, high)
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
        
values = [100, 90, 60, 70, 20, 30, 50, 10, 0, 40, 80]
print("Unsorted List:", values)
print("Number of items:", len(values))

Mergesort(values)

print("Sorted List with Mergesort:", values)

"""
In the Mergesort algorithm, finding the middle point and splitting the list takes O(1) time complexity, 
but recursively splitting the lists at each level, the total number of levels is O(log n). 
The merge method performed on each level have a time complexity of O(n), since it compares and copies every element 
across the different lists. Since the levels of the mergesort is O(log n), and merging element on each level takes O(n),
makes the overall time complexity of the mergesort algorithm O(n log n) for best, average and worst cases. 
"""