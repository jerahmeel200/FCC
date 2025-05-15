# Function to convert a PascalCase or camelCase string to snake_case
def convert_to_snake_case(pascal_or_camel_cased_string):
    # Create a list of characters where uppercase letters are prefixed with '_'
    # and converted to lowercase, while other characters remain unchanged
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()  # Add '_' before uppercase letters and convert to lowercase
        else char  # Keep lowercase letters and other characters as is
        for char in pascal_or_camel_cased_string  # Iterate through each character in the input string
    ]

    # Join the list into a single string and remove any leading '_' using strip
    return ''.join(snake_cased_char_list).strip('_')


# Main function to demonstrate the conversion
def main():
    # Print the result of converting a sample PascalCase string to snake_case
    print(convert_to_snake_case('aLongAndComplexString'))
    
# Call the main function to execute the program
main()
    
    
    
