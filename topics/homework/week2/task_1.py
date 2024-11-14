#Bubble Sort Algorithm
#In ascending order (regular one)
user_input = input("Введите последовательность чисел, разделенных пробелами: ")
numbers = [int(x) for x in user_input.split()]

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

sorted_numbers = bubble_sort(numbers)


print("Отсортированный по возрастанию список:", sorted_numbers)



#In descending order
user_input = input("Введите последовательность чисел, разделенных пробелами: ")
numbers = [int(x) for x in user_input.split()]

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]: # Изменено условие на <
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

sorted_numbers = bubble_sort(numbers)


print("Отсортированный по убыванию список:", sorted_numbers)


#With early stopping
user_input = input("Введите последовательность чисел, разделенных пробелами: ")
numbers = [int(x) for x in user_input.split()]

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False  # Добавленная переменная swapped для отслеживания замен

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Меняем значение swapped, если была совершена замена

        if not swapped:
            break  # Выходим из цикла, если нет замен на текущем проходе

    return arr

sorted_numbers = bubble_sort(numbers)


print("Отсортированный список с выходом из цикла:", sorted_numbers)