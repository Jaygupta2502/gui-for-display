import tkinter as tk
from tkinter import ttk

class Page3:
    def __init__(self):

        def submit_data():
            # Get data from dropdown boxes
            medical_condition = self.medical_variable.get()
            disabilities = self.disabilities_variable.get()
            implants = self.implants_variable.get()
            physical_activity = self.physical_variable.get()
            water_intake = self.water_variable.get()
            alcohol_consumption = self.alcohol_variable.get()
            smoking_cigaratte = self.smoking_variable.get()

        # Print data to the console (you can replace this with saving to a file, database, etc.)
            print("Medical Condition:", medical_condition)
            print("Disabilities:", disabilities)
            print("Implants:", implants)
            print("Physical Activity:", physical_activity)
            print("Water Intake:", water_intake)
            print("Alcohol Consumption:", alcohol_consumption)
            print("Smoking Cigaratte:", smoking_cigaratte)

        # Create main window
        self.root = tk.Tk()
        self.root.title("Mandatory Information")
        self.root.geometry("1024x600")
        self.root.configure(bg="#BEBEBE")
        def get_pas(event):
            print(f'x:{event.x}y:{event.y}')

        self.root.bind('<Motion>', get_pas)
        self.mandatory_label = tk.Label(self.root, text="Mandatory Information", font=("calibri", 20, "bold"), bg="#BEBEBE")
        self.mandatory_label.place(x=410,y=0)
        self.recent_diet_label = tk.Label(self.root, text="Health Parameter (if any)", font=("calibri", 15), bg="#BEBEBE")
        self.recent_diet_label.place(x=410,y=50)
        self.Life_style_lable = tk.Label(self.root, text="Life Style Parameter (Last 30 Days Daily Available)", font=("calibri", 15), bg="#BEBEBE")
        self.Life_style_lable.place(x=335,y=240)
# Create labels and dropdown boxes
        self.medical_label = tk.Label(self.root, text="Medical Condition - Treatment", font=("calibri", 13), bg="#BEBEBE")
        self.medical_label.place(x=250,y=103)
        self.medical_variable = tk.StringVar(self.root)
        self.medical_variable.set("Select")  # Set initial value
        self.medical_dropdown = ttk.Combobox(self.root, textvariable=self.medical_variable, values=["Option 1", "Option 2", "Option 3"],width=40,font=("calibri",15))
        self.medical_dropdown.place(x=488,y=100)

        self.disabilities_label = tk.Label(self.root, text="Disabilities", font=("calibri", 13), bg="#BEBEBE")
        self.disabilities_label.place(x=385,y=130)
        self.disabilities_variable = tk.StringVar(self.root)
        self.disabilities_variable.set("Select")  # Set initial value
        self.disabilities_dropdown = ttk.Combobox(self.root, textvariable=self.disabilities_variable, values=["Option 1", "Option 2", "Option 3"],width=40,font=("calibri",15))
        self.disabilities_dropdown.place(x=488,y=130)

        self.implants_label = tk.Label(self.root, text="Implants", font=("calibri", 13), bg="#BEBEBE")
        self.implants_label.place(x=390,y=160)
        self.implants_variable = tk.StringVar(self.root)
        self.implants_variable.set("Select")  # Set initial value
        self.implants_dropdown = ttk.Combobox(self.root, textvariable=self.implants_variable, values=["Option 1", "Option 2", "Option 3"],width=40,font=("calibri",15))
        self.implants_dropdown.place(x=488,y=160)



        # Create labels and dropdown boxes for life style parameters
        self.physical_label = tk.Label(self.root, text="Physical Activity", font=("calibri", 13), bg="#BEBEBE")
        self.physical_label.place(x=350,y=300)
        self.physical_variable = tk.StringVar(self.root)
        self.physical_variable.set("Select")  # Set initial value
        self.physical_dropdown = ttk.Combobox(self.root, textvariable=self.physical_variable, values=["Option 1", "Option 2", "Option 3"],width=40,font=("calibri",15))
        self.physical_dropdown.place(x=488,y=300)

        self.water_label = tk.Label(self.root, text="Water Intake", font=("calibri", 13), bg="#BEBEBE")
        self.water_label.place(x=370,y=330)
        self.water_variable = tk.StringVar(self.root)
        self.water_variable.set("Select")  # Set initial value
        self.water_dropdown = ttk.Combobox(self.root, textvariable=self.water_variable, values=["Option 1", "Option 2", "Option 3"],width=40,font=("calibri",15))
        self.water_dropdown.place(x=488,y=330)

        self.alcohol_label = tk.Label(self.root, text="Alcohol Consumption", font=("calibri", 13), bg="#BEBEBE")
        self.alcohol_label.place(x=310,y=360)
        self.alcohol_variable = tk.StringVar(self.root)
        self.alcohol_variable.set("Select")  # Set initial value
        self.alcohol_dropdown = ttk.Combobox(self.root, textvariable=self.alcohol_variable, values=["Option 1", "Option 2", "Option 3"],width=40,font=("calibri",15))
        self.alcohol_dropdown.place(x=488,y=360)
        self.smoking_label = tk.Label(self.root, text="Smoking Cigaratte", font=("calibri", 13), bg="#BEBEBE")
        self.smoking_label.place(x=328,y=390)
        self.smoking_variable = tk.StringVar(self.root)
        self.smoking_variable.set("Select")  # Set initial value
        self.smoking_dropdown = ttk.Combobox(self.root, textvariable=self.smoking_variable, values=["Option 1", "Option 2", "Option 3"],width=40,font=("calibri",15))
        self.smoking_dropdown.place(x=488,y=390)

# Create submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.goto_gui3,font=("calibri",15),bg="#1e7b7b",fg="Black",width=18)
        self.submit_button.place(x=430,y=471)

    def goto_gui3(self):
        self.root.destroy()
        import page4
        page4.Page4().run()
        
    def run(self):
        self.root.mainloop()