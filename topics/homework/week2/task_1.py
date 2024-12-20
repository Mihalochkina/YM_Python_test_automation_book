# Bubble Sort Algorithm
# In ascending order (regular one)
def input_data():
    user_input = input("Enter a sequence of numbers separated by spaces: ")
    split_input = user_input.split()
    for x in split_input:
        try:
            int(x)
        except ValueError as e:
            print("Input should contain ONLY numbers. Try once again.")
            return input_data()
    numbers = [int(x) for x in user_input.split()]
    return numbers


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


a = input_data()
sorted_numbers = bubble_sort(a)

print("Sorted list in ascending order:", sorted_numbers)


# In descending order
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Condition is changed to <
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


a = input_data()
sorted_numbers = bubble_sort(a)

print("Sorted list in descending order:", sorted_numbers)


# With early stopping
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False  # Variable 'swapped' is added to track existence of swap

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Change 'swapped', if there was an exchange

        if not swapped:
            break  # go out of the cycle if there are no exchanges

    return arr


a = input_data()
sorted_numbers = bubble_sort(a)

print("Sorted list with loop breakout:", sorted_numbers)
