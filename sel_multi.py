import tkinter as tk
from tkinter import ttk

# create a tkinter window
window = tk.Tk()
window.geometry("400x200")
window.title("Multiple Selection Combobox using the Listbox widget")

# define the values for the dropdown list
values = ["Value 1", "Value 2", "Value 3", "Value 4", "Value 5"]

# create a label for the combobox
label = ttk.Label(window, text="Select values:")
combobox = ttk.Combobox(window, values=values, state="readonly")
label.pack(side="left", padx=10, pady=10)
combobox.pack(side="left", padx=10, pady=10)

label_conex = ttk.Label(window, text="Conexiones:")


# start the main loop
window.mainloop()
