def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # Check if the target number is negative, as square root of negative numbers is not defined in real numbers
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    
    # Handle the special case where the square root of 1 is 1
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    
    # Handle the special case where the square root of 0 is 0
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        # Initialize the lower bound of the search range
        low = 0
        # Initialize the upper bound of the search range
        high = max(1, square_target)
        # Variable to store the computed square root
        root = None
        
        # Perform the bisection method for a maximum number of iterations
        for _ in range(max_iterations):
            # Calculate the midpoint of the current range
            mid = (low + high) / 2
            # Calculate the square of the midpoint
            square_mid = mid**2

            # Check if the square of the midpoint is close enough to the target
            if abs(square_mid - square_target) < tolerance:
                root = mid  # Set the root to the midpoint
                break  # Exit the loop as the solution is found

            # If the square of the midpoint is less than the target, adjust the lower bound
            elif square_mid < square_target:
                low = mid
            # Otherwise, adjust the upper bound
            else:
                high = mid

        # If no solution is found within the maximum iterations, print a failure message
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            # Print the approximate square root
            print(f'The square root of {square_target} is approximately {root}')
    
    # Return the computed square root
    return root

# Define the number for which the square root is to be calculated
N = 16
# Call the function to calculate the square root of N
square_root_bisection(N)