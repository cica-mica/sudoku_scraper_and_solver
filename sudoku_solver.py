"""
For making the sudoku game GUI I use tkinter
"""
import tkinter as tk

root = tk.Tk()
root.title('Sudoku Game')

f1 = tk.Entry(root, text = '0')


f1.grid(row = 1, column = 1)

root.mainloop()
