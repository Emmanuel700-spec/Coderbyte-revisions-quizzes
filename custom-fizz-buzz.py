def custom_fizz_buzz(n: int, rules: dict) -> list:
    """
    Generate a list of custom Fizz Buzz results up to n with specified rules.

    Parameters:
    - n: The number of elements in the sequence (inclusive).
    - rules: A dictionary where keys are multiples and values are the corresponding strings to output.

    Returns:
    - A list of strings with custom Fizz Buzz results.
    """
    results = []
    
    for i in range(1, n + 1):
        output = ''
        for multiple, text in sorted(rules.items()):
            if i % multiple == 0:
                output += text
        
        if not output:
            output = str(i)
        
        results.append(output)
    
    return results

# Example usage
n = 20
rules = {
    3: "Fizz",
    5: "Buzz",
    7: "Bizz"  # Additional custom rule
}

print(custom_fizz_buzz(n, rules))
