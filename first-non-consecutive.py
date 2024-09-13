def first_non_consecutive(arr):
    if not arr:
        return None
    
    # Remove duplicates and sort the array
    arr = sorted(set(arr))
    
    # Iterate through the sorted array to find the first non-consecutive number
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    
    # Return None if all numbers are consecutive
    return None

# Example usage
input_list = [5, 1, 3, 4, 2, 8, 7, 6, 10]
print(f"The first non-consecutive number is: {first_non_consecutive(input_list)}")
