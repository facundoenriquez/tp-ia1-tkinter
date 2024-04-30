from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Cada equipo de trabajo deberá desarrollar una aplicación que permita:

# (1) la carga del espacio de búsqueda en forma de grafo indicando: cantidad de nodos,
# conexiones (bidireccionales) entre los nodos, nodo inicial, nodo final.

# (2) La implementación de los algoritmos de búsqueda de Escalada Simple y Máxima Pendiente,
# utilizando la métrica de distancia en línea recta y distancia Manhattan como heurísticas.

# (3) La visualización del proceso paso a paso.

# (4) La comparación en el funcionamiento de ambos algoritmos, esto implica,
# por ejemplo comparar la cantidad de pasos para llegar al objetivo, la
# debilidad ante máximos/mínimos locales que impidan encontrar el objetivo.

# (5) La visualización del resultado final de la comparativa.
# Todos los datos necesarios deberán ser cargados por el usuario
# y tener una opción de creación de espacios de
# estados de manera aleatoria (cantidad de nodos, conexiones entre los mismos, estado inicial,
# estado final y distancias en línea recta al objetivo).

contador_filas = 0
nodos = []


def agregar_nodo(heuristica):
    global contador_filas, nodos
    if heuristica == "dlr":
        print(heuristica)

        ajustar_ventana()

    else:
        # Convertir el número de fila en un carácter alfabético
        # 65 es el código ASCII para 'A'
        etiqueta_nodo = chr(65 + contador_filas)
        # Agrego el nodo a la lista de nodos
        nodos.append(etiqueta_nodo)
        # Crear y ubicar el nodo con su nombre
        label_nodo = tb.Label(ventana, text="Nodo " + etiqueta_nodo)
        label_nodo.grid(row=contador_filas+2, column=0, padx=10, pady=10)

        # Crear y ubicar el campo de entrada para la posición X
        label_x = tb.Label(ventana, text="Posición X:")
        label_x.grid(row=contador_filas+2, column=1, padx=10, pady=5)
        input_x = tb.Entry(ventana)
        input_x.grid(row=contador_filas+2, column=2, padx=10, pady=5)

        # Crear y ubicar el campo de entrada para la posición Y
        label_y = tb.Label(ventana, text="Posición Y:")
        label_y.grid(row=contador_filas+2, column=3, padx=10, pady=5)
        input_y = tb.Entry(ventana)
        input_y.grid(row=contador_filas+2, column=4, padx=10, pady=5)

        # Creo el combo box (MenuButton) y agrego valores al mismo
        # Crear el listbox con los nodos disponibles
        label_conexiones = tb.Label(ventana, text="Select values:")
        label_conexiones.grid(row=contador_filas+2, column=5, padx=10, pady=5)
        combo_conexiones = tb.Combobox(ventana, state="readonly")
        listbox_conexiones = Listbox(
            ventana, selectmode=MULTIPLE, exportselection=0)
        for value in nodos:
            listbox_conexiones.insert(END, value)

        # define a function to update the combobox when the user selects or deselects a value
        def update_combobox():
            # Get selected values from the Listbox widget
            selected_values = [listbox_conexiones.get(
                idx) for idx in listbox_conexiones.curselection()]

            # Update the combobox with the selected values
            combo_conexiones.configure(width=40, height=7)
            combo_conexiones.set(", ".join(selected_values))

        # bind the update_combobox function to the Listbox widget
        listbox_conexiones.bind("<<ListboxSelect>>",
                                lambda _: update_combobox())

        # Incrementar el contador de filas
        contador_filas += 1

        ajustar_ventana()


def eliminar_nodo():
    global contador_filas
    if contador_filas > 0:
        # Obtener el widget de la última fila y destruirlo
        for widget in ventana.grid_slaves(row=contador_filas):
            widget.grid_forget()
        contador_filas -= 1
        # Elimino el ultimo nodo a la lista de nodos
        nodos.pop()
    else:
        print('No hay mas nodos cargados')
    if contador_filas == 0:
        ventana.geometry("400x200")


def cantidad_nodos(cantidad):
    print(cantidad)


def estados_aleatorios():
    print('estados aleatorios')


def distancia_recta():
    print('distancia recta')
    limpiar_ventana()
    # Crear y ubicar botones de agregar y quitar nodo
    boton_agregar_nodo = tb.Button(
        ventana, text="Agregar Nodo", command=lambda: agregar_nodo("dlr"))
    boton_eliminar_nodo = tb.Button(
        ventana, text="Eliminar Nodo", command=lambda: eliminar_nodo("dlr"))

    boton_agregar_nodo.grid(row=1, column=2, pady=20, padx=20)
    boton_eliminar_nodo.grid(row=1, column=3, pady=20)

    # Crear y centrar el label
    crear_label_central("Distancia en línea recta")


def distancia_manhattan():
    print('distancia manhattan')
    limpiar_ventana()

    # Crear y ubicar botones de agregar y quitar nodo
    boton_agregar_nodo = tb.Button(
        ventana, text="Agregar Nodo", command=lambda: agregar_nodo("manhattan"))
    boton_eliminar_nodo = tb.Button(
        ventana, text="Eliminar Nodo", command=lambda: eliminar_nodo("manhattan"))

    boton_agregar_nodo.grid(row=1, column=2, pady=20, padx=20)
    boton_eliminar_nodo.grid(row=1, column=3, pady=20)

    # Crear y centrar el label
    crear_label_central("Distancia Manhattan")


def limpiar_ventana():
    global contador_filas, nodos
    # Eliminar todos los widgets de la ventana
    for widget in ventana.winfo_children():
        if widget != menu_principal:
            widget.destroy()
    # Reiniciar el contador de filas y la lista de nodos
    contador_filas = 0
    nodos = []

    # Establecer la geometría inicial de la ventana
    ventana.geometry("400x200")


def crear_label_central(texto):
    font = "Helvetica"
    label_central = tb.Label(ventana, text=texto, font=(font, 15))
    label_central.grid(row=0, column=0, columnspan=6, pady=15)


def ajustar_ventana():
    # Ajustar la ventana automáticamente
    ventana.update_idletasks()
    ventana.geometry("")


# Instanciar la ventana
ventana = tb.Window(themename="superhero")
# Darle titulo a la ventana
ventana.title("Trabajo Practica Final IA 1")
# Establecer la geometría inicial de la ventana
ventana.geometry("400x200")

# MENU
# Creo el menu de la ventana
menu_principal = tb.Menu()

# Se crean las opciones principales
menu_heuristicas = tb.Menu(menu_principal, tearoff=False)

# Agregar las opciones principales al menu
menu_principal.add_cascade(label="Heuristicas",
                           menu=menu_heuristicas)

menu_heuristicas.add_command(label="Distancia en linea recta",
                             command=lambda: distancia_recta())
menu_heuristicas.add_command(label="Distancia Manhattan",
                             command=lambda: distancia_manhattan())

# # Crear y ubicar botones de agregar y quitar nodo
# boton_agregar_nodo = tb.Button(
#     ventana, text="Agregar Nodo", command=agregar_nodo)
# boton_eliminar_nodo = tb.Button(
#     ventana, text="Eliminar Nodo", command=eliminar_nodo)

# boton_agregar_nodo.grid(row=0, column=2, pady=20, padx=20)
# boton_eliminar_nodo.grid(row=0, column=3, pady=20)


# Agregar el menu a la ventana
ventana.config(menu=menu_principal)

# Iniciar el bucle de eventos principal
ventana.mainloop()
