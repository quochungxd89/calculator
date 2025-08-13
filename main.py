import tkinter as tk
from logic.calculator import Calculator

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()