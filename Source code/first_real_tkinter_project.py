import tkinter as tk
from tkinter import messagebox

# Conversion logic
def convert_units(option):
    try:
        value = float(entry.get())
        if option == "Kilometers to Meters":
            result = value * 1000
            result_var.set(f"{result:.2f} m")
        elif option == "Meters to Centimeters":
            result = value * 100
            result_var.set(f"{result:.2f} cm")
        elif option == "Inches to Centimeters":
            result = value * 2.54
            result_var.set(f"{result:.2f} cm")
        elif option == "Feet to Meters":
            result = value * 0.3048
            result_var.set(f"{result:.2f} m")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        result_var.set("Invalid")

# Hover animations
def on_enter_button(event):
    convert_button.config(bg="#45a049", relief="raised")
def on_leave_button(event):
    convert_button.config(bg="#4CAF50", relief="flat")
def on_entry_focus_in(event):
    entry.config(bg="#e0f7fa")
def on_entry_focus_out(event):
    entry.config(bg="white")

# Main window
window = tk.Tk()
window.title("📏 Unit Converter")
window.geometry("360x300")
window.configure(bg="#f5f5f5")
window.resizable(False, False)

# Title
title_label = tk.Label(window, text="Unit Converter", font=("Helvetica", 16, "bold"), fg="#333", bg="#f5f5f5")
title_label.pack(pady=(20, 10))

# Input label
entry_label = tk.Label(window, text="Enter value:", font=("Helvetica", 12), bg="#f5f5f5")
entry_label.pack()

# Input field
entry = tk.Entry(window, font=("Helvetica", 12), width=20, justify="center")
entry.insert(0, "0")
entry.pack(pady=5)
entry.bind("<FocusIn>", on_entry_focus_in)
entry.bind("<FocusOut>", on_entry_focus_out)

# Dropdown
options = [
    "Kilometers to Meters",
    "Meters to Centimeters",
    "Inches to Centimeters",
    "Feet to Meters"
]
selected_option = tk.StringVar(value=options[0])
dropdown = tk.OptionMenu(window, selected_option, *options)
dropdown.config(font=("Helvetica", 11), width=25)
dropdown.pack(pady=10)

# Convert button
convert_button = tk.Button(
    window, text="Convert", font=("Helvetica", 12, "bold"),
    bg="#4CAF50", fg="white", width=20,
    activebackground="#66bb6a", activeforeground="white",
    relief="flat",
    command=lambda: convert_units(selected_option.get())
)
convert_button.pack(pady=10)
convert_button.bind("<Enter>", on_enter_button)
convert_button.bind("<Leave>", on_leave_button)

# Result label
result_var = tk.StringVar(value="0.00")
result_label = tk.Label(window, textvariable=result_var, font=("Helvetica", 14, "bold"), fg="#007ACC", bg="#f5f5f5")
result_label.pack(pady=15)

# Run app
window.mainloop()
