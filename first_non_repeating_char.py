from collections import Counter

def first_non_repeating_char(s: str) -> str:
    # Create a counter object to count occurrences of each character
    char_count = Counter(s)
    
    # Iterate through the string and return the first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    # Return None if no non-repeating character is found
    return None

# Example usage:
input_string = "swiss"
result = first_non_repeating_char(input_string)
print(f"The first non-repeating character is: {result}")
