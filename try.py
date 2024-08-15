import tkinter as tk
from tkinter import ttk
import pandas as pd

# Create the main window
window = tk.Tk()
window.title("Welcome")
window.geometry("1024x600")  # Set the resolution

welcome_label = ttk.Label(window, text="WELCOME", font=("Arial", 30))
welcome_label.place(x=420, y=0)

# Create the description label
description_label = ttk.Label(window, text="Login to initiate your measurements", font=("Arial", 23))
description_label.place(x=300, y=48)

# Login Button
login_button = tk.Button(window, text="LOGIN", command=lambda: show_measurements_frame(), font=("Arial", 18), bg="white", fg="black")
login_button.place(x=475, y=100)

# Create a frame for measurements
measurements_frame = tk.Frame(window)
measurements_frame.place(x=0, y=0, width=1024, height=600)
measurements_frame.pack_propagate(False)  # Prevent frame from resizing

# Hide the measurements frame initially
measurements_frame.pack_forget()

# Function to show the measurements frame
def show_measurements_frame():
    login_button.pack_forget()
    measurements_frame.pack()

# Function to create the measurements table
def create_measurements_table():
    # Define your data (replace with actual data)
    data = {
        "Parameter": [
            "Muscle Mass (Kg)",
            "Bone Mass (Kg)",
            "Moisture Content (Kg)",
            "Skeletal Muscle Mass (Kg)",
            "Body Cell Mass (Kg)",
            "Basal Metabolism (kCal)",
            "Waist to Hip Ratio",
            "Body Type",
            "Ideal Weight (Kg)",
            "Target Weight (Kg)",
            "Weight Control (Kg)"
        ],
        "Standard Minimum": [None] * 11,
        "Score": [None] * 11,
        "Standard Maximum": [None] * 11
    }

    df = pd.DataFrame(data)

    # Create a Treeview widget
    tree = ttk.Treeview(measurements_frame, columns=df.columns, show="headings")
    
    # Set column headings
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, stretch=True)

    # Insert data into the Treeview
    for index, row in df.iterrows():
        tree.insert("", 'end', values=list(row))
    
    tree.place(x=0, y=0, width=1024, height=600)

# Call the function to create the table
create_measurements_table()

window.mainloop()  # Start the GUI event loop