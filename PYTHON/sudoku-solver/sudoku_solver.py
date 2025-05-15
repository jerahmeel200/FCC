class Board:
    def __init__(self, board):
        # Initialize the board with the given 2D list
        self.board = board

    def __str__(self):
        # Convert the board into a human-readable string format
        board_str = ''
        for row in self.board:
            # Replace 0 with '*' for better visualization
            row_str = [str(i) if i else '*' for i in row]
            # Join the row elements with spaces and add a newline
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str

    def find_empty_cell(self):
        # Find the first empty cell (represented by 0) in the board
        for row, contents in enumerate(self.board):
            try:
                # Check if 0 exists in the current row
                col = contents.index(0)
                # Return the row and column index of the empty cell
                return row, col
            except ValueError:
                # If 0 is not found in the row, continue to the next row
                pass
        # Return None if no empty cell is found
        return None

    def valid_in_row(self, row, num):
        # Check if the number is not already present in the given row
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # Check if the number is not already present in the given column
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        # Check if the number is not already present in the 3x3 subgrid
        row_start = (row // 3) * 3  # Calculate the starting row of the subgrid
        col_start = (col // 3) * 3  # Calculate the starting column of the subgrid
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                # Return False if the number is found in the subgrid
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        # Check if placing the number in the empty cell is valid
        row, col = empty
        # Validate the number in the row, column, and 3x3 subgrid
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        # Return True if the number is valid in all three checks
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        # Solve the Sudoku puzzle using backtracking
        if (next_empty := self.find_empty_cell()) is None:
            # If no empty cell is found, the puzzle is solved
            return True
        for guess in range(1, 10):
            # Try placing numbers 1 through 9 in the empty cell
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                # Place the number in the empty cell
                self.board[row][col] = guess
                # Recursively attempt to solve the rest of the puzzle
                if self.solver():
                    return True
                # Reset the cell if the guess leads to an invalid solution
                self.board[row][col] = 0
        # Return False if no valid solution is found
        return False

def solve_sudoku(board):
    # Create a Board object with the given puzzle
    gameboard = Board(board)
    # Print the initial puzzle
    print(f'Puzzle to solve:\n{gameboard}')
    # Attempt to solve the puzzle
    if gameboard.solver():
        # Print the solved puzzle if successful
        print(f'Solved puzzle:\n{gameboard}')
    else:
        # Print a message if the puzzle is unsolvable
        print('The provided puzzle is unsolvable.')
    # Return the solved board (or the unsolved board if unsolvable)
    return gameboard

# Define a sample Sudoku puzzle
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

# Solve the Sudoku puzzle
solve_sudoku(puzzle)