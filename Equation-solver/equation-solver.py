from abc import ABC, abstractmethod  # Importing Abstract Base Class (ABC) and abstractmethod for creating abstract classes
import re  # Importing the regular expression module for string manipulation

# Abstract base class for equations
class Equation(ABC):
    degree: int  # Degree of the equation (e.g., 1 for linear, 2 for quadratic)
    type: str  # Type of the equation (e.g., "Linear Equation", "Quadratic Equation")
  
    def __init__(self, *args):  # Constructor to initialize coefficients of the equation
        # Check if the number of arguments matches the degree + 1
        if (self.degree + 1) != len(args):
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        # Ensure all coefficients are of type int or float
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        # Ensure the highest degree coefficient is not zero
        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")
        # Store coefficients in a dictionary with keys as powers of x
        self.coefficients = {(len(args) - n - 1): arg for n, arg in enumerate(args)}

    def __init_subclass__(cls):  # Ensures subclasses define required attributes
        # Check if the subclass has the 'degree' attribute
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )
        # Check if the subclass has the 'type' attribute
        if not hasattr(cls, "type"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'type'"
            )

    def __str__(self):  # String representation of the equation
        terms = []  # List to store terms of the equation
        for n, coefficient in self.coefficients.items():  # Iterate through coefficients
            if not coefficient:  # Skip zero coefficients
                continue
            if n == 0:  # Constant term
                terms.append(f'{coefficient:+}')
            elif n == 1:  # Linear term
                terms.append(f'{coefficient:+}x')
            else:  # Higher degree terms
                terms.append(f"{coefficient:+}x**{n}")
        # Join terms into a single string and format it
        equation_string = ' '.join(terms) + ' = 0'
        return re.sub(r"(?<!\d)1(?=x)", "", equation_string.strip("+"))        

    @abstractmethod
    def solve(self):  # Abstract method to solve the equation
        pass
        
    @abstractmethod
    def analyze(self):  # Abstract method to analyze the equation
        pass

# Class for linear equations
class LinearEquation(Equation):
    degree = 1  # Degree of a linear equation is 1
    type = 'Linear Equation'  # Type of the equation

    def solve(self):  # Solve the linear equation
        a, b = self.coefficients.values()  # Extract coefficients
        x = -b / a  # Calculate the root
        return [x]  # Return the root as a list

    def analyze(self):  # Analyze the linear equation
        slope, intercept = self.coefficients.values()  # Extract slope and intercept
        return {'slope': slope, 'intercept': intercept}  # Return analysis as a dictionary

# Class for quadratic equations
class QuadraticEquation(Equation):
    degree = 2  # Degree of a quadratic equation is 2
    type = 'Quadratic Equation'  # Type of the equation

    def __init__(self, *args):  # Constructor for quadratic equations
        super().__init__(*args)  # Call the parent class constructor
        a, b, c = self.coefficients.values()  # Extract coefficients
        self.delta = b**2 - 4 * a * c  # Calculate the discriminant (delta)

    def solve(self):  # Solve the quadratic equation
        if self.delta < 0:  # No real roots if delta is negative
            return []
        a, b, _ = self.coefficients.values()  # Extract coefficients
        x1 = (-b + (self.delta) ** 0.5) / (2 * a)  # Calculate the first root
        x2 = (-b - (self.delta) ** 0.5) / (2 * a)  # Calculate the second root
        if self.delta == 0:  # If delta is zero, there is only one root
            return [x1]
        return [x1, x2]  # Return both roots

    def analyze(self):  # Analyze the quadratic equation
        a, b, c = self.coefficients.values()  # Extract coefficients
        x = -b / (2 * a)  # Calculate the x-coordinate of the vertex
        y = a * x**2 + b * x + c  # Calculate the y-coordinate of the vertex
        if a > 0:  # Determine the concavity of the parabola
            concavity = 'upwards'
            min_max = 'min'
        else:
            concavity = 'downwards'
            min_max = 'max'
        # Return analysis as a dictionary
        return {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}

# Function to solve and analyze an equation
def solver(equation):
    if not isinstance(equation, Equation):  # Ensure the argument is an Equation object
        raise TypeError("Argument must be an Equation object")

    # Prepare the output string with equation type and representation
    output_string = f'\n{equation.type:-^24}'
    output_string += f'\n\n{equation!s:^24}\n\n'
    output_string += f'{"Solutions":-^24}\n\n'
    results = equation.solve()  # Solve the equation
    match results:  # Format the solutions based on the number of roots
        case []:
            result_list = ['No real roots']
        case [x]:
            result_list = [f'x = {x:+.3f}']
        case [x1, x2]:
            result_list = [f'x1 = {x1:+.3f}', f'x2 = {x2:+.3f}']
    for result in result_list:  # Add solutions to the output string
        output_string += f'{result:^24}\n'
    output_string += f'\n{"Details":-^24}\n\n'
    details = equation.analyze()  # Analyze the equation
    match details:  # Format the analysis details
        case {'slope': slope, 'intercept': intercept}:
            details_list = [f'slope = {slope:>16.3f}', f'y-intercept = {intercept:>10.3f}']
        case {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}:
            coord = f'({x:.3f}, {y:.3f})'
            details_list = [f'concavity = {concavity}', f'{min_max} = {coord}']
    for detail in details_list:  # Add analysis details to the output string
        output_string += f'{detail}\n'
    return output_string  # Return the formatted output string

# Create a linear equation object
lin_eq = LinearEquation(2, 3)
# Create a quadratic equation object
quadr_eq = QuadraticEquation(1, 2, 1)
# Solve and analyze the quadratic equation, then print the result
print(solver(quadr_eq))
