def insertionSort(list):
    length = len(list) #Length of List

    for outer in range(1, length):  #Iterates the List from index 1 to final index position.
        temp = list[outer]          #Copies the current marked element to a temporarily variable. 
        inner = outer               #Sets inner variable to the Outer Variable. 
        while inner > 0 and temp < list[inner - 1]: #Checks if inner is greater than 0 and current element is less than the previout index position.
            list[inner] = list[inner - 1]           #Overwrites the current unsorted element with the previous element.
            inner -= 1                              #Decrease the inner i.e index with -1 in each loop.
        list[inner] = temp                          #Replaces unsorted element in its temporary sorted position. 
    return list                                     #Returns the sorted list


numbers = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
fruits = ["Mango", "Dragonfruit", "Banana", "Kiwi", "Papaya", "Apple", "Pineapple", "Watermelon"]

print(insertionSort(fruits))
    
"""
The Insertion Sort Algorithm have a time complexity of O(n^2), since it is implemented with a nested loop.
The outer loop executes N amount of times, and the inner loop executes N amount of times for each iteration of the outer loop.
N in this case is the length of the list.
Furthermore, the number of comparisons done grows proportionally to the number of iterations done. 
For example, on the 1st iteration a maximum of 1 comparison is done, on the 2nd iteration 2 comparison is done, 
and on the last iteration, N comparisons is done. 
"""