import math  # Importing the math module for mathematical operations

# Constants
GRAVITATIONAL_ACCELERATION = 9.81  # Gravitational acceleration constant (m/s^2)
PROJECTILE = "∙"  # Symbol to represent the projectile in the graph
x_axis_tick = "T"  # Symbol to represent the x-axis in the graph
y_axis_tick = "⊣"  # Symbol to represent the y-axis in the graph

# Class to represent a projectile
class Projectile:
    __slots__ = ('__speed', '__height', '__angle')  # Memory optimization by restricting attributes

    def __init__(self, speed, height, angle):
        # Initialize the projectile with speed, height, and angle
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)  # Convert angle to radians for calculations
        
    def __str__(self):
        # String representation of the projectile's details
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __calculate_displacement(self):
        # Calculate the horizontal displacement of the projectile
        horizontal_component = self.__speed * math.cos(self.__angle)  # Horizontal velocity component
        vertical_component = self.__speed * math.sin(self.__angle)  # Vertical velocity component
        squared_component = vertical_component**2  # Square of vertical velocity
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height  # Gravitational potential energy component
        sqrt_component = math.sqrt(squared_component + gh_component)  # Square root of the sum of components
        
        # Return the total horizontal displacement
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION
        
    def __calculate_y_coordinate(self, x):
        # Calculate the y-coordinate (height) of the projectile at a given x-coordinate
        height_component = self.__height  # Initial height
        angle_component = math.tan(self.__angle) * x  # Height due to angle
        acceleration_component = GRAVITATIONAL_ACCELERATION * x ** 2 / (
                2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)  # Height reduction due to gravity
        y_coordinate = height_component + angle_component - acceleration_component  # Total height

        return y_coordinate  # Return the y-coordinate
    
    def calculate_all_coordinates(self):
        # Calculate all (x, y) coordinates of the projectile's trajectory
        return [
            (x, self.__calculate_y_coordinate(x))  # Generate (x, y) pairs
            for x in range(math.ceil(self.__calculate_displacement()))  # Iterate up to the displacement
        ]

    # Property to get the initial height
    @property
    def height(self):
        return self.__height

    # Property to get the angle in degrees
    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    # Property to get the speed
    @property
    def speed(self):
        return self.__speed

    # Setter for height
    @height.setter
    def height(self, n):
        self.__height = n

    # Setter for angle (converts degrees to radians)
    @angle.setter
    def angle(self, n):
        self.__angle = math.radians(n)

    # Setter for speed
    @speed.setter
    def speed(self, s):
       self.__speed = s
    
    def __repr__(self):
        # Representation of the projectile object
        return f'{self.__class__}({self.speed}, {self.height}, {self.angle})'

# Class to represent the graph of the projectile's trajectory
class Graph:
    __slots__ = ('__coordinates')  # Memory optimization by restricting attributes

    def __init__(self, coord):
        # Initialize the graph with a list of coordinates
        self.__coordinates = coord

    def __repr__(self):
        # Representation of the graph object
        return f"Graph({self.__coordinates})"

    def create_coordinates_table(self):
        # Create a table of x and y coordinates
        table = '\n  x      y\n'  # Header for the table
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'  # Format each coordinate pair

        return table  # Return the formatted table

    def create_trajectory(self):
        # Create a visual representation of the projectile's trajectory

        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]  # Round coordinates to integers

        x_max = max(rounded_coords, key=lambda i: i[0])[0]  # Maximum x-coordinate
        y_max = max(rounded_coords, key=lambda j: j[1])[1]  # Maximum y-coordinate

        # Create a 2D matrix for the graph
        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        # Place the projectile symbol at the appropriate coordinates
        for x, y in rounded_coords:
            matrix_list[-1 - y][x] = PROJECTILE

        # Convert each row of the matrix to a string
        matrix = ["".join(line) for line in matrix_list]

        # Add y-axis ticks and x-axis ticks
        matrix_axes = [y_axis_tick + row for row in matrix]
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))

        # Combine all rows into a single string
        graph = "\n" + "\n".join(matrix_axes) + "\n"

        return graph  # Return the graph as a string

# Helper function to create and display the projectile and its graph
def projectile_helper(speed, height, angle):
    ball = Projectile(speed, height, angle)  # Create a projectile object
    coordinates = ball.calculate_all_coordinates()  # Calculate all trajectory coordinates
    graph = Graph(coordinates)  # Create a graph object

    print(ball)  # Print the projectile details
    print(graph.create_coordinates_table())  # Print the coordinates table
    print(graph.create_trajectory())  # Print the trajectory graph

# Call the function with test values
projectile_helper(15, 5, 60)  # Example usage with speed=15 m/s, height=5 m, angle=60°
