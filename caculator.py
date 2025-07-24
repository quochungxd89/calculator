import tkinter as tk
from math import sin, cos, tan, log, sqrt, radians, pi, e, pow
from tkinter import messagebox
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Máy Tính Khoa Học")
        self.root.geometry("520x570")
        self.root.configure(bg="#0c5789")

        self.cal = ""          
        self.display_cal = ""  
        self.linear_mode = False      # Đang ở chế độ PT bậc 1
        self.linear_step = 0          # 0: chưa nhập, 1: nhập a, 2: nhập b
        self.linear_a = None
        self.linear_b = None
        self.quadratic_mode = False   # Đang ở chế độ PT bậc 2
        self.quadratic_step = 0       # 0: chưa nhập, 1: nhập a, 2: nhập b, 3: nhập c
        self.quadratic_a = None
        self.quadratic_b = None
        self.quadratic_c = None
        self.root_n_mode = False      # Đang nhập căn bậc n
        self.root_n_value = None     # Lưu giá trị n cho căn bậc n
        self.just_calculated = False # Đánh dấu vừa bấm =

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
            ['√', '3√', 'n√', 'PT bậc 1','PT bậc 2'],
            ['Bin', 'Dec', 'Hex', 'Oct', "'"],
            ['7', '8', '9', '+', 'x^2'],
            ['4', '5', '6', '-', 'x^3'],
            ['1', '2', '3', 'x', 'x^n'],
            ['0', '.', '=', '/', '1/x'],
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
        if self.just_calculated:
            if char in '0123456789.':
                self.cal = ''
                self.display_cal = ''
                self.input_text.set('')
                self.just_calculated = False
            elif char in ['+', '-', 'x', '/', '*']:
                last_result = self.result_text.get().replace('=','').strip()
                self.cal = last_result
                self.display_cal = last_result
                self.input_text.set(self.display_cal)
                self.just_calculated = False
            elif char in ['x^2', 'x^3', 'x^n', '√', '3√', 'n√', '1/x']:
                last_result = self.result_text.get().replace('=','').strip()
                self.cal = last_result
                self.display_cal = last_result
                self.input_text.set(self.display_cal)
                self.just_calculated = False
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
            self.cal += '**2'
            self.display_cal += '^2'
            self.input_text.set(self.display_cal)
        elif char == 'x^3':
            self.cal += '**3'
            self.display_cal += '^3'
            self.input_text.set(self.display_cal)
        elif char == 'x^n':
            self.cal += '**'
            self.display_cal += '^'
            self.input_text.set(self.display_cal)
        elif char == 'x10^n':
            self.cal += '*10**'
            self.display_cal += 'x10^'
            self.input_text.set(self.display_cal)
        elif char == '√':
            self.cal += 'sqrt('
            self.display_cal += '√('
            self.input_text.set(self.display_cal)
        elif char == '3√':
            self.root_n_mode = True
            self.root_n_value = 3
            self.cal += 'pow('
            self.display_cal += '3√('
            self.input_text.set(self.display_cal)
        elif char == '1/x':
            self.cal += '**(-1)'
            self.display_cal += '^(-1)'
            self.input_text.set(self.display_cal)
        elif char == 'n√':
            match = re.search(r'(\d+)$', self.cal)
            if match:
                n = int(match.group(1))
                self.cal = self.cal[:-len(str(n))]
                self.display_cal = self.display_cal[:-len(str(n))]
                self.root_n_mode = True
                self.root_n_value = n
                self.cal += 'pow('
                self.display_cal += f'{n}√('
                self.input_text.set(self.display_cal)
            else:
                self.root_n_mode = True
                self.root_n_value = 2
                self.cal += 'pow('
                self.display_cal += '2√('
                self.input_text.set(self.display_cal)
        elif char == ')':
            if self.root_n_mode and self.root_n_value is not None:
                n = self.root_n_value
                self.cal += f',1/{n})'
                self.display_cal += ')'
                self.input_text.set(self.display_cal)
                self.root_n_mode = False
                self.root_n_value = None
            else:
                self.cal += ')'
                self.display_cal += ')'
                self.input_text.set(self.display_cal)
        elif char == 'PT bậc 1':
            self.linear_mode = True
            self.linear_step = 1
            self.linear_a = None
            self.linear_b = None
            self.cal = ""
            self.display_cal = ""
            self.input_text.set("Nhập a rồi nhấn =")
            self.result_text.set("")
        elif char == 'PT bậc 2':
            self.quadratic_mode = True
            self.quadratic_step = 1
            self.quadratic_a = None
            self.quadratic_b = None
            self.quadratic_c = None
            self.cal = ""
            self.display_cal = ""
            self.input_text.set("Nhập a rồi nhấn =")
            self.result_text.set("")
        elif char == 'Bin':
            value = self.get_current_value()
            try:
                int_value = self.parse_int_value(value)
                self.result_text.set('= ' + bin(int_value))
                self.just_calculated = True
            except:
                self.result_text.set('Lỗi!')
        elif char == 'Dec':
            value = self.get_current_value()
            try:
                dec_value = self.parse_int_value(value)
                self.result_text.set('= ' + str(dec_value))
                self.just_calculated = True
            except:
                self.result_text.set('Lỗi!')
        elif char == 'Hex':
            value = self.get_current_value()
            try:
                int_value = self.parse_int_value(value)
                self.result_text.set('= ' + hex(int_value))
                self.just_calculated = True
            except:
                self.result_text.set('Lỗi!')
        elif char == 'Oct':
            value = self.get_current_value()
            try:
                int_value = self.parse_int_value(value)
                self.result_text.set('= ' + oct(int_value))
                self.just_calculated = True
            except:
                self.result_text.set('Lỗi!')
        elif char == "'":
            self.cal += "'"
            self.display_cal += "'"
            self.input_text.set(self.display_cal)
        else:
            if self.linear_mode:
                if char in '0123456789.-':
                    self.cal += str(char)
                    self.display_cal += str(char)
                    self.input_text.set(self.display_cal)
            elif self.quadratic_mode:
                if char in '0123456789.-':
                    self.cal += str(char)
                    self.display_cal += str(char)
                    self.input_text.set(self.display_cal)
            else:
                if self.cal == "0":
                    self.cal = ""
                    self.display_cal = ""

                if char == 'x':
                    self.cal += '*'
                    self.display_cal += 'x'
                elif char in ['sin', 'cos', 'tan', 'cotan', 'log']:
                    self.cal += f"{char}("
                    self.display_cal += f"{char}("
                else:
                    self.cal += str(char)
                    self.display_cal += str(char)
                self.input_text.set(self.display_cal)

    def clear_all(self):
        self.cal = ""
        self.display_cal = ""
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
        self.just_calculated = False

    def delete_last(self):
        if self.cal.endswith("**2") and self.display_cal.endswith("^2"):
            self.cal = self.cal[:-3]
            self.display_cal = self.display_cal[:-2]
        elif self.cal.endswith("**3") and self.display_cal.endswith("^3"):
            self.cal = self.cal[:-3]
            self.display_cal = self.display_cal[:-2]
        elif self.cal.endswith("**n") and self.display_cal.endswith("^n"):
            self.cal = self.cal[:-4]
            self.display_cal = self.display_cal[:-3]
        elif self.cal.endswith("*10**") and self.display_cal.endswith("x10^"):
            self.cal = self.cal[:-5]
            self.display_cal = self.display_cal[:-4]
        else:
            self.cal = self.cal[:-1]
            self.display_cal = self.display_cal[:-1]
        self.input_text.set(self.display_cal if self.display_cal else "0")

    def calculate(self):
        try:
            expr = self._convert_deg_min_sec(self.cal)
            result = eval(expr, {"__builtins__": None}, {
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
            self.just_calculated = True
        except:
            messagebox.showerror("Lỗi", "Phép tính không hợp lệ!")
            self.clear_all()

    def _convert_deg_min_sec(self, expr):
        def repl(m):
            deg = float(m.group(1)) if m.group(1) else 0
            minute = float(m.group(2)) if m.group(2) else 0
            second = float(m.group(3)) if m.group(3) else 0
            return f"({deg} + {minute}/60 + {second}/3600)"
        for trig in ['sin', 'cos', 'tan', 'cotan']:
            expr = re.sub(
                fr'{trig}\((\d+)(?:\'(\d+))?(?:\'(\d+))?\'?\)',
                lambda m: f"{trig}{repl(m)}", expr)
        return expr

    def solve_linear_equation_step(self):
        if self.linear_step == 1:
            # Nhập a
            try:
                a = float(self.cal)
            except Exception:
                self.result_text.set("Hệ số a không hợp lệ!")
                self.cal = ""
                self.display_cal = ""
                self.input_text.set("")
                return
            self.linear_a = a
            self.linear_step = 2
            self.cal = ""
            self.display_cal = ""
            self.input_text.set("Nhập b rồi nhấn =")
        elif self.linear_step == 2:
            # Nhập b
            try:
                b = float(self.cal)
            except Exception:
                self.result_text.set("Hệ số b không hợp lệ!")
                self.cal = ""
                self.display_cal = ""
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
            self.cal = ""
            self.display_cal = ""
            self.input_text.set("0")

    def solve_quadratic_equation_step(self):
        if self.quadratic_step == 1:
            # Nhập a
            try:
                a = float(self.cal)
            except Exception:
                self.result_text.set("Hệ số a không hợp lệ!")
                self.cal = ""
                self.display_cal = ""
                self.input_text.set("")
                return
            self.quadratic_a = a
            self.quadratic_step = 2
            self.cal = ""
            self.display_cal = ""
            self.input_text.set("Nhập b rồi nhấn =")
        elif self.quadratic_step == 2:
            # Nhập b
            try:
                b = float(self.cal)
            except Exception:
                self.result_text.set("Hệ số b không hợp lệ!")
                self.cal = ""
                self.display_cal = ""
                self.input_text.set("")
                return
            self.quadratic_b = b
            self.quadratic_step = 3
            self.cal = ""
            self.display_cal = ""
            self.input_text.set("Nhập c rồi nhấn =")
        elif self.quadratic_step == 3:
            # Nhập c
            try:
                c = float(self.cal)
            except Exception:
                self.result_text.set("Hệ số c không hợp lệ!")
                self.cal = ""
                self.display_cal = ""
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
            self.cal = ""
            self.display_cal = ""
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

    def get_current_value(self):
        if self.just_calculated:
            return self.result_text.get().replace('=','').strip()
        elif self.display_cal:
            return self.display_cal
        else:
            return '0'

    def parse_int_value(self, value):
        value = value.strip()
        if value.startswith('0b'):
            return int(value, 2)
        elif value.startswith('0x'):
            return int(value, 16)
        elif value.startswith('0o'):
            return int(value, 8)
        else:
            return int(float(value))

# ===== Run chương trình =====
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()