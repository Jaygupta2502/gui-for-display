import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Page4:
        def __init__(self):
                def on_submit(self):
                        food_value = self.food_var.get()
                        coffee_tea_value = self.coffee_tea_var.get()
                        water_value = self.water_var.get()
                        alcohol_value = self.alcohol_var.get()
                        # Do something with the values, such as sending them to a server
                        messagebox.showinfo("Submission", "The following values were submitted:\nFood: {}\nCoffee/Tea/Milk/Juices Etc: {}\nWater: {}\nAlcohol: {}".format(food_value, coffee_tea_value, water_value, alcohol_value))

                def on_verify():
        # Validate the OTP
                        otp_value = self.otp_entry.get()
                        if otp_value == "1234":
                                messagebox.showinfo("Verification", "OTP verified successfully.")
                        else:
                                messagebox.showerror("Verification Error", "Invalid OTP.")

    # Create the main window
                self.root = tk.Tk()
                self.root.title("Mandatory Information")
                self.root.geometry("1024x600")
                self.root.configure(bg="#F0F0F0")  # Light grey background

# Set font for all labels and buttons
                font = ("calibri", 14,)

# Labels
                self.mandatory_label = tk.Label(self.root, text="Mandatory Information", font=("calibri", 20, "bold"), bg="#F0F0F0")
                self.recent_diet_label = tk.Label(self.root, text="Recent Diet Information", font=("calibri", 15), bg="#F0F0F0")

# Food label and dropdown
                self.food_label = tk.Label(self.root, text="Food", font=font, bg="#F0F0F0")
                self.food_var = tk.StringVar(value="Select")
                self.food_dropdown = ttk.Combobox(self.root, textvariable=self.food_var, values=["Option 1", "Option 2", "Option 3"], state="readonly",width=30,font=("calibri",15))

        # Coffee/Tea/Milk/Juices Etc label and dropdown
                self.coffee_tea_label = tk.Label(self.root, text="Coffee/Tea/Milk/Juices Etc", font=font, bg="#F0F0F0")
                self.coffee_tea_var = tk.StringVar(value="Select")
                self.coffee_tea_dropdown = ttk.Combobox(self.root, textvariable=self.coffee_tea_var, values=["Option 1", "Option 2", "Option 3"], state="readonly",width=30,font=("calibri",15))

        # Water label and dropdown
                self.water_label = tk.Label(self.root, text="Water", font=font, bg="#F0F0F0")
                self.water_var = tk.StringVar(value="Select")
                self.water_dropdown = ttk.Combobox(self.root, textvariable=self.water_var, values=["Option 1", "Option 2", "Option 3"], state="readonly",width=30,font=("calibri",15))

        # Alcohol label and dropdown
                self.alcohol_label = tk.Label(self.root, text="Alcohol", font=font, bg="#F0F0F0")
                self.alcohol_var = tk.StringVar(value="Select")
                self.alcohol_dropdown = ttk.Combobox(self.root, textvariable=self.alcohol_var, values=["Option 1", "Option 2", "Option 3"], state="readonly",width=30,font=("calibri",15))

        # Submit button
                self.submit_button = tk.Button(self.root, text="Submit", command=on_submit, font=font, bg="#008080", fg="white", width=10)

        # Enter OTP label and entry
                self.otp_label = tk.Label(self.root, text="Enter OTP", font=font, bg="#F0F0F0")
                self.otp_entry = tk.Entry(self.root, font=font)

        # Verify button
                self.verify_button = tk.Button(self.root, text="Verify", command=self.goto_gui4, font=font, bg="#008080", fg="white", width=10)

        # Confirmation message
                self.confirmation_label = tk.Label(self.root, text="I confirm that the above information is true and to the best of my knowledge", font=font, bg="#F0F0F0")

        # Position the widgets
                self.mandatory_label.place(x=375,y=0)
                self.recent_diet_label.place(x=410,y=50)

                self.food_label.place(x=285,y=110)
                self.food_dropdown.place(x=350,y=110)

                self.coffee_tea_label.place(x=90,y=143)
                self.coffee_tea_dropdown.place(x=350,y=143)

                self.water_label.place(x=282,y=176)
                self.water_dropdown.place(x=350,y=176)

                self.alcohol_label.place(x=265,y=209)
                self.alcohol_dropdown.place(x=350,y=209)

                self.submit_button.place(x=465,y=275)

                self.otp_label.place(x=470,y=345)
                self.otp_entry.place(x=415,y=375)

                self.verify_button.place(x=465,y=420)

                self.confirmation_label.place(x=160,y=480)
        def goto_gui4(self):
                self.root.destroy()
                import page5
                page5.Page5().run()

        def run(self):
                self.root.mainloop()
        
