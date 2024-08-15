import tkinter as tk
from tkinter import messagebox

class page7:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Weight & Body Composition Analysis")
        self.root.geometry("1024x600")
        self.root.configure(bg="#BEBEBE")  # Set background color

        self.mandatory_label = tk.Label(self.root, text="Weight & Body Composition Analysis", font=("Calibri", 20, "bold"), bg="#BEBEBE")
        self.mandatory_label.place(x=300,y=50)
        # Create the height input
        self.SpO2_label = tk.Label(
            self.root,
            text="Body Weight",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.SpO2_label.place(x=270,y=148)

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
            text="Kgs",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.Percentage_label.place(x=695,y=145)

# Create the height input
        self.Heart_label = tk.Label(
            self.root,
            text="Body Measurement",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.Heart_label.place(x=225,y=240)

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

        self.next_button = tk.Button(
            self.root,
            width=17,
            text="Next",
            font=("Calibri", 19,"bold"),
            bg="#1e7b7b",
            fg="Black",
            borderwidth=0,
            relief="flat",
            command=lambda: messagebox.showinfo("Next", "You clicked Next!"),
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

        self.left_arrow_button = tk.Button(
            self.root,
            height=1,
            text="←",
            font=("Calibri", 15,"bold"),
            bg="#1e7b7b",
            fg="white",
            borderwidth=0,
            relief="flat",
            command=lambda: messagebox.showinfo("Back", "You clicked Back!"),
        )
        self.left_arrow_button.place(x=810, y=235)

    def goto_gui1(self):
            self.window.destroy()
            import Page1
            Page1.page1().run()

    def run(self):
        self.window.mainloop()