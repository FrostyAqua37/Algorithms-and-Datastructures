class ordered_Array(object):

    def __init__(self, initial_size):
        self.__a = [None] * initial_size
        self.__nItems = 0
    
    def __len__(self):
        return self.__nItems

    def get(self, n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]
        raise IndexError("Index", str(n), "is out of range.")

    def traverse(self, function=print):
        for i in range(self.__nItems):
            function(self.__a[i])
        
    def __str__(self):
        ... 
    


    def find (self, item):
        low = 0 
        high = self.__nItems - 1

        while low <= high:
            middle = (low + high) // 2 #Find middle Index by adding both low and high pointers then dividing them into two.

            if self.__a[middle] == item: #Check is middle index is equal to the item searched for.
                return middle
            elif self.__a[middle] < item: #Sets the range to the upper part if the middle index is smaller than the item search for. 
                low = middle + 1
            else: #Automatically sets the range to the lower part of the array as it is the as possible outcome. 
                high = middle - 1
        return low


