import tkinter as tk

def create_buttons(calc):
    btn_frame = tk.Frame(calc.root, bg="#0c5789")
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
                            command=lambda ch=char: calc.handle_button(ch))
            btn.grid(row=r, column=c, padx=5, pady=5)