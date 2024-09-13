def first_repeating_char(s: str) -> str:
    seen = set()  # Track characters we've seen
    
    for char in s:
        if char in seen:
            return char  # Return the first repeating character
        seen.add(char)  # Add the character to the set
    
    return None  # Return None if no character repeats

# Example usage
input_string = "swiss"
print(f"The first repeating character is: {first_repeating_char(input_string)}")
