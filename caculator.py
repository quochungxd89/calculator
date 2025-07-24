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
        self.linear_mode = False      # Đang ở chế độ PT bậc 1
        self.linear_step = 0          # 0: chưa nhập, 1: nhập a, 2: nhập b
        self.linear_a = None
        self.linear_b = None
        self.quadratic_mode = False   # Đang ở chế độ PT bậc 2
        self.quadratic_step = 0       # 0: chưa nhập, 1: nhập a, 2: nhập b, 3: nhập c
        self.quadratic_a = None
        self.quadratic_b = None
        self.quadratic_c = None

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
            ['(', ')', 'AC', 'Del', 'x10^n'],
            ['sin', 'cos', 'tan', 'cotan', 'log'],
            ['7', '8', '9', '+', 'x^2'],
            ['4', '5', '6', '-', 'x^3'],
            ['1', '2', '3', 'x', 'x^n'],
            ['0', '.', '=', '/', '√'],
            ['', '', '','PT bậc 1', 'PT bậc 2']
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
            if self.linear_mode:
                self.solve_linear_equation_step()
            elif self.quadratic_mode:
                self.solve_quadratic_equation_step()
            else:
                self.calculate()
        elif char == 'x^2':
            self.expression += '**2'
            self.display_expression += '^2'
            self.input_text.set(self.display_expression)
        elif char == 'x^3':
            self.expression += '**3'
            self.display_expression += '^3'
            self.input_text.set(self.display_expression)
        elif char == 'x^n':
            self.expression += '**'
            self.display_expression += '^'
            self.input_text.set(self.display_expression)
        elif char == 'x10^n':
            self.expression += '*10**'
            self.display_expression += 'x10^'
            self.input_text.set(self.display_expression)
        elif char == '√':
            self.expression += 'sqrt('
            self.display_expression += '√('
            self.input_text.set(self.display_expression)
        elif char == 'PT bậc 1':
            self.linear_mode = True
            self.linear_step = 1
            self.linear_a = None
            self.linear_b = None
            self.expression = ""
            self.display_expression = ""
            self.input_text.set("Nhập a rồi nhấn =")
            self.result_text.set("")
        elif char == 'PT bậc 2':
            self.quadratic_mode = True
            self.quadratic_step = 1
            self.quadratic_a = None
            self.quadratic_b = None
            self.quadratic_c = None
            self.expression = ""
            self.display_expression = ""
            self.input_text.set("Nhập a rồi nhấn =")
            self.result_text.set("")
        else:
            if self.linear_mode:
                if char in '0123456789.-':
                    self.expression += str(char)
                    self.display_expression += str(char)
                    self.input_text.set(self.display_expression)
            elif self.quadratic_mode:
                if char in '0123456789.-':
                    self.expression += str(char)
                    self.display_expression += str(char)
                    self.input_text.set(self.display_expression)
            else:
                if self.expression == "0":
                    self.expression = ""
                    self.display_expression = ""

                if char == 'x':
                    self.expression += '*'
                    self.display_expression += 'x'
                elif char in ['sin', 'cos', 'tan', 'cotan', 'log']:
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
        self.linear_mode = False
        self.linear_step = 0
        self.linear_a = None
        self.linear_b = None
        self.quadratic_mode = False
        self.quadratic_step = 0
        self.quadratic_a = None
        self.quadratic_b = None
        self.quadratic_c = None

    def delete_last(self):
        if self.expression.endswith("**2") and self.display_expression.endswith("^2"):
            self.expression = self.expression[:-3]
            self.display_expression = self.display_expression[:-2]
        elif self.expression.endswith("**3") and self.display_expression.endswith("^3"):
            self.expression = self.expression[:-3]
            self.display_expression = self.display_expression[:-2]
        elif self.expression.endswith("**n") and self.display_expression.endswith("^n"):
            self.expression = self.expression[:-4]
            self.display_expression = self.display_expression[:-3]
        elif self.expression.endswith("*10**") and self.display_expression.endswith("x10^"):
            self.expression = self.expression[:-5]
            self.display_expression = self.display_expression[:-4]
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
                "cotan": lambda x: 1/tan(radians(x)),
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

    def solve_linear_equation_step(self):
        if self.linear_step == 1:
            # Đang nhập a
            try:
                a = float(self.expression)
            except Exception:
                self.result_text.set("Hệ số a không hợp lệ!")
                self.expression = ""
                self.display_expression = ""
                self.input_text.set("")
                return
            self.linear_a = a
            self.linear_step = 2
            self.expression = ""
            self.display_expression = ""
            self.input_text.set("Nhập b rồi nhấn =")
        elif self.linear_step == 2:
            # Đang nhập b
            try:
                b = float(self.expression)
            except Exception:
                self.result_text.set("Hệ số b không hợp lệ!")
                self.expression = ""
                self.display_expression = ""
                self.input_text.set("")
                return
            self.linear_b = b
            # Giải phương trình
            a = self.linear_a
            b = self.linear_b
            if a == 0:
                if b == 0:
                    result = "Vô số nghiệm"
                else:
                    result = "Vô nghiệm"
            else:
                result = f"x = {-b / a}"
            self.result_text.set(result)
            self.linear_mode = False
            self.linear_step = 0
            self.linear_a = None
            self.linear_b = None
            self.expression = ""
            self.display_expression = ""
            self.input_text.set("0")

    def solve_quadratic_equation_step(self):
        if self.quadratic_step == 1:
            # Đang nhập a
            try:
                a = float(self.expression)
            except Exception:
                self.result_text.set("Hệ số a không hợp lệ!")
                self.expression = ""
                self.display_expression = ""
                self.input_text.set("")
                return
            self.quadratic_a = a
            self.quadratic_step = 2
            self.expression = ""
            self.display_expression = ""
            self.input_text.set("Nhập b rồi nhấn =")
        elif self.quadratic_step == 2:
            # Đang nhập b
            try:
                b = float(self.expression)
            except Exception:
                self.result_text.set("Hệ số b không hợp lệ!")
                self.expression = ""
                self.display_expression = ""
                self.input_text.set("")
                return
            self.quadratic_b = b
            self.quadratic_step = 3
            self.expression = ""
            self.display_expression = ""
            self.input_text.set("Nhập c rồi nhấn =")
        elif self.quadratic_step == 3:
            # Đang nhập c
            try:
                c = float(self.expression)
            except Exception:
                self.result_text.set("Hệ số c không hợp lệ!")
                self.expression = ""
                self.display_expression = ""
                self.input_text.set("")
                return
            self.quadratic_c = c
            # Giải phương trình bậc 2
            a = self.quadratic_a
            b = self.quadratic_b
            c = self.quadratic_c
            result = self.solve_quadratic_equation(a, b, c)
            self.result_text.set(result)
            self.quadratic_mode = False
            self.quadratic_step = 0
            self.quadratic_a = None
            self.quadratic_b = None
            self.quadratic_c = None
            self.expression = ""
            self.display_expression = ""
            self.input_text.set("0")

    def solve_quadratic_equation(self, a, b, c):
        if a == 0:
            if b == 0:
                if c == 0:
                    return "Vô số nghiệm"
                else:
                    return "Vô nghiệm"
            else:
                return f"x = {-c / b}"
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = (-b + sqrt(delta)) / (2 * a)
            x2 = (-b - sqrt(delta)) / (2 * a)
            return f"x₁ = {x1}, x₂ = {x2}"
        elif delta == 0:
            x = -b / (2 * a)
            return f"x kép = {x}"
        else:
            return "Vô nghiệm"

# ===== Run chương trình =====
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()