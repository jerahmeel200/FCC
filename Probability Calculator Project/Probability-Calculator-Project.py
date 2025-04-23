import copy  # Importing the copy module to create deep copies of objects
import random  # Importing the random module for random sampling

class Hat:
    def __init__(self, **kwargs):
        # Initialize the Hat object with a dictionary of ball colors and their counts
        self.contents = []  # List to store all balls in the hat
        for color, count in kwargs.items():  # Iterate through the provided colors and counts
            self.contents.extend([color] * count)  # Add the specified number of each color to the contents

    def draw(self, num_balls):
        # Method to draw a specified number of balls from the hat
        if num_balls >= len(self.contents):  # If the number of balls to draw is greater than or equal to the total balls
            drawn = self.contents.copy()  # Copy all balls to the drawn list
            self.contents.clear()  # Clear the contents of the hat
            return drawn  # Return all balls as drawn
        
        # Randomly select the specified number of balls
        drawn = random.sample(self.contents, num_balls)  # Randomly sample balls without replacement
        for ball in drawn:  # Iterate through the drawn balls
            self.contents.remove(ball)  # Remove each drawn ball from the hat
        return drawn  # Return the list of drawn balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Function to perform an experiment to calculate the probability of drawing expected balls
    success_count = 0  # Counter for successful experiments

    for _ in range(num_experiments):  # Repeat the experiment for the specified number of times
        trial_hat = copy.deepcopy(hat)  # Create a deep copy of the hat to avoid modifying the original
        drawn_balls = trial_hat.draw(num_balls_drawn)  # Draw the specified number of balls

        # Count the occurrences of each ball drawn
        drawn_counts = {}  # Dictionary to store the count of each drawn ball
        for ball in drawn_balls:  # Iterate through the drawn balls
            if ball in drawn_counts:  # If the ball is already in the dictionary
                drawn_counts[ball] += 1  # Increment its count
            else:
                drawn_counts[ball] = 1  # Otherwise, initialize its count to 1

        # Check if the drawn balls meet or exceed the expected counts
        success = True  # Flag to track if the experiment is successful
        for color, min_count in expected_balls.items():  # Iterate through the expected balls and their counts
            if drawn_counts.get(color, 0) < min_count:  # If the drawn count is less than the expected count
                success = False  # Mark the experiment as unsuccessful
                break  # Exit the loop
        
        if success:  # If the experiment is successful
            success_count += 1  # Increment the success counter

    # Return the probability of success as the ratio of successful experiments to total experiments
    return success_count / num_experiments
