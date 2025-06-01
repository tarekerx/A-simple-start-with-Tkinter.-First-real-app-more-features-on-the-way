import tkinter as tk
from tkinter import messagebox  # For showing error dialogs

# Function to convert centimeters to meters
def convert_cm_to_meters():
    try:
        # Get input from entry, convert to float and calculate meters
        cm = float(entry.get())
        result_var.set(f"{cm / 100:.2f} m")  # Format to 2 decimal places
    except ValueError:
        # Show error if input is not a valid number
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        result_var.set("Invalid")

# Create the main application window
window = tk.Tk()
window.title("CM to Meters Converter")     # Window title
window.geometry("250x150")                 # Set fixed size
window.resizable(False, False)             # Disable resizing

# Variable to hold the conversion result
result_var = tk.StringVar(value="0.00 m")

# Entry widget for user input (centimeters)
entry = tk.Entry(window, width=10)
entry.insert(0, "0")  # Default value
entry.pack(pady=10)

# Button to perform the conversion
convert_button = tk.Button(window, text="Convert to meters", command=convert_cm_to_meters)
convert_button.pack()

# Label to display the result
result_label = tk.Label(window, textvariable=result_var, font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
