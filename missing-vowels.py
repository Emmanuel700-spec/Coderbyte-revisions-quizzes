def missing_vowels(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    found_vowels = set()
    
    # Iterate through the string and add vowels to found_vowels set
    for char in s:
        if char in vowels:
            found_vowels.add(char)
    
    # Determine the missing vowels by subtracting found_vowels from vowels
    missing = vowels - found_vowels
    
    # Return the missing vowels as a sorted string
    return ''.join(sorted(missing)) if missing else 'None'

# Example usage
input_string = "hello world"
print(f"Missing vowels: {missing_vowels(input_string)}")
