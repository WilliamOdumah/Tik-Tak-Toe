import random
import numpy as np
from player import Player

class Board:
    def __init__(self, size, style):
        self.size = size
        self.style = style
        self.created_with = "list"
        self.board = self.create_board_list(size, style)
        self.spots = size * size
        self.spots_left = self.spots
        
        
        
    def create_board(self, size, style):
        options = ['list', 'dict', 'numpy']
        choice = random.choice(options)
        print("the choice was:::::"+str(choice))
        if choice == 'list':
            self.created_with = "list"
            print("IN LIST")
            return self.create_board_list(size,style)
        elif choice == 'dict':
            print("IN DICT")
            self.created_with = "dict"
            return self.create_board_dict(size,style)
        else:
            print("IN NUMPY")
            self.created_with = "numpy"
            return self.create_board_numpy(size,style)                
    
    def create_board_list(self, size, style):
        # List of lists
        # grid = [[" " for _ in range(size)]for _ in range(size)] (SHORTER VERSION)
        grid = []
        for row in range(size):
            grid.append([])
            for col in range(size):
                grid[row].append(" ")
                
        return grid
    
    def create_board_dict(self, size, style):
        grid = {(row, col): "" for row in range(size) for col in range(size)}
        return grid
    
    def create_board_numpy(self, size, style):
        grid = np.full((size,size), " ")
        return grid
    
    def display_board(self):
        if self.created_with == "list":
            self.display_board_list()
        elif self.created_with == "dict":
            self.display_board_dict()
        elif self.created_with == "numpy":
            self.display_board_numpy()
        else:
            print("No board was created")
            
            
            
    def display_board_list(self):
        for row in range(self.size):
            # Create a string for the current row
            row_str = " | ".join(self.board[row])
            print(row_str)
            if row < self.size - 1:
                print("-" * (self.size * 3))  # Print a separator line between rows
        
    def display_board_dict(self):
        for row in range(self.size):
            row_values = []
            for col in range(self.size):
                row_values.append(str(self.board[(row, col)]))
            print(" | ".join(row_values))
            if row < self.size - 1:
                print("-" * (self.size *3))
    
    def display_board_numpy(self):
        for i, row in enumerate(self.board):
            # Convert each element of the row to a string
            row_str = " | ".join(str(cell) for cell in row)
            print(row_str)
            # Check if it's not the last row using index comparison
            if i < self.size - 1:
                print("-" * (self.size * 4 - 1))  # Print a separator line
                
                
    def play_list(self, where, who, name):
        row, col = where # Unpack dimensions
        if 0 <= row < self.size and 0<= col < self.size:
            # Check if spot available
            if self.board[row][col] == " ":
                self.board[row][col] = who
                print("\n"+name+" played\n")
                self.spots_left = self.spots_left - 1
                self.display_board_list()
            else:
                print("\nSpot not available. Try again\n")
        else:
            print("\nThats not a spot\n")
            
    
    def check_status_list(self, spot, who):
        row, col = spot
        # Returns True if a player has won in any way
        return (self.check_row(row=row,who=who) or self.check_col(col=col, who=who) or self.check_diagonal(who=who)) 
            
    def check_row(self, row, who):
        progress = 0
        for col in range(self.size):
            if self.board[row][col] == who:
                progress = progress + 1
                if progress == 3:
                    return True
            else:
                # Return False if there is no way to win on this row
                return False

    def check_col(self, col, who):
        progress = 0
        for row in range(self.size):
            if self.board[row][col] == who:
                progress = progress + 1
                if progress == 3:
                    return True
            else:
                # Return False if there is no way to win on this column
                return False
            
    def check_diagonal(self, who):
        return (self.check_left_diagonal(who=who) or self.check_right_diagonal(who=who))     
            
    def check_left_diagonal(self, who):
        progress = 0
        for row in range(self.size):
            if self.board[row][row] == who:
                progress = progress + 1
                if progress == 3:
                    return True
            else:
                # Return False if there is no way to win on this diagonal
                return False     
            
    def check_right_diagonal(self, who):
        progress = 0
        col = self.size - 1
        for row in range(self.size):
            if self.board[row][col] == who:
                col = col - 1 
                progress = progress + 1
                if progress == 3:
                    return True
            else:
                # Return False if there is no way to win on this diagonal
                return False
            
    def clear_board_list(self):
        self.spots_left = 0
        for row in range(self.size):
            for col in range(self.size):
                self.board[row][col] = " "
     