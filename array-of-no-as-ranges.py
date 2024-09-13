def array_to_ranges(arr):
    if not arr:
        return []
    
    # Sort the array to ensure consecutive numbers are adjacent
    arr = sorted(set(arr))
    
    ranges = []
    start = arr[0]
    end = arr[0]

    for num in arr[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}-{end}")
            start = num
            end = num

    # Append the last range
    if start == end:
        ranges.append(f"{start}")
    else:
        ranges.append(f"{start}-{end}")
    
    return ranges

# Example usage
input_array = [1, 2, 3, 5, 6, 8]
print(f"Ranges: {array_to_ranges(input_array)}")
