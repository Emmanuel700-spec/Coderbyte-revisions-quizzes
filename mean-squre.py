def mean_square(arr):
    """
    Calculate the mean of the squares of the elements in the array.

    Parameters:
    - arr: List of numbers (integers or floats).

    Returns:
    - The mean of the squared values as a float.
    """
    if not arr:
        return 0  # Handle empty array case
    
    # Calculate the squares of the elements
    squared_values = [x ** 2 for x in arr]
    
    # Compute the mean of the squared values
    mean_of_squares = sum(squared_values) / len(arr)
    
    return mean_of_squares

# Example usage
input_array = [1, 2, 3, 4, 5]
print(f"Mean square of the array: {mean_square(input_array)}")
