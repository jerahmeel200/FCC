def verify_card_number(card_number):
    # Initialize the sum of digits at odd positions
    sum_of_odd_digits = 0
    # Reverse the card number string
    card_number_reversed = card_number[::-1]
    # Extract digits at odd positions (1st, 3rd, etc.) from the reversed card number
    odd_digits = card_number_reversed[::2]

    # Loop through each odd-position digit and add it to the sum
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Initialize the sum of digits at even positions
    sum_of_even_digits = 0
    # Extract digits at even positions (2nd, 4th, etc.) from the reversed card number
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        # Double the digit at the even position
        number = int(digit) * 2
        # If the doubled value is 10 or greater, sum its digits
        if number >= 10:
            number = (number // 10) + (number % 10)
        # Add the processed number to the sum of even-position digits
        sum_of_even_digits += number

    # Calculate the total sum of odd and even position digits
    total = sum_of_odd_digits + sum_of_even_digits
    # Print the total sum for debugging purposes
    print(total)
    # Return True if the total is divisible by 10, otherwise False
    return total % 10 == 0

def main():
    # Define the card number to be validated
    card_number = '4111-1111-4555-1141'
    # Create a translation table to remove dashes and spaces from the card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    # Translate the card number to remove unwanted characters
    translated_card_number = card_number.translate(card_translation)

    # Check if the card number is valid using the Luhn algorithm
    if verify_card_number(translated_card_number):
        # Print VALID if the card number passes the Luhn check
        print('VALID!')
    else:
        # Print INVALID if the card number fails the Luhn check
        print('INVALID!')

# Call the main function to execute the program
main()