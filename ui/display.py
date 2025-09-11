import tkinter as tk

def create_display(calc):
    display_frame = tk.Frame(calc.root, height=100, bg="white")
    display_frame.pack(fill="both", padx=10, pady=10)

    input_label = tk.Label(display_frame, textvariable=calc.input_text,
                           font=("Arial", 20), anchor="e", bg="white", fg="black",
                           pady=5)
    input_label.pack(expand=True, fill="both")

    result_label = tk.Label(display_frame, textvariable=calc.result_text,
                            font=("Arial", 16), anchor="e", bg="white", fg="gray")
    result_label.pack(expand=True, fill="both")

    history_label = tk.Label(display_frame, text="Lịch sử phép tính:", font=("Arial", 12), anchor="w", bg="white", fg="#0c5789")
    history_label.pack(fill="x")
    calc.history_listbox = tk.Listbox(display_frame, height=5, font=("Arial", 12), bg="#f0f0f0")
    calc.history_listbox.pack(fill="both", padx=5, pady=5)

    def update_history_display():
        calc.history_listbox.delete(0, tk.END)
        for item in calc.get_history()[-10:]:
            if len(item) == 3: 
                expr, result, item_type = item
                calc.history_listbox.insert(tk.END, f"{expr} => {result}")
            else: 
                expr, result = item
                calc.history_listbox.insert(tk.END, f"{expr} = {result}")
    calc.update_history_display = update_history_display