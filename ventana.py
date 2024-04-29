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

contador_filas = 0


def eliminar_nodo():
    global contador_filas
    if contador_filas > 0:
        # Obtener el widget de la última fila y destruirlo
        for widget in ventana.grid_slaves(row=contador_filas):
            widget.grid_forget()
        contador_filas -= 1
    else:
        print('No hay mas nodos cargados')


def cantidad_nodos(cantidad):
    print(cantidad)


def agregar_nodo():
    global contador_filas
    # Convertir el número de fila en un carácter alfabético
    etiqueta_nodo = chr(65 + contador_filas)  # 65 es el código ASCII para 'A'

    # Crear y ubicar el nodo con su nombre
    label_nodo = tk.Label(ventana, text="Nodo " +
                          etiqueta_nodo, padx=10, pady=10)
    label_nodo.grid(row=contador_filas+1, column=0, sticky="ew")

    # Crear y ubicar el campo de entrada para la posición X
    label_x = tk.Label(ventana, text="Posición X:")
    label_x.grid(row=contador_filas+1, column=1, padx=10, pady=5)
    input_x = tk.Entry(ventana)
    input_x.grid(row=contador_filas+1, column=2, padx=10, pady=5)

    # Crear y ubicar el campo de entrada para la posición Y
    label_y = tk.Label(ventana, text="Posición Y:")
    label_y.grid(row=contador_filas+1, column=3, padx=10, pady=5)
    input_y = tk.Entry(ventana)
    input_y.grid(row=contador_filas+1, column=4, padx=10, pady=5)

    # Incrementar el contador de filas
    contador_filas += 1


ventana = tk.Tk()
ventana.title("Trabajo Practica Final IA 1")
# Establecer la geometría inicial de la ventana
ventana.geometry("400x200")

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

boton_agregar_nodo.grid(row=0, column=2)
boton_eliminar_nodo.grid(row=0, column=3)


ventana.config(menu=menu_principal)

# Iniciar el bucle de eventos principal
ventana.mainloop()
