from Stack import *

stack = Stack(20)

for letter in ["r", "a", "c", "e", "c", "a", "r"]:
    stack.push(letter)

print(f"Stack: {stack.__str__()}")
print(f"Removing top item in the Stack... \nItem '{stack.pop()}' have been removed.")
print(f"Stack: {stack.__str__()}")

print("Length:", stack.__len__())
print("Top Item:", stack.peek())
print("Full:", stack.isFull())
print("Empty:", stack.isEmpty())

