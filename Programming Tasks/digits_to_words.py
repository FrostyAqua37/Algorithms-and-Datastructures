def digit_to_word(number):
    match number:
        case "0":
            print("Zero")
        case "1":
            print("One")
        case "2":
            print("Two")
        case "3": 
            print("Three")
        case "4":
            print("Four")
        case "5":
            print("Five")
        case "6":
            print("Six")
        case "7": 
            print("Seven")
        case "8":
            print("Eight")
        case "9": 
            print("Nine")

def print_word(n):
    i = 0
    length = len(n)

    while i < length:
        digit_to_word(N[i])
        i += 1

N = "1234"
print_word(N)