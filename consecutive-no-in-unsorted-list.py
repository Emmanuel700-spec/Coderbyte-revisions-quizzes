def consecutive_ranges(arr):
    if not arr:
        return []
    
    # Remove duplicates and sort the array
    arr = sorted(set(arr))
    
    # Initialize list to hold ranges
    ranges = []
    
    # Start with the first number
    start = arr[0]
    end = arr[0]
    
    for num in arr[1:]:
        if num == end + 1:
            # Extend the current range
            end = num
        else:
            # Finalize the current range
            if start == end:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}-{end}")
            # Start a new range
            start = num
            end = num
    
    # Finalize the last range
    if start == end:
        ranges.append(f"{start}")
    else:
        ranges.append(f"{start}-{end}")
    
    return ranges

# Example usage
input_list = [5, 1, 3, 4, 2, 8, 7, 6, 10]
print(f"Consecutive ranges: {consecutive_ranges(input_list)}")
