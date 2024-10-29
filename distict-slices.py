def count_distinct_slices(M, A):
    n = len(A)           # Get the length of the input array A
    seen = set()        # Initialize a set to track distinct elements in the current slice
    start = 0           # Pointer to the start of the current slice
    count = 0           # Initialize a counter for the number of distinct slices

    # Loop through the array using 'end' as the pointer for the current element
    for end in range(n):
        # While the current element A[end] is already in the seen set (indicating a duplicate)
        while A[end] in seen:
            # Remove the element at the 'start' pointer from the set to shrink the window
            seen.remove(A[start])
            # Move the 'start' pointer to the right to find a new slice without duplicates
            start += 1
            
        # After ensuring A[end] is not a duplicate, add it to the seen set
        seen.add(A[end])
        
        # Count the distinct slices that end at the 'end' index
        # All slices starting from 'start' to 'end' are valid
        count += end - start + 1
        
        # To prevent integer overflow, we cap the count at 1,000,000,000
        if count > 1_000_000_000:
            return 1_000_000_000
            
    return count  # Return the total count of distinct slices

# Example usage:
M = 6  # Maximum value in A (not directly used in the function)
A = [3, 4, 5, 5, 2]  # Input array
print(count_distinct_slices(M, A))  # Output: 9 (number of distinct slices)
