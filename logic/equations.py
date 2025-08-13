from math import sqrt

def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Vô số nghiệm"
        else:
            return "Vô nghiệm"
    return f"x = {-b / a}"

def solve_quadratic_equation(a, b, c):
    if a == 0:
        return solve_linear_equation(b, c)
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