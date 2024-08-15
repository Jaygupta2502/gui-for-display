import tkinter as tk
from tkinter import ttk

def submit_data():
    # Get data from checkboxes
    medical_condition = [value for value in medical_values if medical_checkboxes[value].get() == 1]
    disabilities = [value for value in disabilities_values if disabilities_checkboxes[value].get() == 1]
    implants = [value for value in implants_values if implants_checkboxes[value].get() == 1]
    physical_activity = [value for value in physical_values if physical_checkboxes[value].get() == 1]
    water_intake = [value for value in water_values if water_checkboxes[value].get() == 1]
    alcohol_consumption = [value for value in alcohol_values if alcohol_checkboxes[value].get() == 1]
    smoking_cigaratte = [value for value in smoking_values if smoking_checkboxes[value].get() == 1]

    # Print data to the console (you can replace this with saving to a file, database, etc.)
    print("Medical Condition:", medical_condition)
    print("Disabilities:", disabilities)
    print("Implants:", implants)
    print("Physical Activity:", physical_activity)
    print("Water Intake:", water_intake)
    print("Alcohol Consumption:", alcohol_consumption)
    print("Smoking Cigaratte:", smoking_cigaratte)

# Create main window
root = tk.Tk()
root.title("Mandatory Information")

# Create labels and checkboxes
medical_label = tk.Label(root, text="Medical Condition - Treatment")
medical_label.grid(row=0, column=0, padx=10, pady=10)
medical_variable = tk.StringVar(root)
medical_variable.set("Select")  # Set initial value
medical_dropdown = ttk.Combobox(root, textvariable=medical_variable, values=["Option 1", "Option 2", "Option 3"])
medical_dropdown.grid(row=0, column=1, padx=10, pady=10)
def medical_checkboxes_undefined():
# Define possible values for checkboxes
    medical_values = ["Option 1", "Option 2", "Option 3"]
    medical_checkboxes = {}
    for i, value in enumerate(medical_values):
        medical_checkboxes[value] = tk.IntVar()
        medical_checkbox = tk.Checkbutton(root, text=value, variable=medical_checkboxes[value])
        medical_checkbox.grid(row=i+1, column=0, padx=10, pady=5, sticky='w')

# Create a separator
separator = ttk.Separator(root, orient='horizontal')
separator.grid(row=4, column=0, columnspan=2, sticky='ew', pady=10)

# Repeat for other categories
disabilities_label = tk.Label(root, text="Disabilities")
disabilities_label.grid(row=5, column=0, padx=10, pady=10)
disabilities_values = ["Option 1", "Option 2", "Option 3"]
disabilities_checkboxes = {}
for i, value in enumerate(disabilities_values):
    disabilities_checkboxes[value] = tk.IntVar()
    disabilities_checkbox = tk.Checkbutton(root, text=value, variable=disabilities_checkboxes[value])
    disabilities_checkbox.grid(row=i+6, column=0, padx=10, pady=5, sticky='w')

implants_label = tk.Label(root, text="Implants")
implants_label.grid(row=9, column=0, padx=10, pady=10)
implants_values = ["Option 1", "Option 2", "Option 3"]
implants_checkboxes = {}
for i, value in enumerate(implants_values):
    implants_checkboxes[value] = tk.IntVar()
    implants_checkbox = tk.Checkbutton(root, text=value, variable=implants_checkboxes[value])
    implants_checkbox.grid(row=i+10, column=0, padx=10, pady=5, sticky='w')

# Life style parameters
physical_label = tk.Label(root, text="Physical Activity")
physical_label.grid(row=13, column=0, padx=10, pady=10)
physical_values = ["Option 1", "Option 2", "Option 3"]
physical_checkboxes = {}
for i, value in enumerate(physical_values):
    physical_checkboxes[value] = tk.IntVar()
    physical_checkbox = tk.Checkbutton(root, text=value, variable=physical_checkboxes[value])
    physical_checkbox.grid(row=i+14, column=0, padx=10, pady=5, sticky='w')

water_label = tk.Label(root, text="Water Intake")
water_label.grid(row=17, column=0, padx=10, pady=10)
water_values = ["Option 1", "Option 2", "Option 3"]
water_checkboxes = {}
for i, value in enumerate(water_values):
    water_checkboxes[value] = tk.IntVar()
    water_checkbox = tk.Checkbutton(root, text=value, variable=water_checkboxes[value])
    water_checkbox.grid(row=i+18, column=0, padx=10, pady=5, sticky='w')

alcohol_label = tk.Label(root, text="Alcohol Consumption")
alcohol_label.grid(row=21, column=0, padx=10, pady=10)
alcohol_values = ["Option 1", "Option 2", "Option 3"]
alcohol_checkboxes = {}
for i, value in enumerate(alcohol_values):
    alcohol_checkboxes[value] = tk.IntVar()
    alcohol_checkbox = tk.Checkbutton(root, text=value, variable=alcohol_checkboxes[value])
    alcohol_checkbox.grid(row=i+22, column=0, padx=10, pady=5, sticky='w')

smoking_label = tk.Label(root, text="Smoking Cigaratte")
smoking_label.grid(row=25, column=0, padx=10, pady=10)
smoking_values = ["Option 1", "Option 2", "Option 3"]
smoking_checkboxes = {}
for i, value in enumerate(smoking_values):
    smoking_checkboxes[value] = tk.IntVar()
    smoking_checkbox = tk.Checkbutton(root, text=value, variable=smoking_checkboxes[value])
    smoking_checkbox.grid(row=i+26, column=0, padx=10, pady=5, sticky='w')

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=30, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()