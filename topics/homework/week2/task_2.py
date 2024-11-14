#Caching Mechanism
number = int(input("Enter a number: "))# Prompt the user to input a number

cache = {}

def square(n):
    if n in cache:  # Check if result is already in the cache
        return cache[n]

    # If result is not in cache, calculate the square and store it in the cache
    result = n * n
    cache[n] = result

    return result

# Call the square function with the user's input
result = square(number)

print("The square of", number, "is", result)