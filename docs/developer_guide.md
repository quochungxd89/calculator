# 👨‍💻 HƯỚNG DẪN PHÁT TRIỂN - CALCULATOR

## 🎯 GIỚI THIỆU

Tài liệu này dành cho developers muốn hiểu, bảo trì, và mở rộng dự án Calculator. Bao gồm cấu trúc code, coding standards, và hướng dẫn thêm tính năng mới.

## 🏗️ CÀI ĐẶT MÔI TRƯỜNG PHÁT TRIỂN

### Yêu Cầu Hệ Thống
```bash
Python 3.7+
tkinter (built-in with Python)
math module (built-in)
re module (built-in)
```

### Setup Development Environment
```bash
# 1. Clone repository  
git clone <repository_url>
cd calculator

# 2. Tạo virtual environment (optional)
python -m venv calculator_env
source calculator_env/bin/activate  # Linux/Mac
# calculator_env\Scripts\activate   # Windows

# 3. Verify installation
python main.py
```

### IDE Recommendations
- **VS Code**: với Python extension
- **PyCharm**: Professional hoặc Community
- **Sublime Text**: với Python packages

## 📁 KIẾN TRÚC DỰ ÁN CHI TIẾT

### Directory Structure
```
calculator/
├── main.py                 # Entry point
├── logic/                  # Business logic layer
│   ├── __init__.py        # Package initializer
│   ├── calculator.py      # Main calculator class (Controller)
│   ├── equations.py       # Equation solving (Model)  
│   └── utils.py           # Utility functions (Model)
├── ui/                     # User interface layer
│   ├── __init__.py        # Package initializer
│   ├── display.py         # Display components (View)
│   └── buttons.py         # Button layout (View)
├── docs/                   # Documentation
│   ├── technical_docs.md
│   ├── user_manual.md
│   ├── developer_guide.md
│   └── project_report.md
└── README.md              # Project overview
```

### Code Organization Principles
- **Separation of Concerns**: Logic, UI, và utilities tách biệt
- **Modular Design**: Mỗi module có responsibility rõ ràng
- **Single Responsibility**: Mỗi function/class có 1 mục đích
- **DRY Principle**: Không lặp lại code

## 🔍 DEEP DIVE VÀO CODE

### 1. Main Controller (`logic/calculator.py`)

#### Class Calculator - Core Architecture
```python
class Calculator:
    def __init__(self, root):
        # UI State Management
        self.cal = ""              # Internal calculation string
        self.display_cal = ""      # User-friendly display string
        
        # Mode Management  
        self.linear_mode = False   # Linear equation mode
        self.quadratic_mode = False # Quadratic equation mode
        self.root_n_mode = False   # nth root calculation mode
        
        # History & State
        self.history = []          # Calculation history
        self.just_calculated = False # Post-calculation state
```

#### Key Methods Analysis

**`handle_button(char)` - Event Router**
```python
def handle_button(self, char):
    # Post-calculation behavior management
    if self.just_calculated:
        if char in '0123456789.':
            self.clear_for_new_input()
        elif char in ['+', '-', 'x', '/']:
            self.continue_with_result()
    
    # Route to appropriate handler
    if char == 'AC': self.clear_all()
    elif char == '=': self.process_equals()
    elif char in ['x²', 'x³']: self.handle_powers()
    # ... more routing logic
```

**`calculate()` - Safe Expression Evaluation**
```python
def calculate(self):
    try:
        # Convert degree-minute-second format
        expr = convert_deg_min_sec(self.cal)
        
        # Safe evaluation with restricted context
        result = eval(expr, {"__builtins__": None}, {
            "sin": lambda x: sin(radians(x)),
            "cos": lambda x: cos(radians(x)),
            # ... safe functions only
        })
        
        # Update UI and history
        self.result_text.set("= " + str(result))
        self.history.append((self.display_cal, str(result)))
        
    except Exception:
        self.show_error("Phép tính không hợp lệ!")
```

### 2. Equation Solver (`logic/equations.py`)

#### Linear Equation Solver
```python
def solve_linear_equation(a, b):
    """
    Solve ax + b = 0
    
    Returns:
        str: Solution description
        
    Edge cases:
        - a=0, b=0: Infinite solutions  
        - a=0, b≠0: No solution
        - a≠0: x = -b/a
    """
    if a == 0:
        return "Vô số nghiệm" if b == 0 else "Vô nghiệm"
    return f"x = {-b / a}"
```

#### Quadratic Equation Solver
```python
def solve_quadratic_equation(a, b, c):
    """
    Solve ax² + bx + c = 0 using discriminant method
    
    Algorithm:
        1. Calculate Δ = b² - 4ac
        2. If Δ > 0: Two distinct real roots
        3. If Δ = 0: One repeated real root  
        4. If Δ < 0: No real roots
    """
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
```

### 3. Utility Functions (`logic/utils.py`)

#### Degree-Minute-Second Converter
```python
def convert_deg_min_sec(expr):
    """
    Convert degree'minute'second' format to decimal degrees
    
    Example: sin(30'45'30') → sin(30 + 45/60 + 30/3600)
    
    Uses regex to find and replace DMS patterns in trig functions
    """
    def repl(m):
        deg = float(m.group(1)) if m.group(1) else 0
        minute = float(m.group(2)) if m.group(2) else 0  
        second = float(m.group(3)) if m.group(3) else 0
        return f"({deg} + {minute}/60 + {second}/3600)"
    
    # Apply to all trig functions
    for trig in ['sin', 'cos', 'tan', 'cotan']:
        pattern = fr"{trig}\(([0-9]+(?:\.[0-9]+)?)(?:'([0-9]+(?:\.[0-9]+)?))?(?:'([0-9]+(?:\.[0-9]+)?))?'?\)"
        expr = re.sub(pattern, lambda m: f"{trig}{repl(m)}", expr)
    
    return expr
```

## 🔧 ADDING NEW FEATURES

### 1. Adding New Mathematical Functions

#### Step 1: Add to Safe Context
```python
# In calculator.py calculate() method
safe_context = {
    "sin": lambda x: sin(radians(x)),
    "cos": lambda x: cos(radians(x)),
    # ADD NEW FUNCTION HERE
    "sinh": lambda x: sinh(x),  # Example: hyperbolic sine
    "factorial": lambda x: factorial(int(x)),
}
```

#### Step 2: Add Button
```python
# In ui/buttons.py
buttons = [
    ['(', ')', 'AC', 'Del', 'x10^n'],
    ['sin', 'cos', 'tan', 'sinh', 'log'],  # Add 'sinh' button
    # ... rest of layout
]
```

#### Step 3: Handle Button Event
```python
# In calculator.py handle_button() method
elif char in ['sin', 'cos', 'tan', 'sinh', 'cotan', 'log']:
    self.cal += f"{char}("
    self.display_cal += f"{char}("
```

### 2. Adding New Equation Types

#### Example: Cubic Equation Solver

**Step 1: Create Solver Function**
```python
# In logic/equations.py
def solve_cubic_equation(a, b, c, d):
    """Solve ax³ + bx² + cx + d = 0"""
    # Implement cubic formula or numerical method
    # Return formatted solution string
    pass
```

**Step 2: Add Mode Variables**
```python
# In calculator.py __init__()
self.cubic_mode = False
self.cubic_step = 0
self.cubic_coeffs = [None, None, None, None]
```

**Step 3: Add Button and Handler**
```python
# Add 'PT bậc 3' button and handle in handle_button()
elif char == 'PT bậc 3':
    self.cubic_mode = True
    self.cubic_step = 1
    # ... setup cubic input mode
```

### 3. Adding Memory Functions

#### Implementation Example
```python
# Add to calculator.py
class Calculator:
    def __init__(self, root):
        # ... existing init code ...
        self.memory = 0  # Memory storage
        
    def memory_store(self):
        """Store current result in memory"""
        if self.just_calculated:
            try:
                self.memory = float(self.result_text.get().replace('=','').strip())
            except ValueError:
                pass
                
    def memory_recall(self):
        """Recall value from memory"""  
        self.cal = str(self.memory)
        self.display_cal = str(self.memory)
        self.input_text.set(self.display_cal)
```

### 4. Adding Themes/Customization

#### Color Theme System
```python
# Create themes.py
THEMES = {
    'dark': {
        'bg': '#2b2b2b',
        'fg': '#ffffff', 
        'button_bg': '#404040',
        'button_fg': '#ffffff'
    },
    'light': {
        'bg': '#ffffff',
        'fg': '#000000',
        'button_bg': '#f0f0f0', 
        'button_fg': '#000000'
    }
}

# Modify calculator.py to accept theme
class Calculator:
    def __init__(self, root, theme='light'):
        self.theme = THEMES[theme]
        # Apply theme colors to all UI elements
```

## 🧪 TESTING STRATEGY

### 1. Unit Testing Framework
```python
# tests/test_equations.py
import unittest
from logic.equations import solve_linear_equation, solve_quadratic_equation

class TestEquations(unittest.TestCase):
    def test_linear_normal_case(self):
        result = solve_linear_equation(2, 4)
        self.assertEqual(result, "x = -2.0")
        
    def test_linear_zero_coefficient(self):
        result = solve_linear_equation(0, 0)
        self.assertEqual(result, "Vô số nghiệm")
        
    def test_quadratic_two_roots(self):
        result = solve_quadratic_equation(1, -5, 6)
        # Test for presence of both roots
        self.assertIn("x₁", result)
        self.assertIn("x₂", result)

if __name__ == '__main__':
    unittest.main()
```

### 2. Integration Testing
```python
# tests/test_calculator.py  
import unittest
from unittest.mock import Mock
from logic.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Mock tkinter root
        self.mock_root = Mock()
        self.calc = Calculator(self.mock_root)
        
    def test_basic_calculation(self):
        self.calc.handle_button('5')
        self.calc.handle_button('+')
        self.calc.handle_button('3')
        self.calc.handle_button('=')
        
        result = self.calc.result_text.get()
        self.assertEqual(result, "= 8")
```

### 3. Manual Testing Checklist
- [ ] All buttons respond correctly
- [ ] Mathematical functions produce correct results  
- [ ] Equation solvers handle all edge cases
- [ ] Number base conversions work properly
- [ ] History displays and updates correctly
- [ ] Error handling shows appropriate messages
- [ ] UI remains responsive during calculations

## 📊 PERFORMANCE OPTIMIZATION

### 1. Memory Management
```python
# Limit history size to prevent memory leaks
def add_to_history(self, calculation, result):
    self.history.append((calculation, result))
    if len(self.history) > 50:  # Keep only last 50 items
        self.history = self.history[-10:]  # Show only last 10
```

### 2. Calculation Optimization
```python
# Cache complex calculations
from functools import lru_cache

@lru_cache(maxsize=100)
def expensive_function(x):
    # Complex mathematical operation
    return result
```

### 3. UI Performance
```python
# Update UI efficiently
def batch_ui_update(self):
    """Update multiple UI elements at once"""
    self.root.update_idletasks()  # Process only essential updates
```

## 🐛 DEBUGGING TECHNIQUES

### 1. Add Debug Mode
```python
class Calculator:
    def __init__(self, root, debug=False):
        self.debug = debug
        
    def debug_print(self, message):
        if self.debug:
            print(f"DEBUG: {message}")
            
    def handle_button(self, char):
        self.debug_print(f"Button pressed: {char}")
        self.debug_print(f"Current cal: {self.cal}")
        # ... existing logic
```

### 2. Error Logging
```python
import logging

# Setup logging
logging.basicConfig(
    filename='calculator.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate(self):
    try:
        # ... calculation logic
    except Exception as e:
        logging.error(f"Calculation error: {e}")
        logging.error(f"Expression: {self.cal}")
        # ... error handling
```

## 📋 CODING STANDARDS

### 1. Python Style Guide (PEP 8)
- **Line Length**: Maximum 79 characters
- **Indentation**: 4 spaces (no tabs)
- **Naming**: snake_case for variables/functions, PascalCase for classes
- **Comments**: Docstrings for all functions/classes

### 2. Documentation Standards
```python
def solve_quadratic_equation(a, b, c):
    """
    Solve quadratic equation ax² + bx + c = 0
    
    Args:
        a (float): Coefficient of x²
        b (float): Coefficient of x
        c (float): Constant term
        
    Returns:
        str: Formatted solution description
        
    Raises:
        None: All errors handled internally
        
    Example:
        >>> solve_quadratic_equation(1, -5, 6)
        'x₁ = 3.0, x₂ = 2.0'
    """
```

### 3. Error Handling Standards
```python
def safe_operation(self, operation):
    """
    Standard pattern for safe operations
    """
    try:
        return operation()
    except ValueError as e:
        self.show_error(f"Invalid input: {e}")
        return None
    except ZeroDivisionError:
        self.show_error("Cannot divide by zero")
        return None
    except Exception as e:
        self.show_error("Unexpected error occurred")
        logging.error(f"Unexpected error: {e}")
        return None
```

## 🚀 DEPLOYMENT & DISTRIBUTION

### 1. Creating Executable
```bash
# Install PyInstaller
pip install pyinstaller

# Create standalone executable
pyinstaller --onefile --windowed main.py

# Create with icon and name
pyinstaller --onefile --windowed --icon=icon.ico --name="Calculator" main.py
```

### 2. Package Structure for Distribution
```
calculator-v1.0/
├── calculator.exe       # Executable (Windows)
├── calculator          # Executable (Linux/Mac)
├── README.md           # User documentation
├── LICENSE             # License file
└── docs/               # Complete documentation
    ├── user_manual.md
    └── technical_docs.md
```

### 3. Version Control Best Practices
```bash
# Git workflow
git checkout -b feature/new-function
# ... make changes ...
git add .
git commit -m "feat: add hyperbolic functions"
git push origin feature/new-function
# ... create pull request ...
```

## 🔄 MAINTENANCE TASKS

### Regular Maintenance Checklist
- [ ] **Code Review**: Check for code smells and refactoring opportunities
- [ ] **Dependency Update**: Keep Python and libraries up to date
- [ ] **Performance Review**: Profile and optimize slow operations  
- [ ] **Security Audit**: Review eval() usage and input validation
- [ ] **Documentation Update**: Keep docs synchronized with code changes
- [ ] **Bug Tracking**: Maintain issue list and prioritize fixes
- [ ] **User Feedback**: Collect and analyze user experience feedback

### Refactoring Opportunities
1. **Extract Complex Methods**: Break down large functions
2. **Create Configuration System**: Externalize settings
3. **Implement Plugin Architecture**: Allow easy feature additions
4. **Add Comprehensive Testing**: Increase code coverage
5. **Improve Error Messages**: Make them more user-friendly

---

## 💡 ADVANCED FEATURES TO CONSIDER

### 1. Scientific Computing Extensions
- **Matrix Operations**: Add matrix calculator
- **Calculus Functions**: Derivatives and integrals
- **Statistical Functions**: Mean, median, standard deviation
- **Unit Conversions**: Length, weight, temperature

### 2. User Experience Enhancements
- **Keyboard Shortcuts**: Full keyboard support
- **Expression History**: Save/load calculation sessions
- **Graph Plotting**: Visualize functions
- **Dark Mode**: Theme system implementation

### 3. Technical Improvements  
- **Plugin System**: Modular feature architecture
- **Configuration File**: User preferences storage
- **Localization**: Multi-language support
- **Cloud Sync**: Save calculations online

---

*Tài liệu này cung cấp foundation solid để phát triển và mở rộng Calculator project. Follow coding standards và best practices để maintain code quality cao.*
