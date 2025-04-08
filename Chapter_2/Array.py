class Array(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

    def __len__(self):
        return self.__nItems
    
    def get(self, n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]
        
    def set(self, n, value):
        if 0 <= n and n < self.__nItems:
            self.__a[n] = value
    
    def insert(self, value):
        self.__a[self.__nItems] = value
        self.__nItems += 1

    def find(self, value):
        for i in range(self.__nItems):
            if self.__a[i] == value:
                return i 
        return "Value does not exist in array"
    
    def search(self, value):
        return self.get(self.find(value))

    def delete(self, value):
        for i in range(self.__nItems):
            if self.__a[i] == value:
                self.__nItems -= 1
                for j in range(i, self.__nItems):
                    self.__a[j] = self.__a[j+1]
                return True

    def traverse(self):
        output = "["
        for i in range(self.__nItems):
            if len(output) > 1:
                output += ", "
            output += str(self.__a[i])
        output += "]"
        return output
            

    def getMaxNum(self, highest_number=None):
        if self.__nItems == 0:
            return "Array is empty."

        if isinstance(self.__a[0], (int, float)):
            highest_number = self.__a[0]

        for i in range(self.__nItems):
            if isinstance(self.__a[i], (int, float)):
                if self.__a[i] > highest_number:
                    highest_number = self.__a[i]

        if highest_number == None:
            return "Array contains no numbers"

        return highest_number
    
    def deleteMaxNum(self):
        highest_number = self.getMaxNum()

        if isinstance(highest_number, (int, float)):
            self.delete(highest_number)
            return "Highest Number have been removed."
        return highest_number
    
    def removeDupes(self):
        no_duplicate = []
        for i in range(self.__nItems):
            if self.__a.count(self.__a[i]) > 1:
                continue
            else:
                no_duplicate.append(self.__a[i])
        return no_duplicate
