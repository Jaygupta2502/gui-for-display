import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class page1:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Advanced Body Composition Analyzer")
        #root.configure(bg="grey")


        # Set the window size
        self.root.geometry("1024x600")

        # Load and display the background image
        self.bg_image = Image.open("background.png")  # Replace "background.jpg" with your image file
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=303,y=180)

        # Create the MIT-ADT logo
        self.logo_image = Image.open("Mit_ADT.webp")  # Replace "mit_adt_logo.png" with your image file
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self.root, image=self.logo_photo)
        self.logo_label.place(x=0, y=0)

    # Create the CrieYa logo
        self.crieya_image = Image.open("CRIEYA_logo_to_size.png")  # Replace "crieya_logo.png" with your image file
        self.crieya_photo = ImageTk.PhotoImage(self.crieya_image)
        self.crieya_label = tk.Label(self.root, image=self.crieya_photo)
        self.crieya_label.place(x=844, y=10)

        # Create the device logo
        self.device_image = Image.open("device_logo.png")  # Replace "crieya_logo.png" with your image file
        self.device_photo = ImageTk.PhotoImage(self.device_image)
        self.device_label = tk.Label(self.root, image=self.device_photo)
        self.device_label.place(x=378, y=362)

        # Create the title label
        self.title_label = tk.Label(self.root, text="Advanced Body Composition Analyzer", font=("Arial", 30), fg="Red")
        self.title_label.place(x=175, y=533)


        #Create the login button
        self.login_button = tk.Button(self.root, text="ENTER LOGIN PIN",  font=("Arial", 18), bg="teal", fg="white",command=self.goto_gui2)
        self.login_button.place(x=390, y=446)

    def goto_gui2(self):
        self.root.destroy()
        import Page2
        Page2.page2().run()
        
    def run(self):
        self.root.mainloop()

