import tkinter as tk
from tkinter import ttk
import json

class BodyCompositionApp:
    def __init__(self, master):
        self.master = master
        master.title("Body Composition Analysis")
        master.geometry("1024x600")

        
        try:
            with open("output.json", "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}  

        
        self.create_widgets()

    def create_widgets(self):
        
        left_frame = tk.Frame(self.master)
        left_frame.pack(side=tk.LEFT, padx=20, pady=20)

        labels = [
            "Name",
            "Age",
            "Height (cms)",
            "BMI",
            "Visceral Fat Level",
            "Heart Rate",
            "Physical Age (Yrs)",
            "Intracellular Water (Kg)",
            "Total Body Water (Kg)",
            "Protein Mass (Kg)",
            "InOrganic Salt (Kg)",
            "Body Fat Mass (Kg)",
        ]

        for i, label in enumerate(labels):
            label_widget = tk.Label(left_frame, text=label)
            label_widget.grid(row=i, column=0, sticky="w")

        
        right_frame = tk.Frame(self.master)
        right_frame.pack(side=tk.LEFT, padx=20, pady=20)

        
        self.entry_widgets = {}
        for i, key in enumerate(self.data.keys()):
            if key in ["Name", "Age", "Height (cms)"]:
                entry = ttk.Entry(right_frame)
            else:
                entry = ttk.Entry(right_frame, state="readonly")
            entry.grid(row=i, column=0, padx=5, pady=5)
            self.entry_widgets[key] = entry

        
        self.update_entries()

        
        save_button = tk.Button(right_frame, text="Save", command=self.save_data)
        save_button.grid(row=len(self.data) + 1, column=0, pady=10)

    def update_entries(self):
        for key, value in self.data.items():
            if key in self.entry_widgets:
                self.entry_widgets[key].config(state="normal")
                self.entry_widgets[key].delete(0, tk.END)
                self.entry_widgets[key].insert(0, value)
                self.entry_widgets[key].config(state="readonly")

    def save_data(self):
        for key, entry in self.entry_widgets.items():
            if key not in ["Name", "Age", "Height (cms)"]:
                continue
            self.data[key] = entry.get()
        with open("body_composition_data.json", "w") as f:
            json.dump(self.data, f)

root = tk.Tk()
app = BodyCompositionApp(root)
root.mainloop()