def valid_spacing(s: str) -> bool:
    """
    Check if the string has valid spacing:
    - No leading or trailing spaces.
    - No multiple consecutive spaces.

    Parameters:
    - s: The input string.

    Returns:
    - True if the spacing is valid, False otherwise.
    """
    # Strip leading and trailing spaces and split the string by spaces
    stripped_string = s.strip()
    words = stripped_string.split()
    
    # Rejoin the words with a single space to check if it matches the original stripped string
    normalized_string = ' '.join(words)
    
    return normalized_string == stripped_string

# Example usage
input_string = "  Hello   world! This  is a test.  "
print(f"Is the spacing valid? {valid_spacing(input_string)}")

# For normalizing the spacing
def normalize_spacing(s: str) -> str:
    """
    Normalize the spacing in the string:
    - Remove leading and trailing spaces.
    - Replace multiple consecutive spaces with a single space.

    Parameters:
    - s: The input string.

    Returns:
    - The normalized string.
    """
    # Strip leading and trailing spaces and replace multiple spaces with a single space
    return ' '.join(s.strip().split())

# Example usage
normalized_string = normalize_spacing(input_string)
print(f"Normalized string: '{normalized_string}'")
