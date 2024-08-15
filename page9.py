import tkinter as tk
from tkinter import ttk

def create_table(root):
    # Create a table frame
    table_frame = tk.Frame(root)
    table_frame.pack(fill=tk.BOTH, expand=True)

    # Create a Treeview widget
    table = ttk.Treeview(table_frame, columns=("Parameter", "Standard Minimum", "Score", "Standard Maximum"), show="headings")
    table.pack(fill=tk.BOTH, expand=True)

    # Define column headings
    table.heading("Parameter", text="Parameter")
    table.heading("Standard Minimum", text="Standard Minimum")
    table.heading("Score", text="Score")
    table.heading("Standard Maximum", text="Standard Maximum")

    # Insert data into the table
    table.insert("", tk.END, values=("Muscle Mass (Kg)", "", "", ""))
    table.insert("", tk.END, values=("Bone Mass (Kg)", "", "", ""))
    table.insert("", tk.END, values=("Moisture Content (Kg)", "", "", ""))
    table.insert("", tk.END, values=("Skeletal Muscle Mass (Kg)", "", "", ""))
    table.insert("", tk.END, values=("Body Cell Mass (Kg)", "", "", ""))
    table.insert("", tk.END, values=("Basal Metabolism (kCal)", "", "", ""))
    table.insert("", tk.END, values=("Waist to Hip Ratio", "", "", ""))
    table.insert("", tk.END, values=("Body Type", "", "Body Score", ""))
    table.insert("", tk.END, values=("Ideal Weight (Kg)", "", "Muscle Control (Kg)", ""))
    table.insert("", tk.END, values=("Target Weight (Kg)", "", "Fat Control (Kg)", ""))
    table.insert("", tk.END, values=("Weight Control (Kg)", "", "Recommended Intake (kCal)", ""))

    # Configure column widths
    table.column("Parameter", width=200, anchor=tk.W)
    table.column("Standard Minimum", width=200, anchor=tk.W)
    table.column("Score", width=200, anchor=tk.W)
    table.column("Standard Maximum", width=200, anchor=tk.W)

    # Set row height
    table.config(height=12)

    # Make the table resize with the window
    table_frame.bind("<Configure>", lambda event: table.configure(width=event.width, height=event.height))

# Create the main window
root = tk.Tk()
root.title("Table GUI")
root.geometry("1024x600")  # Set resolution to 1024x600

# Create the table
create_table(root)

# Start the main event loop
root.mainloop()