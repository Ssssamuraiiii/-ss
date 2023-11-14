import tkinter as tk
from tkinter import ttk
from datetime import datetime

def update_datetime():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label.config(text="Current Date and Time: " + current_datetime)
    root.after(1000, update_datetime)  # Update every 1000 milliseconds (1 second)

# Creating the main window
root = tk.Tk()
root.title("Date and Time Display")

# Creating a label to display the date and time
label = ttk.Label(root, font=("Helvetica", 14))

# Placing the label in the main window
label.pack(pady=20)

# Calling the update_datetime function initially
update_datetime()

# Running the main loop of the program
root.mainloop()
