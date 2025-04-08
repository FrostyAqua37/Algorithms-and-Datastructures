import Array
max_size = 10
arr = Array.Array(max_size)

arr.insert(77)
arr.insert(99)
arr.insert(44)
arr.insert(100.40)
arr.insert(0)
arr.insert(-17)
arr.insert(200)
arr.insert(200)
arr.insert("foo")
arr.insert("zoo")

print("Original Array:", arr.traverse(), "\n" + f"Length of array: {len(arr)}")

print("Array with no Duplicates:", arr.removeDupes())