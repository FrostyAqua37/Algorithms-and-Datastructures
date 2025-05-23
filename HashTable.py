#Methods for Node class: __init__()
#Methods for HashTable class: __init__(), _hash(), insert(), search(), delete() and 


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
class HashTable(object):
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__size = 0
        self.__table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.__capacity
    
    def insert(self, key, value):
        index = self._hash(key)
        if self.__table[index] is None:
            self.__table[index] = Node(key, value)
            self.__size += 1
        else:
            current = self.__table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return 
                current = current.next
            
            new_node = Node(key, value)
            new_node.next = self.__table[index]
            self.__table[index] = new_node
            self.__size += 1

    def search(self, key):
        index = self._hash(key)
        current = self.__table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)
        previous = None
        current = self.__table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:      
                    self.__table[index] = current.next
                current.key, current.value = None, None 
                self.__size -= 1
                return 
            
            previous = current
            current = current.next
        raise KeyError("No Matching Key Found.")
    

def word_frequency(word_list):
    ht = HashTable(50)
    for word in word_list:
        word = word.lower()
        count = ht.search(word)

        if count is None:
            ht.insert(word, 1)
        else:
            ht.insert(word, count + 1)
    return ht

words = ["apple", "banana", "Apple", "orange", "banana", "banana"]
hash_table = word_frequency(words)

# Print the frequencies
print("Word Frequencies:")

for word in set(w.lower() for w in words):
    print(f"{word}: {hash_table.search(word)}")