def average_value(array):
    total = 0
    sum = 0
    for i in array:
        sum += i
        total += 1
    return sum, total
    
def main():
    arr = [1, 2, 3, 4, 5]
    result = average_value(arr)
    average = result[0] / result[1]

    print(f"Average: {average}")
    print(f"Sum of all the numbers: {result[0]}")
    print(f"Total number of elements: {result[1]}")
    print(f"Average is then {result[0]} / {result[1]} = {int(average)}")

main()