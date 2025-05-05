class InsertionSort(object):
    def insertionSort(self, list):
        self.__a = list
        self.__nitems = len(list)
        self.__iteration = 0
    
        for outer in range(1, self.__nitems):
            self.__iteration += 1
            temp = self.__a[outer]
            inner = outer

            while inner > 0 and temp < self.__a[inner - 1]:
                self.__iteration += 1
                self.__a[inner] = self.__a[inner - 1]
                inner -= 1
            self.__a[inner] = temp
        return self.__a
    
    def iteration(self):
        return self.__iteration

list = [8, 7, 6, 5, 4, 3, 2, 1]

fruits = ["Lemon", "Apple", "Mango", "Grape", "Lime", "Melon", "Orange", "Papaya", "Kiwi", "Pineapple", "Lychee", "Guava"]
sort = InsertionSort()
print(sort.insertionSort(fruits))
print(f"Numnber of Iteration(s): {sort.iteration()}")
    