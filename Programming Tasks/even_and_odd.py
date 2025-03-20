arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
even, odd = [], []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

if len(even) == 0:
    print(f"All value are odd {odd}.")
elif len(odd) == 0:
    print(f"All values are even {even}.")
else:
    print(f"In the array, there are {len(even)} even numbers{even}, and {len(odd)} odd numbers{odd}")