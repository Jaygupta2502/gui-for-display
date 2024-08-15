
import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

class page2:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Welcome")
        self.window.geometry("1024x600")  # Set the resolution

        self.welcome_label = ttk.Label(self.window, text="WELCOME", font=("Arial", 30))
        self.welcome_label.place(x=423, y=20)

        self.description_label = ttk.Label(self.window, text="Login to initiate your measurements", font=("Arial", 23))
        self.description_label.place(x=300, y=75)

        # Dropdown Options
        self.dropdown_options = ["Phone Number", "UUID"]
        self.dropdown_variable = tk.StringVar(self.window)
        self.dropdown_variable.set(self.dropdown_options[0])  # Default to "Phone Number"
        self.dropdown = ttk.Combobox(self.window, textvariable=self.dropdown_variable, values=self.dropdown_options)
        self.dropdown.place(x=450, y=160)

        # Phone Number/UUID Entry
        self.phone_entry = ttk.Entry(self.window, font=("Arial", 18))
        self.phone_entry.place(x=405, y=190)

        # Next Button
        self.next_button = tk.Button(self.window, text="   Next    ", font=("Arial", 15), bg="teal", fg="white", command=self.on_next_button_click)
        self.next_button.place(x=478, y=250)

    def check_customer(self, input_value, selected_option):
        if selected_option == "Phone Number":
            api_url = f"http://15.207.85.39/api/get-info?phoneNumber={input_value}"
        elif selected_option == "UUID":
            api_url = f"http://15.207.85.39/api/get-info?UUID={input_value}"

        try:
            response = requests.get(api_url)
            data = response.json()

            if "UUID" in data:
                # Save JSON data locally
                timestamp = data.get("Timestamp", "no_timestamp").replace(" ", "_").replace(":", "-")
                filename = f"{data['UUID']}_{timestamp}_info.json"
                with open(filename, "w") as json_file:
                    json.dump(data, json_file, indent=4)

                return True  # Customer exists

            else:
                # Display an error message
                messagebox.showerror("Error", f"Customer not found for {selected_option}. Please try again.")
                return False

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to connect to API: {e}")
            return False

    def on_next_button_click(self):
        input_value = self.phone_entry.get()  # Get the input from the entry widget
        selected_option = self.dropdown_variable.get()  # Get the selected dropdown option

        if self.check_customer(input_value, selected_option):
            self.goto_gui1()  # Proceed to the next page if the customer exists

    def goto_gui1(self):
        self.window.destroy()
        import page3
        page3.Page3().run()

    def run(self):
        self.window.mainloop()

# Example usage
if __name__ == "__main__":
    app = page2()
    app.run()
