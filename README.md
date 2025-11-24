```markdown
# Credit Card Validator using Luhn Algorithm

## Overview
This project implements a credit card number validator using the Luhn algorithm. The Luhn algorithm is a simple checksum formula used to validate various identification numbers, primarily credit card numbers.

## Objective
Create a function `verify_card_number` that takes a string representing a credit card number and verifies whether it is valid according to the Luhn algorithm.

## How it works
The validator performs the following steps:
- Cleans the input string by removing any spaces or dashes.
- Converts the cleaned string into a list of digits.
- Starting from the rightmost digit (excluding the check digit), doubles every other digit.
- If doubling results in a number greater than 9, subtracts 9 from it.
- Sums all the digits.
- Checks if the total sum is divisible by 10.
- Returns "VALID!" if the number passes the check, otherwise returns "INVALID!".

## Usage
Call the function `verify_card_number` with a string of the credit card number:

```python
print(verify_card_number('453914889')) # Output: VALID!
print(verify_card_number('4111-1111-1111-1111')) # Output: VALID!
print(verify_card_number('453914881')) # Output: INVALID!
print(verify_card_number('1234 5678 9012 3456')) # Output: INVALID!
``

## Testing
The function is tested with various credit card number formats, including:
- Pure digit strings
- Strings with dashes
- Strings with spaces

## License
This project is for educational purposes and demonstrates the implementation of the Luhn algorithm in Python.
