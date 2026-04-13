import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())

        if gallons <= 0:
            messagebox.showerror("Error", "Gallons must be greater than 0.")
            return

        mpg = miles / gallons
        result_label.config(text=f"MPG: {mpg:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Gas Mileage Calculator")
root.geometry("300x200")

tk.Label(root, text="Gallons:").pack(pady=5)
gallons_entry = tk.Entry(root)
gallons_entry.pack(pady=5)

tk.Label(root, text="Miles:").pack(pady=5)
miles_entry = tk.Entry(root)
miles_entry.pack(pady=5)

tk.Button(root, text="Calculate MPG", command=calculate_mpg).pack(pady=10)

result_label = tk.Label(root, text="MPG: ")
result_label.pack(pady=5)

root.mainloop()
