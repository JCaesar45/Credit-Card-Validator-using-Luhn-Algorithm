def verify_card_number(card_number: str) -> str:
    # Remove spaces and dashes
    cleaned_number = ''.join(char for char in card_number if char.isdigit())
    
    # Convert to list of integers
    digits = [int(d) for d in cleaned_number]
    
    # Double every other digit starting from the second last digit
    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
    
    # Sum all digits
    total = sum(digits)
    
    # Validate the sum
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
