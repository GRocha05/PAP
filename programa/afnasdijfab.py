import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

path = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select file", filetypes = (("Text files", "*.txt"), ("all files", "*.*")))


         