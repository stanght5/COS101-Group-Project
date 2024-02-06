import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI is: {bmi:.2f}")
        interpretation_label.config(text=f"Interpretation: {interpret_bmi(bmi)}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values.")

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


window = tk.Tk()
window.title("BMI Calculator")


weight_label = tk.Label(window, text="Enter Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)

weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = tk.Label(window, text="Enter Height (m):")
height_label.grid(row=1, column=0, padx=10, pady=10)

height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

interpretation_label = tk.Label(window, text="")
interpretation_label.grid(row=4, column=0, columnspan=2, pady=10)
window.mainloop()
