# Caching Mechanism
# Define a cache dictionary to store previously computed squares
cache = {}


# Define the square function with caching mechanism
def square(n):
    # Check if the result for the given n is already in the cache
    if n in cache:
        print("Result retrieved from cache.")
        return cache[n]
    else:
        # Compute the square
        result = n * n
        # Store the result in the cache
        cache[n] = result
        print("Result computed and stored in cache.")
        return result


# Testing the square function with caching
print(square(5))  # Result computed and stored in cache. Output: 25
print(square(5))  # Result retrieved from cache. Output: 25
print(square(3))  # Result computed and stored in cache. Output: 9
print(square(3))  # Result retrieved from cache. Output: 9
