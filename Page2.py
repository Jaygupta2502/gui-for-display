import tkinter as tk
from tkinter import ttk
class page2:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Welcome")
        self.window.geometry("1024x600")  # Set the resolution

        self.welcome_label = ttk.Label(self.window, text="WELCOME", font=("Arial", 30))
        self.welcome_label.place(x=42320,y=0)

        # Create the description label
        self.description_label = ttk.Label(self.window, text="Login to initiate your measurements", font=("Arial", 23))
        self.description_label.place(x=300,y=48)

        # Login ID Label
        #login_id_label = tk.Label(window, text="Login ID",font=("Arial",18))
        #login_id_label.place(x=483,y=151)

        self.login_button = tk.Button(self.window, text="LOGIN", command=lambda: print("Login button clicked"), font=("Arial", 18), bg="white", fg="black")
        self.login_button.place(x=475,y=100)

        # Login ID Entry
        #login_id_entry = tk.Entry(window)
        #login_id_entry.place(x=400,y=48)

        # Dropdown Options
        self.dropdown_options = ["Option 1", "Option 2", "Option 3"]

        # Dropdown Variable
        self.dropdown_variable = tk.StringVar(self.window)
        self.dropdown_variable.set(self.dropdown_options[0])  # Default value

        # Dropdown Widget
        self.dropdown = ttk.Combobox(self.window, textvariable=self.dropdown_variable, values=self.dropdown_options)
        self.dropdown.place(x=450,y=160)

        # Next Button
        def next_button_clicked(self):
            # Your logic for handling the button press
            self.print(f"Selected Login ID: {self.login_id_entry.get()}")
            self.print(f"Selected Dropdown Option: {self.dropdown_variable.get()}")

        self.next_button = tk.Button(self.window, text="   Next    ",font=("Arial", 15), bg="teal", fg="white",command=self.goto_gui1)
        self.next_button.place(x=478,y=190)
        

    def goto_gui1(self):
            self.window.destroy()
            import page3
            page3.Page3().run()

    def run(self):
        self.window.mainloop()