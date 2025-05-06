def insertionSort(array):
    nItems = len(array)
    for outer in range(1, nItems):
        temp = array[outer]
        inner = outer 

        while inner > 0 and temp < array[inner - 1]:
            array[inner] = array[inner - 1]
            inner -= 1
        array[inner] = temp
    return array




list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

fruits = ["Lemon", "Apple", "Mango", "Grape", "Lime", "Melon", "Orange", "Papaya", "Kiwi", "Pineapple", "Lychee", "Guava"]
print(insertionSort(fruits))
#print(f"Numnber of Iteration(s): {iteration()}")

"""The time complexity of the Insertion Sort algorithm is O(n^2), since is have a nested loop, 
which means that the outer loop iterates N amounts of times, while the inner loop also iterates N amount of times for each iteration of the outer loop.
Furthermore, because the list is in descending order, the algorithm performs the maximum amount of steps possible, for the number of comparisons and swaps
increase proportionally to the iterations done. The total number of comparisons and swaps is approximately the same as the number of iterations"""
    