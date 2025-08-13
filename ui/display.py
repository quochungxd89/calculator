import tkinter as tk

def create_display(calc):
    display_frame = tk.Frame(calc.root, height=100, bg="white")
    display_frame.pack(fill="both", padx=10, pady=10)

    input_label = tk.Label(display_frame, textvariable=calc.input_text,
                           font=("Arial", 20), anchor="e", bg="white", fg="black")
    input_label.pack(expand=True, fill="both")

    result_label = tk.Label(display_frame, textvariable=calc.result_text,
                            font=("Arial", 16), anchor="e", bg="white", fg="gray")
    result_label.pack(expand=True, fill="both")