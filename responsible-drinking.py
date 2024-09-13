def responsible_drinking(adults, drinks):
    """
    Provides advice on responsible drinking based on the number of drinks consumed.

    Parameters:
    - adults: Number of adults consuming alcohol.
    - drinks: Number of standard drinks consumed.

    Returns:
    - A message with advice on responsible drinking.
    """
    if adults <= 0 or drinks < 0:
        return "Invalid input. Number of adults must be positive and number of drinks cannot be negative."

    # General guideline: Maximum 2 standard drinks per day for women, 3 for men.
    max_drinks = {
        'women': 2,
        'men': 3
    }
    
    # Calculate average drinks per adult
    average_drinks_per_adult = drinks / adults
    
    advice = []
    for gender in max_drinks:
        if average_drinks_per_adult > max_drinks[gender]:
            advice.append(f"On average, {gender.capitalize()} are consuming more than the recommended {max_drinks[gender]} drinks per day.")
        else:
            advice.append(f"On average, {gender.capitalize()} are within the recommended limit of {max_drinks[gender]} drinks per day.")

    return " ".join(advice) + " Always drink responsibly. Stay hydrated and never drink and drive."

# Example usage
adults = 4
drinks = 10
print(responsible_drinking(adults, drinks))
