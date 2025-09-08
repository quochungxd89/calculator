import tkinter as tk

def create_buttons(calc):
    btn_frame = tk.Frame(calc.root, bg="#0c5789")
    btn_frame.pack()

    buttons = [
        ['(', ')', 'AC', 'Del', 'x10ⁿ'],
        ['sin', 'cos', 'tan', 'cotan', 'log'],
        ['√', '³√', 'ⁿ√', 'PT bậc 1','PT bậc 2'],
        ['Bin', 'Dec', 'Hex', 'Oct', "'"],
        ['7', '8', '9', '+', 'x²'],
        ['4', '5', '6', '-', 'x³'],
        ['1', '2', '3', 'x', 'xⁿ'],
        ['0', '.', '=', '/', 'x⁻¹'],
    ]

    for r, row in enumerate(buttons):
        for c, char in enumerate(row):
            if char == '':
                continue
            btn = tk.Button(btn_frame, text=char, width=6, height=2,
                            font=("Arial", 14), fg="black", bg="white",
                            command=lambda ch=char: calc.handle_button(ch))
            btn.grid(row=r, column=c, padx=5, pady=5)