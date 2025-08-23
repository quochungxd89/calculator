import tkinter as tk
from tkinter import messagebox
from math import sin, cos, tan, log, sqrt, radians, pi, e, pow
import re

from logic.equations import solve_linear_equation, solve_quadratic_equation
from logic.utils import convert_deg_min_sec, parse_int_value
from ui.display import create_display
from ui.buttons import create_buttons

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Máy Tính Khoa Học")
        self.root.geometry("520x800")
        self.root.configure(bg="#0c5789")

        self.cal = ""          
        self.display_cal = ""  
        self.linear_mode = False
        self.linear_step = 0
        self.linear_a = None
        self.linear_b = None
        self.quadratic_mode = False
        self.quadratic_step = 0
        self.quadratic_a = None
        self.quadratic_b = None
        self.quadratic_c = None
        self.root_n_mode = False
        self.root_n_value = None
        self.just_calculated = False
        self.history = []

        self.input_text = tk.StringVar(value="0")
        self.result_text = tk.StringVar(value="= 0")

        create_display(self)
        create_buttons(self)

    def handle_button(self, char):
        if self.just_calculated:
            if char in '0123456789.':
                self.cal = ''
                self.display_cal = ''
                self.input_text.set('')
                self.just_calculated = False
            elif char in ['+', '-', 'x', '/']:
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
        elif char == 'x²':
            self.cal += '**2'
            self.display_cal += '²'
            self.input_text.set(self.display_cal)
        elif char == 'x³':
            self.cal += '**3'
            self.display_cal += '³'
            self.input_text.set(self.display_cal)
        elif char == 'xⁿ':
            self.cal += '**'
            self.display_cal += '^'
            self.input_text.set(self.display_cal)
        elif char == 'x10ⁿ':
            self.cal += '*10**'
            self.display_cal += 'x10ⁿ'
            self.input_text.set(self.display_cal)
        elif char == '√':
            self.cal += 'sqrt('
            self.display_cal += '√('
            self.input_text.set(self.display_cal)
        elif char == '³√':
            self.root_n_mode = True
            self.root_n_value = 3
            self.cal += 'pow('
            self.display_cal += '³√('
            self.input_text.set(self.display_cal)
        elif char == 'x⁻¹':
            self.cal += '**(-1)'
            self.display_cal += '⁻¹'
            self.input_text.set(self.display_cal)
        elif char == 'ⁿ√':
            match = re.search(r'(\d+)$', self.cal)
            if match:
                n = int(match.group(1))
                self.cal = self.cal[:-len(str(n))]
                self.display_cal = self.display_cal[:-len(str(n))]
                self.root_n_mode = True
                self.root_n_value = n
                self.cal += 'pow('
                self.display_cal += f'{ⁿ}√('
                self.input_text.set(self.display_cal)
            else:
                self.root_n_mode = True
                self.root_n_value = 2
                self.cal += 'pow('
                self.display_cal += '√('
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
        elif char in ['Bin', 'Dec', 'Hex', 'Oct']:
            value = self.get_current_value()
            try:
                int_value = parse_int_value(value)
                if char == 'Bin':
                    self.result_text.set('= ' + bin(int_value))
                elif char == 'Dec':
                    self.result_text.set('= ' + str(int_value))
                elif char == 'Hex':
                    self.result_text.set('= ' + hex(int_value))
                elif char == 'Oct':
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

    def reset_equation_mode(self):
        """Reset equation mode variables without clearing display"""
        self.cal = ""
        self.display_cal = ""
        self.linear_mode = False
        self.linear_step = 0
        self.linear_a = None
        self.linear_b = None
        self.quadratic_mode = False
        self.quadratic_step = 0
        self.quadratic_a = None
        self.quadratic_b = None
        self.quadratic_c = None
        self.just_calculated = True

    def delete_last(self):
        if self.cal.endswith("**2") and self.display_cal.endswith("^2"):
            self.cal = self.cal[:-3]
            self.display_cal = self.display_cal[:-2]
        elif self.cal.endswith("**3") and self.display_cal.endswith("^3"):
            self.cal = self.cal[:-3]
            self.display_cal = self.display_cal[:-2]
        elif self.cal.endswith("*10**") and self.display_cal.endswith("x10^"):
            self.cal = self.cal[:-5]
            self.display_cal = self.display_cal[:-4]
        else:
            self.cal = self.cal[:-1]
            self.display_cal = self.display_cal[:-1]
        self.input_text.set(self.display_cal if self.display_cal else "0")

    def calculate(self):
        try:
            expr = convert_deg_min_sec(self.cal)
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
            
            self.history.append((self.display_cal, str(result)))
            if hasattr(self, 'update_history_display'):
                self.update_history_display()
        except:
            messagebox.showerror("Lỗi", "Phép tính không hợp lệ!")
            self.clear_all()

    def solve_linear_equation_step(self):
        if self.linear_step == 1:
            try:
                a = float(self.cal)
            except:
                self.result_text.set("Hệ số a không hợp lệ!")
                self.cal = ""
                self.display_cal = ""
                return
            self.linear_a = a
            self.linear_step = 2
            self.cal = ""
            self.display_cal = ""
            self.input_text.set("Nhập b rồi nhấn =")
        elif self.linear_step == 2:
            try:
                b = float(self.cal)
            except:
                self.result_text.set("Hệ số b không hợp lệ!")
                self.cal = ""
                self.display_cal = ""
                return
            self.linear_b = b
            result = solve_linear_equation(self.linear_a, self.linear_b)
            self.result_text.set(result)
            
            equation_display = ""
            if self.linear_a == 1:
                equation_display += "x"
            elif self.linear_a == -1:
                equation_display += "-x"
            else:
                equation_display += f"{self.linear_a}x"
            
            if self.linear_b > 0:
                equation_display += f" + {self.linear_b}"
            elif self.linear_b < 0:
                equation_display += f" - {abs(self.linear_b)}"
            equation_display += " = 0"
            self.history.append((equation_display, result, "equation"))
            if hasattr(self, 'update_history_display'):
                self.update_history_display()
            
            self.reset_equation_mode()

    def solve_quadratic_equation_step(self):
        if self.quadratic_step == 1:
            try:
                a = float(self.cal)
            except:
                self.result_text.set("Hệ số a không hợp lệ!")
                self.cal = ""
                self.display_cal = ""
                return
            self.quadratic_a = a
            self.quadratic_step = 2
            self.cal = ""
            self.display_cal = ""
            self.input_text.set("Nhập b rồi nhấn =")
        elif self.quadratic_step == 2:
            try:
                b = float(self.cal)
            except:
                self.result_text.set("Hệ số b không hợp lệ!")
                self.cal = ""
                self.display_cal = ""
                return
            self.quadratic_b = b
            self.quadratic_step = 3
            self.cal = ""
            self.display_cal = ""
            self.input_text.set("Nhập c rồi nhấn =")
        elif self.quadratic_step == 3:
            try:
                c = float(self.cal)
            except:
                self.result_text.set("Hệ số c không hợp lệ!")
                self.cal = ""
                self.display_cal = ""
                return
            self.quadratic_c = c
            result = solve_quadratic_equation(self.quadratic_a, self.quadratic_b, self.quadratic_c)
            self.result_text.set(result)
            
            equation_display = ""
            if self.quadratic_a == 0:
              
                if self.quadratic_b == 1:
                    equation_display += "x"
                elif self.quadratic_b == -1:
                    equation_display += "-x"
                else:
                    equation_display += f"{self.quadratic_b}x"
                
                if self.quadratic_c > 0:
                    equation_display += f" + {self.quadratic_c}"
                elif self.quadratic_c < 0:
                    equation_display += f" - {abs(self.quadratic_c)}"
            else:
               
                if self.quadratic_a == 1:
                    equation_display += "x²"
                elif self.quadratic_a == -1:
                    equation_display += "-x²"
                else:
                    equation_display += f"{self.quadratic_a}x²"
                
                if self.quadratic_b != 0:
                    if self.quadratic_b > 0:
                        if self.quadratic_b == 1:
                            equation_display += " + x"
                        else:
                            equation_display += f" + {self.quadratic_b}x"
                    else:
                        if self.quadratic_b == -1:
                            equation_display += " - x"
                        else:
                            equation_display += f" - {abs(self.quadratic_b)}x"
                
                if self.quadratic_c != 0:
                    if self.quadratic_c > 0:
                        equation_display += f" + {self.quadratic_c}"
                    else:
                        equation_display += f" - {abs(self.quadratic_c)}"
            
            equation_display += " = 0"
            self.history.append((equation_display, result, "equation"))
            if hasattr(self, 'update_history_display'):
                self.update_history_display()
            
            self.reset_equation_mode()

    def get_current_value(self):
        if self.just_calculated:
            return self.result_text.get().replace('=','').strip()
        elif self.display_cal:
            return self.display_cal
        else:
            return '0'

    def get_history(self):
        return self.history