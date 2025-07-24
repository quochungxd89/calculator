import tkinter as tk
from math import sin, cos, tan, log, sqrt, radians, pi, e, pow
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Máy Tính Khoa Học")
        self.root.geometry("520x570")
        self.root.configure(bg="#0c5789")

        self.expression = ""          
        self.display_expression = ""  

        self.input_text = tk.StringVar()
        self.result_text = tk.StringVar()

        self.input_text.set("0")
        self.result_text.set("= 0")

        # ===== Màn hình hiển thị =====
        display_frame = tk.Frame(self.root, height=100, bg="white")
        display_frame.pack(fill="both", padx=10, pady=10)

        input_label = tk.Label(display_frame, textvariable=self.input_text,
                               font=("Arial", 20), anchor="e", bg="white", fg="black")
        input_label.pack(expand=True, fill="both")

        result_label = tk.Label(display_frame, textvariable=self.result_text,
                                font=("Arial", 16), anchor="e", bg="white", fg="gray")
        result_label.pack(expand=True, fill="both")

        # ===== Bàn phím =====
        btn_frame = tk.Frame(self.root, bg="#0c5789")
        btn_frame.pack()

        buttons = [
            ['(', ')', 'AC', 'Del', 'sin'],
            ['7', '8', '9', '+', 'cos'],
            ['4', '5', '6', '-', 'tan'],
            ['1', '2', '3', 'x', 'log'],
            ['0', '.', '=', '/', 'x^2'],
            ['', '', '', '√', 'x^3']
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                if char == '':
                    continue
                btn = tk.Button(btn_frame, text=char, width=6, height=2,
                                font=("Arial", 14), fg="black", bg="white",
                                command=lambda ch=char: self.handle_button(ch))
                btn.grid(row=r, column=c, padx=5, pady=5)

    def handle_button(self, char):
        if char == 'AC':
            self.clear_all()
        elif char == 'Del':
            self.delete_last()
        elif char == '=':
            self.calculate()
        elif char == 'x^2':
            self.expression += '**2'
            self.display_expression += '^2'
            self.input_text.set(self.display_expression)
        elif char == 'x^3':
            self.expression += '**3'
            self.display_expression += '^3'
            self.input_text.set(self.display_expression)
        elif char == '√':
            self.expression += 'sqrt('
            self.display_expression += '√('
            self.input_text.set(self.display_expression)
        else:
            if self.expression == "0":
                self.expression = ""
                self.display_expression = ""

            if char == 'x':
                self.expression += '*'
                self.display_expression += 'x'
            elif char in ['sin', 'cos', 'tan', 'log']:
                self.expression += f"{char}("
                self.display_expression += f"{char}("
            else:
                self.expression += str(char)
                self.display_expression += str(char)
            self.input_text.set(self.display_expression)

    def clear_all(self):
        self.expression = ""
        self.display_expression = ""
        self.input_text.set("0")
        self.result_text.set("= 0")

    def delete_last(self):
        if self.expression.endswith("**2") and self.display_expression.endswith("^2"):
            self.expression = self.expression[:-3]
            self.display_expression = self.display_expression[:-2]
        elif self.expression.endswith("**3") and self.display_expression.endswith("^3"):
            self.expression = self.expression[:-3]
            self.display_expression = self.display_expression[:-2]
        else:
            self.expression = self.expression[:-1]
            self.display_expression = self.display_expression[:-1]
        self.input_text.set(self.display_expression if self.display_expression else "0")

    def calculate(self):
        try:
            result = eval(self.expression, {"__builtins__": None}, {
                "sin": lambda x: sin(radians(x)),
                "cos": lambda x: cos(radians(x)),
                "tan": lambda x: tan(radians(x)),
                "log": log,
                "sqrt": sqrt,
                "pi": pi,
                "e": e,
                "pow": pow
            })
            self.result_text.set("= " + str(result))
        except:
            messagebox.showerror("Lỗi", "Phép tính không hợp lệ!")
            self.clear_all()

# ===== Run chương trình =====
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()