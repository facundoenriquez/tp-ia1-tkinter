import tkinter as tk

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

ventana = tk.Tk()
ventana.config(width=400, height=300)


def agregar_nodo():
    print('agregar nodo')


def eliminar_nodo():
    print('eliminar nodo')


def cantidad_nodos(cantidad):
    print(cantidad)


# MENU
# Creo el menu de la ventana
menu_principal = tk.Menu()

# Se crean las opciones principales
menu_nodos = tk.Menu(menu_principal, tearoff=False)

# Agregar las opciones principales al menu
menu_principal.add_cascade(label="Nodos",
                           menu=menu_nodos)

menu_nodos.add_command(label="Agregar Cantidad de Nodos",
                       command=lambda: cantidad_nodos(5))

# Crear y ubicar botones de agregar y quitar nodo
boton_agregar_nodo = tk.Button(
    ventana, text="Agregar Nodo", command=agregar_nodo)
boton_eliminar_nodo = tk.Button(
    ventana, text="Eliminar Nodo", command=eliminar_nodo)

boton_agregar_nodo.grid(row=0, column=1)
boton_eliminar_nodo.grid(row=0, column=2)

# Crear y ubicar el nodo A con su nombre
label_nodo_a = tk.Label(ventana, text="A", padx=10, pady=10)
label_nodo_a.grid(row=1, column=0, sticky="ew")

# Crear y ubicar el campo de entrada para la posición X
label_x = tk.Label(ventana, text="Posición X:")
label_x.grid(row=1, column=1, padx=10, pady=5)

input_x = tk.Entry(ventana)
input_x.grid(row=1, column=2, padx=10, pady=5)

# Crear y ubicar el campo de entrada para la posición Y
label_y = tk.Label(ventana, text="Posición Y:")
label_y.grid(row=1, column=3, padx=10, pady=5)

input_y = tk.Entry(ventana)
input_y.grid(row=1, column=4, padx=10, pady=5)

ventana.config(menu=menu_principal)

# Iniciar el bucle de eventos principal
ventana.mainloop()
