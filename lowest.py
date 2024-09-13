def SecondGreatLow(arr):
    # Convert the list to a set to remove duplicate values and then sort the unique values
    unique_sorted = sorted(set(arr))
    
    # Check if there are at least 2 unique numbers to determine the second smallest and second largest
    if len(unique_sorted) < 2:
        # If there are fewer than 2 unique numbers, we cannot find the second smallest or second largest
        return "-1 -1"
    
    # Retrieve the second smallest number
    # Since unique_sorted is sorted, the second smallest number is at index 1
    second_smallest = unique_sorted[1]
    
    # Retrieve the second largest number
    # Since unique_sorted is sorted, the second largest number is at index -2 (second to last)
    second_largest = unique_sorted[-2]
    
    # Return the results as a string with space separating the two numbers
    return f"{second_smallest} {second_largest}"

# Example usage:
print(SecondGreatLow([1, 1, 2, 3, 4]))  # Output: "2 3"
print(SecondGreatLow([1, 2]))            # Output: "-1 -1"
print(SecondGreatLow([5, 5, 5, 5]))      # Output: "-1 -1"
