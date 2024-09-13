def smallest_power_higher_than(base: int, value: int) -> int:
    if base <= 1 or value < 0:
        raise ValueError("Base must be greater than 1 and value must be non-negative.")

    power = 1
    while power <= value:
        power *= base

    return power

# Example usage
base = 2
value = 10
print(f"The smallest power of {base} higher than {value} is: {smallest_power_higher_than(base, value)}")
