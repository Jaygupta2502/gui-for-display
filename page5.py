import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Page5:
    def __init__(self):

# Create the main window
        self.root = tk.Tk()
        self.root.title("Height & Body Temperature")
        self.root.geometry("1024x600")
        self.root.configure(bg="#BEBEBE")

# Create the title label
        self.title_label = tk.Label(
            self.root,
            text="Height & Body Temperature",
            font=("Calibri", 19,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.title_label.place(x=375, y=50)

# Create the height input
        self.height_label = tk.Label(
            self.root,
            text="Height",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.height_label.place(x=340,y=125)

        self.height_entry = tk.Entry(
        self.root,
        width=14,
        font=("Calibri", 24),
        bg="white",
        fg="black",
        borderwidth=2,
        relief="solid",
        )
        self.height_entry.place(x=420,y=120)

        self.cms_label = tk.Label(
            self.root,
            text="cms",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.cms_label.place(x=695,y=125)

# Create the body temperature input
        self.body_temp_label = tk.Label(
            self.root,
            text="Body Temperature",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.body_temp_label.place(x=225,y=213)

        self.body_temp_entry = tk.Entry(
            self.root,
            width=14,
            font=("Calibri", 24),
            bg="white",
            fg="black",
            borderwidth=2,
            relief="solid",
        )
        self.body_temp_entry.place(x=420,y=205)

        self.f_label = tk.Label(
            self.root,
            text="°F",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.f_label.place(x=695,y=210)

# Create the ambient temperature input
        self.ambient_temp_label = tk.Label(
            self.root,
            text="Ambient Temperature",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.ambient_temp_label.place(x=200,y=295)

        self.ambient_temp_entry = tk.Entry(
            self.root,
            width=14,
            font=("Calibri", 24),
            bg="white",
            fg="black",
            borderwidth=2,
            relief="solid",
        )
        self.ambient_temp_entry.place(x=420,y=290)

        self.c_label = tk.Label(
            self.root,
            text="°C",
            font=("Calibri", 15,"bold"),
            bg="#BEBEBE",
            fg="black",
        )
        self.c_label.place(x=695,y=300)

        # Create the next button
        self.next_button = tk.Button(
            self.root,
            width=17,
            text="Next",
            font=("Calibri", 19,"bold"),
            bg="#1e7b7b",
            fg="Black",
            borderwidth=0,
            relief="flat",
            command=self.goto_gui5,
        )
        self.next_button.place(x=420,y=380)

        # Create the left arrow button
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
        self.left_arrow_button.place(x=810, y=206)

        # Create the right arrow button
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
        self.right_arrow_button.place(x=810, y=120)

    def goto_gui5(self):
        self.root.destroy()
        import page6
        page6.Page6().run()
        
    def run(self):
        self.root.mainloop()