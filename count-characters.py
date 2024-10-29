#Count characters
from collections import Counter

def count_characters(s: str) -> dict:
   
    return dict(Counter(s))

# input_string = "hello world"
# character_counts = count_characters(input_string)
# print(f"Character counts: {character_counts}")

print(count_characters("aba"))  # Expected output: {'a': 2, 'b': 1}
print(count_characters(""))     # Expected output: {}
print(count_characters("hello"))  # Expected output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(count_characters("mississippi"))  # Expected output: {'m': 1, 'i': 4, 's': 4, 'p': 2}
print(count_characters("programming"))  # Expected output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
