import tkinter as tk
from tkinter import messagebox

class Page6:
    def __init__(self):
# Create the main window
        self.root = tk.Tk()
        self.root.title("Pulse Oximeter & Heart Rate")
        self.root.geometry("1024x600")
        self.root.configure(bg="#BEBEBE")  # Set background color

        self.mandatory_label = tk.Label(self.root, text="Pulse Oximeter & Heart Rate", font=("Arial", 20, "bold"), bg="#BEBEBE")
        self.mandatory_label.place(x=360,y=50)
# Create the height input
        self.SpO2_label = tk.Label(
            self.root,
            text="SpO2",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.SpO2_label.place(x=340,y=150)

        self.SpO2_entry = tk.Entry(
            self.root,
            width=14,
            font=("Calibri", 24),
            bg="white",
            fg="black",
            borderwidth=0,
            relief="solid",
        )
        self.SpO2_entry.place(x=420,y=140)

        self.Percentage_label = tk.Label(
            self.root,
            text="%",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.Percentage_label.place(x=695,y=145)

        # Create the height input
        self.Heart_label = tk.Label(
            self.root,
            text="Heart Rate",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.Heart_label.place(x=295,y=240)

        self.Heart_entry = tk.Entry(
            self.root,
            width=14,
            font=("Calibri", 24),
            bg="white",
            fg="black",
            borderwidth=0,
            relief="solid",
        )
        self.Heart_entry.place(x=420,y=235)

        self.BPM_label = tk.Label(
            self.root,
            text="BPM",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.BPM_label.place(x=695,y=235)

        self.next_button = tk.Button(
            self.root,
            width=17,
            text="Next",
            font=("Calibri", 19,"bold"),
            bg="#1e7b7b",
            fg="Black",
            borderwidth=0,
            relief="flat",
            command=self.goto_gui6
        )
        self.next_button.place(x=420,y=380)

        self.right_arrow_button = tk.Button(
            self.root,
            text="←",
            font=("Calibri", 15,"bold"),
            bg="#1e7b7b",
            fg="white",
            borderwidth=0,
            relief="flat",
            command=lambda: messagebox.showinfo("Forward", "You clicked Forward!"),
        )
        self.right_arrow_button.place(x=810, y=140)
    
    
    def goto_gui6(self):
        self.root.destroy()
        import Page7
        Page7.page7().run()

    def run(self):
        self.root.mainloop()