import tkinter as tk

# Define a dictionary with MET (Metabolic Equivalent of Task) values for different exercises
exercise_met_values = {
    "Treadmill Running": 7.0,
    "Calisthenics": 5.0,
    "Weightlifting": 3.0,
}

def calculate_calories_burned():
    exercise = exercise_var.get()
    duration = float(entry_duration.get())
    weight = float(entry_weight.get())
    height = float(entry_height.get())
    age = float(entry_age.get())
    bmi = (weight / ((height / 100) ** 2))

    if exercise in exercise_met_values:
        met = exercise_met_values[exercise]
        # Calculate BMR (Basal Metabolic Rate) using the Harris-Benedict equation
        bmr = 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age)
        # Calculate calories burned using the MET value
        calories_burned = (met * bmr * duration) / 1440  # 1440 minutes in a day

        weight_status = get_weight_status(bmi)
        result_var.set(f"Calories Burned: {calories_burned:.2f} kcal\nBMI: {bmi:.2f}\nWeight Status: {weight_status}")
    else:
        result_var.set("Invalid exercise selected.")

def get_weight_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25.0 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

app = tk.Tk()
app.title("Calories Burned Calculator with BMI and Weight Status")

exercise_var = tk.StringVar()
exercise_var.set("Treadmill Running")

label_exercise = tk.Label(app, text="Select Exercise:")
label_exercise.pack()

exercise_options = list(exercise_met_values.keys())
exercise_menu = tk.OptionMenu(app, exercise_var, *exercise_options)
exercise_menu.pack()

label_duration = tk.Label(app, text="Duration (minutes):")
label_duration.pack()

entry_duration = tk.Entry(app)
entry_duration.pack()

label_weight = tk.Label(app, text="Weight (kg):")
label_weight.pack()

entry_weight = tk.Entry(app)
entry_weight.pack()

label_height = tk.Label(app, text="Height (cm):")
label_height.pack()

entry_height = tk.Entry(app)
entry_height.pack()

label_age = tk.Label(app, text="Age:")
label_age.pack()

entry_age = tk.Entry(app)
entry_age.pack()

calculate_button = tk.Button(app, text="Calculate Calories", command=calculate_calories_burned)
calculate_button.pack()

result_var = tk.StringVar()
result_label = tk.Label(app, textvariable=result_var)
result_label.pack()

app.mainloop()
