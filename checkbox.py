import tkinter as tk
from tkinter import ttk

def show_selected():
    selected_items = [
        item.get()
        for item in checkboxes
        if item.get()
    ]
    print(f"Selected items: {selected_items}")

root = tk.Tk()
root.title("Multiple Choice Dropdown with Checkbox")

# Create a list of parameters for the dropdown
parameters = [
    "None",
    "Do Not Want To Declare",
    "Type 1 Diabetes",
    "Type 2 Diabities",
    "High Cholestrol",
    "High Blood Pressure",
    "Cancer Treatment",
    "Blood Treatment",
    "Heart Treatment",
    "Lung Treatment",
    "Kidney Treatment",
    "Liver Treatment",
    "Other Major Surgery",
    "Others",
    "Pregnancy",
    "Post Pregnancy (<6 months)"
]

# Create a list to store the checkboxes
checkboxes = []

# Create a frame to hold the checkboxes
checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=10)

# Create a dropdown for selecting the parameter category
category_dropdown = ttk.Combobox(root, values=["Medical"], state="readonly")
category_dropdown.pack(pady=10)

# Create a function to update the checkboxes based on the selected category
def update_checkboxes(event):
    # Clear existing checkboxes


    # Get the selected category
    selected_category = category_dropdown.get()

    # Filter the parameters based on the selected category
    filtered_parameters = [
        param
        for param in parameters
        if (selected_category == "Medical" and not param.endswith("(<6 months)"))
        or (selected_category == "Other" and param.endswith("(<6 months)"))
    ]

    # Create a checkbox for each filtered parameter
    for i, param in enumerate(filtered_parameters):
        checkbox_var = tk.BooleanVar(value=False)
        checkboxes.append(checkbox_var)
        checkbox = tk.Checkbutton(
            checkbox_frame,
            text=param,
            variable=checkbox_var,
            onvalue=True,
            offvalue=False
        )
        checkbox.grid(row=i, column=0, sticky="w")

# Bind the update_checkboxes function to the dropdown's selection event
#category_dropdown.bind("<<ComboboxSelected>>", update_checkboxes)

# Call the update_checkboxes function initially to set the default checkboxes
update_checkboxes(None)

# Create a button to show the selected items
show_button = tk.Button(root, text="Show Selected", command=show_selected)
show_button.pack(pady=10)

root.mainloop()