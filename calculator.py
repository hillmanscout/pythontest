import tkinter as tk
from tkinter import ttk

total_bonus_base = 10000  # Base bonus if all targets are met
weights = {'A': 0.70, 'B': 0.15, 'C': 0.05, 'D': 0.10}  # Weights of each target

# Define Target A scale (3948 to 4450 units)
min_units_A = 3948
max_units_A = 4450

def calculate_bonus(units_A, percent_B, percent_C, percent_D):
    percent_A = max(0, (units_A - min_units_A) / (max_units_A - min_units_A))
    bonus_A = percent_A * weights['A'] * total_bonus_base
    if units_A > max_units_A:
        bonus_A += ((units_A - max_units_A) / max_units_A) * weights['A'] * total_bonus_base  # Scaling beyond 100%
    
    bonus_B = percent_B * weights['B'] * total_bonus_base
    bonus_C = percent_C * weights['C'] * total_bonus_base
    bonus_D = percent_D * weights['D'] * total_bonus_base
    
    total_earned_bonus = bonus_A + bonus_B + bonus_C + bonus_D
    return total_earned_bonus

def update_bonus(*args):
    units_A = units_A_var.get()
    percent_B = percent_B_var.get() / 100
    percent_C = percent_C_var.get() / 100
    percent_D = percent_D_var.get() / 100
    
    total_earned_bonus = calculate_bonus(units_A, percent_B, percent_C, percent_D)
    result_label.config(text=f"Total Bonus Earned: ${total_earned_bonus:.2f}")

# Create the main window
root = tk.Tk()
root.title("Bonus Calculator")
root.geometry("400x400")

# UI Elements
units_A_var = tk.IntVar(value=4000)
percent_B_var = tk.IntVar(value=50)
percent_C_var = tk.IntVar(value=50)
percent_D_var = tk.IntVar(value=50)

tk.Label(root, text="Units (Target A)").pack()
units_A_slider = tk.Scale(root, from_=min_units_A, to=max_units_A + 1000, orient="horizontal", variable=units_A_var, command=update_bonus)
units_A_slider.pack()

tk.Label(root, text="% Target B").pack()
percent_B_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", variable=percent_B_var, command=update_bonus)
percent_B_slider.pack()

tk.Label(root, text="% Target C").pack()
percent_C_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", variable=percent_C_var, command=update_bonus)
percent_C_slider.pack()

tk.Label(root, text="% Target D").pack()
percent_D_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", variable=percent_D_var, command=update_bonus)
percent_D_slider.pack()

# Result Label
result_label = tk.Label(root, text="Total Bonus Earned: $0.00", font=("Arial", 14))
result_label.pack(pady=20)

# Run the application
update_bonus()
root.mainloop()
