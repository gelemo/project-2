import tkinter as tk
from tkinter import messagebox

class SudokuGame:
    def __init__(self, board):
        self.board = board
        self.solution = [row[:] for row in board]
        self.init_gui()

    def init_gui(self):
        self.root = tk.Tk()
        self.root.title("Sudoku Game")

        self.entry_board = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    entry_text = str(self.board[i][j])
                    state = 'disabled'
                else:
                    entry_text = ''
                    state = 'normal'

                self.entry_board[i][j] = tk.Entry(
                    self.root, width=2, font=('Arial', 18), justify='center', state=state)
                self.entry_board[i][j].insert(0, entry_text)
                self.entry_board[i][j].grid(row=i, column=j)

        submit_btn = tk.Button(self.root, text="Submit", command=self.check_solution)
        submit_btn.grid(row=9, column=4)

    def check_solution(self):
        for i in range(9):
            for j in range(9):
                entry_text = self.entry_board[i][j].get()
                if entry_text == '':
                    self.board[i][j] = 0
                elif not entry_text.isdigit() or int(entry_text) > 9:
                    messagebox.showerror("Error", "Invalid input!")
                    return
                else:
                    self.board[i][j] = int(entry_text)

        if self.solve_sudoku():
            if self.board == self.solution:
                messagebox.showinfo("Success", "Congratulations! Sudoku solved!")
            else:
                messagebox.showinfo("Incorrect", "Incorrect solution.")
        else:
            messagebox.showerror("Error", "No solution exists.")

    def solve_sudoku(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.board[row][col] = num
                if self.solve_sudoku():
                    return True
                self.board[row][col] = 0

        return False

    def is_valid(self, num, row, col):
        def used_in_row(num, row):
            return num in self.board[row]

        def used_in_col(num, col):
            for i in range(9):
                if self.board[i][col] == num:
                    return True
            return False

        def used_in_box(num, start_row, start_col):
            for i in range(3):
                for j in range(3):
                    if self.board[i + start_row][j + start_col] == num:
                        return True
            return False

        return not used_in_row(num, row) and not used_in_col(num, col) and not used_in_box(num, row - row % 3, col - col % 3)

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def start(self):
        self.root.mainloop()

# Example Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

game = SudokuGame(board)
game.start()
