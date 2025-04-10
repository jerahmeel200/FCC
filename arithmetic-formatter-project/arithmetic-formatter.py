def arithmetic_arranger(problems, show_answers=False):
    # Define the operators
    plus = "+"
    minus = "-"
    # Initialize a list to store formatted problems
    formatted_problem_list = []
    # Initialize the arranged problems with placeholders for lines
    arranged_problems = ['', '', '', ''] if show_answers else ['', '', '']
    # Define the space between problems
    spacer = ' ' * 4

    # Check if there are more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Loop through each problem
    for problem in problems:
        # Check if the operator is valid
        if plus not in problem and minus not in problem:
            return "Error: Operator must be '+' or '-'."

        # Split the problem into components
        symbols = problem.split()
        line1 = symbols[0]  # First number
        operator = symbols[1]  # Operator
        line2 = symbols[2]  # Second number

        # Check if both operands are digits
        if not line1.isdigit() or not line2.isdigit():
            return 'Error: Numbers must only contain digits.'
        # Check if the operands are within the allowed length
        if len(line1) > 4 or len(line2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate the lengths of the operands
        len1, len2 = len(line1), len(line2)
        # Determine the width of the problem
        longest = max(len1, len2)
        width = longest + 2  # Add 2 for the operator and space

        # Format the top line (first operand)
        top = line1.rjust(width)
        # Format the bottom line (operator and second operand)
        bottom = operator + ' ' + line2.rjust(longest)
        # Create the dash line
        dash = '-' * width

        # Calculate the answer if show_answers is True
        if show_answers:
            if operator == '+':
                result = int(line1) + int(line2)  # Perform addition
            else:
                result = int(line1) - int(line2)  # Perform subtraction
            # Format the answer line
            answer = str(result).rjust(width)
            # Append all lines to the formatted problem list
            formatted_problem_list.append([top, bottom, dash, answer])
        else:
            # Append only the top, bottom, and dash lines
            formatted_problem_list.append([top, bottom, dash])

    # Build the arranged problems line by line
    for i in range(len(arranged_problems)):
        for j, parts in enumerate(formatted_problem_list):
            # Add the corresponding part of each problem to the line
            arranged_problems[i] += parts[i]
            # Add spacing between problems, except for the last one
            if j < len(formatted_problem_list) - 1:
                arranged_problems[i] += spacer

    # Join the lines with newline characters and return the result
    return '\n'.join(arranged_problems[:4 if show_answers else 3])


# Test the function with example problems and show answers
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)}')



def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ''
    second_line = ''
    dashes = ''
    answers = ''

    for index, problem in enumerate(problems):
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2
        top = num1.rjust(width)
        bottom = operator + ' ' + num2.rjust(width - 2)
        line = '-' * width

        if show_answers:
            result = str(eval(f"{num1} {operator} {num2}")).rjust(width)
            answers += result + ('    ' if index < len(problems) - 1 else '')

        first_line += top + ('    ' if index < len(problems) - 1 else '')
        second_line += bottom + ('    ' if index < len(problems) - 1 else '')
        dashes += line + ('    ' if index < len(problems) - 1 else '')

    arranged = f"{first_line}\n{second_line}\n{dashes}"
    if show_answers:
        arranged += f"\n{answers}"

    return arranged


# Test
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))
