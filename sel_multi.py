import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as mb

# create a tkinter window
window = tk.Tk()
window.geometry("500x200")
window.title("Multiple Selection Combobox using the Listbox widget")

values = ["A","B"]

# Load the images
plus_image = Image.open("plus.png")
minus_image = Image.open("minus.png")

# Resize the images to desired dimensions
plus_image = plus_image.resize((15, 15))
minus_image = minus_image.resize((15, 15))

# Convert images to Tkinter PhotoImage objects
plus_icon = ImageTk.PhotoImage(plus_image)
minus_icon = ImageTk.PhotoImage(minus_image)

# Function to handle button clicks
def plus_clicked():
    selected_value = combobox.get()
    if selected_value == "":
        mb.showwarning(
            "Danger", "La conexion no puede estar vacia!", parent=window)
    elif selected_value in values:
        mb.showwarning(
            "Danger", "El nodo ya se encuentra en la lista!", parent=window)
    else:
        values.append(selected_value)
        label_uniones.config(text=values)
        print(values)

def minus_clicked():
    if len(values) > 0:
        values.pop()
        label_uniones.config(text=values)
    else:
        mb.showwarning(
            "Danger", "No hay mas nodos en la lista!", parent=window)


# create a label for the combobox
label = ttk.Label(window, text="Conexiones:")
combobox = ttk.Combobox(window, values=values, state="readonly")
label.pack(side="left", padx=10, pady=10)
combobox.pack(side="left", padx=10, pady=10)

button_add = ttk.Button(window, image=plus_icon, command=plus_clicked)
button_remove = ttk.Button(window, image=minus_icon, command=minus_clicked)
button_add.pack(side="left", padx=10, pady=10)
button_remove.pack(side="left", padx=10, pady=10)

label_conex = ttk.Label(window, text="Uniones:")
label_conex.pack(side="left", padx=10, pady=10)

label_uniones = ttk.Label(window, text=f"{values}")
label_uniones.pack(side="left", padx=10, pady=10)


# start the main loop
window.mainloop()
