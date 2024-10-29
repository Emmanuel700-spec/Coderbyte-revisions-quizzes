from collections import Counter

def first_non_repeating_char(s: str) -> str:
    lower_count = Counter(s.lower())
    
    for char in s:
        if lower_count[char.lower()] == 1:
            return char
    
    return ""

input_string = "sTreSS"
result = first_non_repeating_char(input_string)
print(f"The first non-repeating character is: {result}")  # Output: "T"
