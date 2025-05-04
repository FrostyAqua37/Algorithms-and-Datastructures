class InsertionSort(object):

    def insertionSort(self, list): #Sets the list and the length in private instance variables
        self.__a = list
        self.__nItems = len(list)

        for outer in range(1, self.__nItems): #The outer loops which iterates through every element one at a time
            temp = self.__a[outer]
            inner = outer
            while inner > 0 and temp < self.__a[inner - 1]: #Checks if the current element is greater than 0 and the previous element is greater than current element i.e checking for unsorted elements. 
                self.__a[inner] = self.__a[inner - 1] #Sets the current element to be the same value as the previous element 
                inner -= 1 
            self.__a[inner] = temp #Sets the previous element to be temp
        return self.__a #Returns the sorted list
    
list = ["Melon", "Apple", "Orange", "Banana", "Citrus", "Plum", "Mandarin", "Lemon", "Lime", "Grape", "Papaya", "Starfruit", "Kiwi"]

sort = InsertionSort()
print(sort.insertionSort(list))

"""The insertion sort in this program have an time complexity of O(n^2), and is the worst case in this scenario,    
since the list is in decending order. Because it is in descending order, it makes the maximum amount of iterations needed. 
With each iteration, the number of comparison and swaps increase proportionally to the number of iterations. This algorithm 
makes O(10^2) which is approximately 100 comparisons and swaps. """
        