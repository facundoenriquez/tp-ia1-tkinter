import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as mb
from distancias import distancias_manhattan, distancias_linea_recta
from conexiones_nodos import uniones_nodos
import random
from dibujar import crear_ventana_inicial
import sys

# from ejemplo_matplot import crear_ventana_inicial

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

contador_filas_dlr = 0
contador_filas_manhattan = 0
nodos = {}
nodo_inicial = ""
nodo_final = ""
posiciones = {}
comboboxes_dlr = []
comboboxes_manhattan = []
contador_comboboxes = 0
contador_campos_x = 0
contador_campos_y = 0
contador_campos_dlr = 0
campos_x = []
campos_y = []
campos_dlr = []


def agregar_nodo(heuristica):
    global contador_filas_dlr, contador_filas_manhattan, nodos
    if heuristica == "dlr":
        # Convertir el número de fila en un carácter alfabético
        # 65 es el código ASCII para 'A'
        etiqueta_nodo = chr(65 + contador_filas_dlr)

        # Agrego el nodo a la lista de nodos
        nodos[etiqueta_nodo] = []

        # Crear y ubicar el nodo con su nombre
        label_nodo = tk.Label(ventana, text="Nodo " + etiqueta_nodo)
        label_nodo.grid(row=contador_filas_dlr+2, column=0, padx=10, pady=10)

        # Crear y ubicar el campo de entrada para la posición X
        label_drl = tk.Label(ventana, text="Distancia en linea recta:")
        label_drl.grid(row=contador_filas_dlr+2, column=1, padx=10, pady=5)
        label_dlr = tk.Entry(ventana)
        label_dlr.grid(row=contador_filas_dlr+2, column=2, padx=10, pady=5)

        # Agrego los inputs a una lista global de inputs
        posiciones[etiqueta_nodo] = [label_dlr]

        # Crear y ubicar el label y combo para los conexiones de los nodos
        nodos_combo_label = tk.Label(ventana, text="Conexiones:")
        nodos_combo_label.grid(row=contador_filas_dlr+2,
                               column=3, padx=10, pady=5)
        keys = list(nodos.keys())
        nodo_combobox = ttk.Combobox(ventana, values=keys, state="readonly")
        nodo_combobox.grid(row=contador_filas_dlr+2, column=4, padx=10, pady=5)

        # Crear y ubicar hacia que nodos se une el nodo de la fila correspondiente
        label_conex = tk.Label(ventana, text="Uniones:")
        label_conex.grid(row=contador_filas_dlr+2, column=7, padx=10, pady=5)
        label_uniones = tk.Label(ventana, text=f"{nodos[etiqueta_nodo]}")
        label_uniones.grid(row=contador_filas_dlr+2,
                           column=10, padx=10, pady=5)

        # Crear y ubicar los botones de agregar y eliminar nodos de la lista de conexiones
        button_add = tk.Button(ventana, image=plus_icon, command=lambda: plus_clicked(
            nodo_combobox, nodos[etiqueta_nodo], label_uniones, etiqueta_nodo))
        button_add.grid(row=contador_filas_dlr+2, column=5, padx=10, pady=5)
        button_remove = tk.Button(
            ventana, image=minus_icon, command=lambda: minus_clicked(nodos[etiqueta_nodo], label_uniones))
        button_remove.grid(row=contador_filas_dlr+2, column=6, padx=10, pady=5)

        # Incrementar el contador de filas
        contador_filas_dlr += 1

        # Agrega el Combobox recién creado a una lista global
        comboboxes_dlr.append(nodo_combobox)
        # Actualizar todos los Combobox
        actualizar_comboboxes_dlr()
        # Actualiza la lista de nodo inicial y final
        actualizar_nodo_inicial_final()
        # Actualizar ventana cuando cambia de heuristica
        ajustar_ventana()

    else:
        # Convertir el número de fila en un carácter alfabético
        # 65 es el código ASCII para 'A'
        etiqueta_nodo = chr(65 + contador_filas_manhattan)

        # Agrego el nodo a la lista de nodos
        nodos[etiqueta_nodo] = []

        # Crear y ubicar el nodo con su nombre
        label_nodo = tk.Label(ventana, text="Nodo " + etiqueta_nodo)
        label_nodo.grid(row=contador_filas_manhattan +
                        2, column=0, padx=10, pady=10)

        # Crear y ubicar el campo de entrada para la posición X
        label_x = tk.Label(ventana, text="Distancia X:")
        label_x.grid(row=contador_filas_manhattan+2, column=1, padx=10, pady=5)
        input_x = tk.Entry(ventana)
        input_x.grid(row=contador_filas_manhattan+2, column=2, padx=10, pady=5)

        # Crear y ubicar el campo de entrada para la posición Y
        label_y = tk.Label(ventana, text="Distancia Y:")
        label_y.grid(row=contador_filas_manhattan+2, column=3, padx=10, pady=5)
        input_y = tk.Entry(ventana)
        input_y.grid(row=contador_filas_manhattan+2, column=4, padx=10, pady=5)

        # Agrego los inputs a una lista global de inputs
        posiciones[etiqueta_nodo] = [input_x, input_y]

        # Crear y ubicar el label y combo para los conexiones de los nodos
        nodos_combo_label = tk.Label(ventana, text="Conexiones:")
        nodos_combo_label.grid(
            row=contador_filas_manhattan+2, column=5, padx=10, pady=5)
        keys = list(nodos.keys())
        nodo_combobox = ttk.Combobox(ventana, values=keys, state="readonly")
        nodo_combobox.grid(row=contador_filas_manhattan +
                           2, column=6, padx=10, pady=5)

        # Crear y ubicar los botones de agregar y eliminar nodos de la lista de conexiones
        button_add = tk.Button(ventana, image=plus_icon, command=lambda: plus_clicked(
            nodo_combobox, nodos[etiqueta_nodo], label_uniones, etiqueta_nodo))
        button_add.grid(row=contador_filas_manhattan +
                        2, column=7, padx=10, pady=5)
        button_remove = tk.Button(
            ventana, image=minus_icon, command=lambda: minus_clicked(nodos[etiqueta_nodo], label_uniones))
        button_remove.grid(row=contador_filas_manhattan +
                           2, column=8, padx=10, pady=5)

        # Crear y ubicar hacia que nodos se une el nodo de la fila correspondiente
        label_conex = tk.Label(ventana, text="Uniones:")
        label_conex.grid(row=contador_filas_manhattan +
                         2, column=9, padx=10, pady=5)
        label_uniones = tk.Label(ventana, text=f"{nodos[etiqueta_nodo]}")
        label_uniones.grid(row=contador_filas_manhattan +
                           2, column=10, padx=10, pady=5)

        # Incrementar el contador de filas
        contador_filas_manhattan += 1

        # Agrega el Combobox recién creado a una lista global
        comboboxes_manhattan.append(nodo_combobox)
        # Actualizar todos los Combobox
        actualizar_comboboxes_manhattan()
        # Actualiza la lista de nodo inicial y final
        actualizar_nodo_inicial_final()
        # Actualizar ventana cuando cambia de heuristica
        ajustar_ventana()


def actualizar_nodo_inicial_final():
    global nodo_inicial, nodo_final
    keys = list(nodos.keys())
    nodo_inicial['values'] = keys
    nodo_final['values'] = keys


def actualizar_comboboxes_dlr():
    keys = list(nodos.keys())
    for combobox in comboboxes_dlr:
        combobox['values'] = keys


def actualizar_comboboxes_manhattan():
    keys = list(nodos.keys())
    for combobox in comboboxes_manhattan:
        combobox['values'] = keys


def eliminar_nodo():
    global contador_filas
    if contador_filas > 0:
        # Obtener el widget de la última fila y destruirlo
        for widget in ventana.grid_slaves(row=contador_filas):
            widget.grid_forget()
        contador_filas -= 1
        # Elimino el ultimo nodo a la lista de nodos
        # nodos.pop()
    else:
        print('No hay mas nodos cargados')
    if contador_filas == 0:
        ventana.geometry("400x200")


def estados_aleatorios(heuristica):
    global contador_filas, nodos, contador_comboboxes

    if heuristica == "dlr":
        for widget in ventana.grid_slaves():
            if widget.grid_info()['row'] > 1:
                widget.grid_forget()
        nodos.clear()
        contador_filas = 0
        comboboxes_dlr.clear()
        campos_dlr.clear()
        contador_comboboxes = 0
        contador_campos_dlr = 0
        posiciones.clear()

        num_nodos = random.randint(1, 7)

        for i in range(num_nodos):
            etiqueta_nodo = chr(65 + i)
            nodos[etiqueta_nodo] = []

            # Crear y ubicar el nodo con su nombre
            label_nodo = tk.Label(ventana, text="Nodo " + etiqueta_nodo)
            label_nodo.grid(row=contador_filas+2, column=0, padx=10, pady=10)

            # Crear y ubicar el campo de entrada para la distancia en linea recta
            label_dlr = tk.Label(ventana, text="Distancia en linea recta:")
            label_dlr.grid(row=contador_filas+2, column=1, padx=10, pady=5)
            input_dlr_id = f"input_dlr_{contador_campos_dlr}"
            input_dlr = tk.Entry(ventana, name=input_dlr_id)
            input_dlr.grid(row=contador_filas+2, column=2, padx=10, pady=5)

            campos_dlr.append(input_dlr)

            # Agrego los inputs a una lista global de inputs
            posiciones[etiqueta_nodo] = [input_dlr]

            # Crear y ubicar el label y combo para los conexiones de los nodos
            nodos_combo_label = tk.Label(ventana, text="Conexiones:")
            nodos_combo_label.grid(row=contador_filas+2,
                                   column=3, padx=10, pady=5)
            keys = list(nodos.keys())
            combobox_id = f"combobox_{contador_comboboxes}"
            nodo_combobox = ttk.Combobox(
                ventana, values=keys, state="readonly", name=combobox_id)
            nodo_combobox.grid(row=contador_filas+2, column=4, padx=10, pady=5)

            # Agregar el Combobox recién creado a la lista global de Comboboxes
            comboboxes_dlr.append(nodo_combobox)

            # Actualizar todos los combos de conexión de los nodos
            actualizar_comboboxes_dlr()

            # Crear y ubicar hacia que nodos se une el nodo de la fila correspondiente
            label_conex = tk.Label(ventana, text="Uniones:")
            label_conex.grid(row=contador_filas+2, column=9, padx=10, pady=5)
            label_uniones = tk.Label(ventana, text=f"{nodos[etiqueta_nodo]}")
            label_uniones.grid(row=contador_filas+2,
                               column=10, padx=10, pady=5)

            # Crear y ubicar los botones de agregar y eliminar nodos de la lista de conexiones
            button_add = tk.Button(ventana, image=plus_icon, command=lambda combobox=nodo_combobox, conexiones=nodos[etiqueta_nodo], label_uniones=label_uniones, etiqueta_nodo=etiqueta_nodo: plus_clicked(
                combobox, conexiones, label_uniones, etiqueta_nodo))
            button_add.grid(row=contador_filas+2, column=5, padx=10, pady=5)

            button_remove = tk.Button(
                ventana, image=minus_icon, command=lambda conexiones=nodos[etiqueta_nodo], label_uniones=label_uniones: minus_clicked(conexiones, label_uniones))
            button_remove.grid(row=contador_filas+2, column=6, padx=10, pady=5)

            # Incrementar el contador de filas
            contador_filas += 1
            # Incrementa el contador de Comboboxes
            contador_comboboxes += 1
            # Incrementa el contador campos dlr
            contador_campos_dlr += 1

        actualizar_nodo_inicial_final()
        ajustar_ventana()

    else:
        for widget in ventana.grid_slaves():
            if widget.grid_info()['row'] > 1:
                widget.grid_forget()
        nodos.clear()
        contador_filas = 0
        comboboxes_manhattan.clear()
        campos_x.clear()
        campos_y.clear()
        contador_comboboxes = 0
        contador_campos_x = 0
        contador_campos_y = 0
        posiciones.clear()

        num_nodos = random.randint(1, 7)

        for i in range(num_nodos):
            etiqueta_nodo = chr(65 + i)
            nodos[etiqueta_nodo] = []

            # Crear y ubicar el nodo con su nombre
            label_nodo = tk.Label(ventana, text="Nodo " + etiqueta_nodo)
            label_nodo.grid(row=contador_filas+2, column=0, padx=10, pady=10)

            # Crear y ubicar el campo de entrada para la posición X
            label_x = tk.Label(ventana, text="Distancia X:")
            label_x.grid(row=contador_filas+2, column=1, padx=10, pady=5)
            input_x_id = f"input_x_{contador_campos_x}"
            input_x = tk.Entry(ventana, name=input_x_id)
            input_x.grid(row=contador_filas+2, column=2, padx=10, pady=5)

            # Agregar el campo de entrada X a la lista de campos_x
            campos_x.append(input_x)

            # Crear y ubicar el campo de entrada para la posición Y
            label_y = tk.Label(ventana, text="Distancia Y:")
            label_y.grid(row=contador_filas+2, column=3, padx=10, pady=5)
            input_y_id = f"input_y_{contador_campos_y}"
            input_y = tk.Entry(ventana, name=input_y_id)
            input_y.grid(row=contador_filas+2, column=4, padx=10, pady=5)

            # Agregar el campo de entrada Y a la lista de campos_y
            campos_y.append(input_y)

            # Agrego los inputs a una lista global de inputs
            posiciones[etiqueta_nodo] = [input_x, input_y]

            # Crear y ubicar el label y combo para los conexiones de los nodos
            nodos_combo_label = tk.Label(ventana, text="Conexiones:")
            nodos_combo_label.grid(row=contador_filas+2,
                                   column=5, padx=10, pady=5)
            keys = list(nodos.keys())
            combobox_id = f"combobox_{contador_comboboxes}"
            nodo_combobox = ttk.Combobox(
                ventana, values=keys, state="readonly", name=combobox_id)
            nodo_combobox.grid(row=contador_filas+2, column=6, padx=10, pady=5)

            # Agregar el Combobox recién creado a la lista global de Comboboxes
            comboboxes_manhattan.append(nodo_combobox)

            # Actualizar todos los combos de conexión de los nodos
            actualizar_comboboxes_manhattan()

            # Crear y ubicar hacia que nodos se une el nodo de la fila correspondiente
            label_conex = tk.Label(ventana, text="Uniones:")
            label_conex.grid(row=contador_filas+2, column=9, padx=10, pady=5)
            label_uniones = tk.Label(ventana, text=f"{nodos[etiqueta_nodo]}")
            label_uniones.grid(row=contador_filas+2,
                               column=10, padx=10, pady=5)

            # Crear y ubicar los botones de agregar y eliminar nodos de la lista de conexiones
            button_add = tk.Button(ventana, image=plus_icon, command=lambda combobox=nodo_combobox, conexiones=nodos[etiqueta_nodo], label_uniones=label_uniones, etiqueta_nodo=etiqueta_nodo: plus_clicked(
                combobox, conexiones, label_uniones, etiqueta_nodo))
            button_add.grid(row=contador_filas+2, column=7, padx=10, pady=5)

            button_remove = tk.Button(
                ventana, image=minus_icon, command=lambda conexiones=nodos[etiqueta_nodo], label_uniones=label_uniones: minus_clicked(conexiones, label_uniones))
            button_remove.grid(row=contador_filas+2, column=8, padx=10, pady=5)

            # Incrementar el contador de filas
            contador_filas += 1
            # Incrementa el contador de Comboboxes
            contador_comboboxes += 1
            # Incrementa el contador campos x e y
            contador_campos_x += 1
            contador_campos_y += 1

        actualizar_nodo_inicial_final()
        ajustar_ventana()


# Ventana principal distancia en linea recta
def distancia_recta_manual():
    global nodo_inicial, nodo_final
    print('distancia linea recta manual')
    limpiar_ventana()

    # Crear y ubicar botones de nodo incial y final
    keys = list(nodos.keys())
    label_nodo_inicial = tk.Label(text="Nodo Inicial:")
    label_nodo_final = tk.Label(text="Nodo Final:")
    nodo_inicial = combo_nodo_inicial = ttk.Combobox(
        ventana, values=keys, state="readonly")
    nodo_final = combo_nodo_final = ttk.Combobox(
        ventana, values=keys, state="readonly")

    # Crear y ubicar el combo nodo inicial y final
    label_nodo_inicial.grid(row=1, column=0, pady=20, padx=20)
    label_nodo_final.grid(row=1, column=2, pady=20, padx=20)
    combo_nodo_inicial.grid(row=1, column=1, pady=20, padx=20)
    combo_nodo_final.grid(row=1, column=3, pady=20, padx=20)

    # Crear y ubicar botones de agregar y quitar nodo
    boton_agregar_nodo = tk.Button(
        ventana, text="Agregar Nodo", command=lambda: agregar_nodo("dlr"))
    boton_eliminar_nodo = tk.Button(
        ventana, text="Eliminar Nodo", command=lambda: eliminar_nodo("dlr"))

    boton_agregar_nodo.grid(row=1, column=4, pady=20, padx=20)
    boton_eliminar_nodo.grid(row=1, column=5, pady=20, padx=20)

    # Crear y ubicar boton dibujar
    boton_dibujar = tk.Button(ventana, text="Dibujar",
                              command=obtener_datos_dlr_manual)
    boton_dibujar.grid(row=1, column=6, pady=20, padx=20)

    # Crear y centrar el label
    label_central = tk.Label(
        ventana, text="Distancia en Linea Recta (Manual)", font=("Helvetica", 15))
    label_central.grid(row=0, column=0, columnspan=12, pady=15)

    ajustar_ventana()


def distancia_recta_aleatoria():
    global nodo_inicial, nodo_final
    print('distancia dlr (aleatoria)')
    limpiar_ventana()

    # Crear y ubicar botones de nodo incial y final
    keys = list(nodos.keys())
    label_nodo_inicial = tk.Label(text="Nodo Inicial:")
    label_nodo_final = tk.Label(text="Nodo Final:")
    nodo_inicial = combo_nodo_inicial = ttk.Combobox(
        ventana, values=keys, state="readonly")
    nodo_final = combo_nodo_final = ttk.Combobox(
        ventana, values=keys, state="readonly")

    # Crear y ubicar el combo nodo inicial y final
    label_nodo_inicial.grid(row=1, column=0, pady=20, padx=20)
    combo_nodo_inicial.grid(row=1, column=1, pady=20, padx=20)
    label_nodo_final.grid(row=1, column=2, pady=20, padx=20)
    combo_nodo_final.grid(row=1, column=3, pady=20, padx=20)

    # Crear y ubicar botones de agregar y quitar nodo
    boton_generar_estados_aleatorios = tk.Button(
        ventana, text="Generar Estados Aleatorios", command=lambda: estados_aleatorios("dlr"))
    boton_generar_estados_aleatorios.grid(row=1, column=4, pady=20, padx=20)

    # Crear y ubicar boton dibujar
    boton_dibujar = tk.Button(ventana, text="Dibujar",
                              command=obtener_datos_dlr_aleatorios)
    boton_dibujar.grid(row=1, column=5, pady=20, padx=20)

    # Crear y centrar el label
    label_central = tk.Label(
        ventana, text="Distancia Linea Recta (Aleatorio)", font=("Helvetica", 15))
    label_central.grid(row=0, column=0, columnspan=12, pady=15)

    ajustar_ventana()


# Ventana principal distancia manhattan
def distancia_manhattan_manual():
    global nodo_inicial, nodo_final
    print('distancia manhattan (manual)')
    limpiar_ventana()

    # Crear y ubicar botones de nodo incial y final
    keys = list(nodos.keys())
    label_nodo_inicial = tk.Label(text="Nodo Inicial:")
    label_nodo_final = tk.Label(text="Nodo Final:")
    nodo_inicial = combo_nodo_inicial = ttk.Combobox(
        ventana, values=keys, state="readonly")
    nodo_final = combo_nodo_final = ttk.Combobox(
        ventana, values=keys, state="readonly")

    # Crear y ubicar el combo nodo inicial y final
    label_nodo_inicial.grid(row=1, column=0, pady=20, padx=20)
    label_nodo_final.grid(row=1, column=2, pady=20, padx=20)
    combo_nodo_inicial.grid(row=1, column=1, pady=20, padx=20)
    combo_nodo_final.grid(row=1, column=3, pady=20, padx=20)

    # Crear y ubicar botones de agregar y quitar nodo
    boton_agregar_nodo = tk.Button(
        ventana, text="Agregar Nodo", command=lambda: agregar_nodo("manhattan"))
    boton_eliminar_nodo = tk.Button(
        ventana, text="Eliminar Nodo", command=lambda: eliminar_nodo("manhattan"))

    boton_agregar_nodo.grid(row=1, column=4, pady=20, padx=20)
    boton_eliminar_nodo.grid(row=1, column=5, pady=20, padx=20)

    # Crear y ubicar boton dibujar
    boton_dibujar = tk.Button(ventana, text="Dibujar",
                              command=obtener_datos_manhattan_manual)
    boton_dibujar.grid(row=1, column=6, pady=20, padx=20)

    # Crear y centrar el label
    label_central = tk.Label(
        ventana, text="Distancia Manhattan (Manual)", font=("Helvetica", 15))
    label_central.grid(row=0, column=0, columnspan=12, pady=15)

    ajustar_ventana()


def distancia_manhattan_aleatoria():
    global nodo_inicial, nodo_final
    print('distancia manhattan (aleatorio)')
    limpiar_ventana()

    # Crear y ubicar botones de nodo incial y final
    keys = list(nodos.keys())
    label_nodo_inicial = tk.Label(text="Nodo Inicial:")
    label_nodo_final = tk.Label(text="Nodo Final:")
    nodo_inicial = combo_nodo_inicial = ttk.Combobox(
        ventana, values=keys, state="readonly")
    nodo_final = combo_nodo_final = ttk.Combobox(
        ventana, values=keys, state="readonly")

    # Crear y ubicar el combo nodo inicial y final
    label_nodo_inicial.grid(row=1, column=0, pady=20, padx=20)
    combo_nodo_inicial.grid(row=1, column=1, pady=20, padx=20)
    label_nodo_final.grid(row=1, column=2, pady=20, padx=20)
    combo_nodo_final.grid(row=1, column=3, pady=20, padx=20)

    # Crear y ubicar botones de agregar y quitar nodo
    boton_generar_estados_aleatorios = tk.Button(
        ventana, text="Generar Estados Aleatorios", command=lambda: estados_aleatorios("manhattan"))
    boton_generar_estados_aleatorios.grid(row=1, column=4, pady=20, padx=20)

    # Crear y ubicar boton dibujar
    boton_dibujar = tk.Button(ventana, text="Dibujar",
                              command=obtener_datos_manhattan_aleatorios)
    boton_dibujar.grid(row=1, column=5, pady=20, padx=20)

    # Crear y centrar el label
    label_central = tk.Label(
        ventana, text="Distancia Manhattan (Aleatorio)", font=("Helvetica", 15))
    label_central.grid(row=0, column=0, columnspan=12, pady=15)

    ajustar_ventana()


def limpiar_ventana():
    global contador_filas, nodos, contador_campos_dlr, contador_filas_manhattan, nodo_inicial, nodo_final, contador_filas_dlr, posiciones, comboboxes_dlr
    global comboboxes_manhattan, contador_comboboxes, contador_campos_x, contador_campos_y, campos_x, campos_y, campos_dlr

    # Eliminar todos los widgets de la ventana
    for widget in ventana.winfo_children():
        if widget != menu_principal:
            widget.destroy()

    contador_filas_dlr = 0
    contador_filas_manhattan = 0
    nodos.clear()
    nodo_inicial = ""
    nodo_final = ""
    posiciones.clear()
    comboboxes_dlr.clear()
    comboboxes_manhattan.clear()
    contador_comboboxes = 0
    contador_campos_x = 0
    contador_campos_y = 0
    contador_campos_dlr = 0
    campos_x.clear()
    campos_y.clear()
    campos_dlr.clear()

    # Establecer la geometría inicial de la ventana
    ventana.geometry("400x200")


def ajustar_ventana():
    # Ajustar la ventana automáticamente
    ventana.update_idletasks()
    ventana.geometry("")


def plus_clicked(nodo_combobox, conexiones, label_uniones, nodo_actual):
    selected_value = nodo_combobox.get()
    if selected_value == "":
        mb.showwarning(
            "Danger", "La conexion no puede estar vacia!", parent=ventana)
    elif selected_value in conexiones:
        mb.showwarning(
            "Danger", "El nodo ya se encuentra en la lista!", parent=ventana)
    elif selected_value == nodo_actual:
        mb.showwarning(
            "Danger", "El nodo seleccionado no puede ser el mismo que el nodo de la fila!", parent=ventana)
    else:
        conexiones.append(selected_value)
        label_uniones.config(text=conexiones)


def minus_clicked(conexiones, label_uniones):
    if len(conexiones) > 0:
        conexiones.pop()
        label_uniones.config(text=conexiones)
    else:
        mb.showwarning(
            "Danger", "No hay mas nodos en la lista!", parent=ventana)


def obtener_datos_manhattan_manual():
    if nodo_inicial.get() == "" or nodo_final.get() == "" or nodo_inicial.get() == nodo_final.get():
        return mb.showwarning("Error Nodo Inicial o Final", "Los combos de nodo inicial o final no pueden estar vacios o contener el mismo nodo", parent=ventana)

    for key, value in nodos.items():
        if not value:
            return mb.showwarning("Error Uniones", "Alguno de los nodos no contiene ninguna union a otro nodo", parent=ventana)

    for key, value in posiciones.items():
        if isinstance(value[0], tk.Entry) and isinstance(value[1], tk.Entry):
            x_value = value[0].get()
            y_value = value[1].get()
            if x_value == "" or y_value == "":
                return mb.showwarning("Error Posicion X o Y", "Alguno de los campos de entradas X o Y esta vacio", parent=ventana)
            posiciones[key] = [x_value, y_value]

    distancias = distancias_manhattan(
        nodo_final=nodo_final.get(), posiciones=posiciones)

    uniones = uniones_nodos(dict=nodos)

    info = {
        'nodo_inicial': nodo_inicial.get(),
        'nodo_final': nodo_final.get(),
        'nodos': list(nodos.keys()),
        'distancias': distancias,
        'uniones': uniones,
    }

    crear_ventana_inicial(info=info)


def obtener_datos_manhattan_aleatorios():
    if nodo_inicial.get() == "" or nodo_final.get() == "" or nodo_inicial.get() == nodo_final.get():
        return mb.showwarning("Error Nodo Inicial o Final", "Los combos de nodo inicial o final no pueden estar vacios o contener el mismo nodo", parent=ventana)

    for key, value in nodos.items():
        if not value:
            return mb.showwarning("Error Uniones", "Alguno de los nodos no contiene ninguna union a otro nodo", parent=ventana)

    valores_posiciones = {}

    for key, value in posiciones.items():
        x_value = value[0].get()
        y_value = value[1].get()
        if x_value == "" or y_value == "":
            return mb.showwarning("Error Posicion X o Y", "Alguno de los campos de entradas X o Y esta vacio", parent=ventana)
        valores_posiciones[key] = [x_value, y_value]

    distancias = distancias_manhattan(
        nodo_final=nodo_final.get(), posiciones=valores_posiciones)

    uniones = uniones_nodos(dict=nodos)

    info = {
        'nodo_inicial': nodo_inicial.get(),
        'nodo_final': nodo_final.get(),
        'nodos': list(nodos.keys()),
        'distancias': distancias,
        'uniones': uniones,
    }

    crear_ventana_inicial(info=info)


def obtener_datos_dlr_manual():
    print("dlr manual")

    if nodo_inicial.get() == "" or nodo_final.get() == "" or nodo_inicial.get() == nodo_final.get():
        return mb.showwarning("Error Nodo Inicial o Final", "Los combos de nodo inicial o final no pueden estar vacios o contener el mismo nodo", parent=ventana)

    for key, value in nodos.items():
        if not value:
            return mb.showwarning("Error Uniones", "Alguno de los nodos no contiene ninguna union a otro nodo", parent=ventana)

    for key, value in posiciones.items():
        if isinstance(value[0], tk.Entry):
            dlr_value = value[0].get()
            if dlr_value == "":
                return mb.showwarning("Error Posicion DLR", "Alguno de los campos de entradas de distancias esta vacio", parent=ventana)
            posiciones[key] = [dlr_value]

    distancias = distancias_linea_recta(
        nodo_final=nodo_final.get(), posiciones=posiciones)

    uniones = uniones_nodos(dict=nodos)

    info = {
        'nodo_inicial': nodo_inicial.get(),
        'nodo_final': nodo_final.get(),
        'nodos': list(nodos.keys()),
        'distancias': distancias,
        'uniones': uniones,
    }

    crear_ventana_inicial(info=info)


def obtener_datos_dlr_aleatorios():
    print("dlr aleatorio")

    if nodo_inicial.get() == "" or nodo_final.get() == "" or nodo_inicial.get() == nodo_final.get():
        return mb.showwarning("Error Nodo Inicial o Final", "Los combos de nodo inicial o final no pueden estar vacios o contener el mismo nodo", parent=ventana)

    for key, value in nodos.items():
        if not value:
            return mb.showwarning("Error Uniones", "Alguno de los nodos no contiene ninguna union a otro nodo", parent=ventana)

    for key, value in posiciones.items():
        if isinstance(value[0], tk.Entry):
            dlr_value = value[0].get()
            if dlr_value == "":
                return mb.showwarning("Error Posicion DLR", "Alguno de los campos de entradas de distancias esta vacio", parent=ventana)
            posiciones[key] = [dlr_value]

    distancias = distancias_linea_recta(
        nodo_final=nodo_final.get(), posiciones=posiciones)

    uniones = uniones_nodos(dict=nodos)

    info = {
        'nodo_inicial': nodo_inicial.get(),
        'nodo_final': nodo_final.get(),
        'nodos': list(nodos.keys()),
        'distancias': distancias,
        'uniones': uniones,
    }

    crear_ventana_inicial(info=info)


def cerrar_ventana():
    # Cerrar todas las ventanas y salir del programa
    ventana.quit()
    ventana.destroy()
    sys.exit()


# Instanciar la ventana
ventana = tk.Tk()
# Darle titulo a la ventana
ventana.title("Trabajo Practica Final IA 1")
# Establecer la geometría inicial de la ventana
ventana.geometry("400x200")

# MENU
# Creo el menu de la ventana
menu_principal = tk.Menu()

# Capturar el evento de cierre de la ventana principal
ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Se crean las opciones principales
menu_heuristicas = tk.Menu(menu_principal, tearoff=False)

# Agregar las opciones principales al menu
menu_principal.add_cascade(label="Heuristicas",
                           menu=menu_heuristicas)

# Submenú para la distancia en línea recta
sub_menu_linea_recta = tk.Menu(menu_heuristicas, tearoff=False)
menu_heuristicas.add_cascade(
    label="Distancia en línea recta", menu=sub_menu_linea_recta)
sub_menu_linea_recta.add_command(
    label="Manual", command=distancia_recta_manual)
sub_menu_linea_recta.add_command(
    label="Aleatorio", command=distancia_recta_aleatoria)

# Submenú para la distancia Manhattan
sub_menu_manhattan = tk.Menu(menu_heuristicas, tearoff=False)
menu_heuristicas.add_cascade(
    label="Distancia Manhattan", menu=sub_menu_manhattan)
sub_menu_manhattan.add_command(
    label="Manual", command=distancia_manhattan_manual)
sub_menu_manhattan.add_command(
    label="Aleatorio", command=distancia_manhattan_aleatoria)

# Cargar Imagenes
plus_image = Image.open("plus.png")
minus_image = Image.open("minus.png")

# Redimensionar imagenes
plus_image = plus_image.resize((15, 15))
minus_image = minus_image.resize((15, 15))

# Convertir imagenes a objectos Tkinter PhotoImage
plus_icon = ImageTk.PhotoImage(plus_image)
minus_icon = ImageTk.PhotoImage(minus_image)

# Agregar el menu a la ventana
ventana.config(menu=menu_principal)

# Iniciar el bucle de eventos principal
ventana.mainloop()
