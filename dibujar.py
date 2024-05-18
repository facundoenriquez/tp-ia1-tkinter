import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Definir ventana como variable global
ventana = None
frames = []
nodo_inicial = ""
nodo_final = ""
nodos = []
conexiones = []
distancias = {}

# Datos para escalada simple
estados_escalada_simple = []
nuevas_conexiones_escalada_simple = []
conexiones_escalada_simple = conexiones.copy()
canvas_escalada_simple = None
fig_escalada_simple = None
agregar_frames_escalada_simple = True
pasos_escalada_simple = 0

# Datos para maxima pendiente
estados_maxima_pendiente = []
nuevas_conexiones_maxima_pendiente = []
conexiones_maxima_pendiente = conexiones.copy()
canvas_maxima_pendiente = None
fig_maxima_pendiente = None
agregar_frames_maxima_pendiente = True
succ = []
pasos_escalada_maxima_pendiente = 0


nodo_incial_20_1 = 'A'
nodo_final_20_1 = 'F'
dlr_20_1 = {"A": 60, "B": 40, "C": 50, "D": 10, "E": 20, "F": 00}
nodos_20_1 = ['A', 'B', 'C', 'D', 'E', 'F']
uniones_20_1 = [
    ('A', 'B'), ('A', 'E'), ('A', 'D'),
    ('B', 'C'), ('B', 'E'), ('B', 'D'), ('B', 'F'),
    ('C', 'D'), ('C', 'F'),
    ('D', 'E'),
]

nodo_incial_20_2 = 'A'
nodo_final_20_2 = 'B'
dlr_20_2 = {"A": 77, "B": 00, "X": 55, "F": 12, "P": 10, "S": 22}
nodos_20_2 = ['A', 'X', 'P', 'F', 'S', 'B']
uniones_20_2 = [
    ('A', 'X'), ('A', 'P'), ('A', 'F'), ('A', 'S'),
    ('X', 'S'), ('X', 'B'), ('P', 'F'),
    ('S', 'F'), ('P', 'S'), ('S', 'B'),
]

nodo_incial_20_3 = 'A'
nodo_final_20_3 = 'G'
dlr_20_3 = {"A": 60, "B": 40, "C": 50, "D": 10, "E": 20, "F": 15, "G": 00}
nodos_20_3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
uniones_20_3 = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'),
    ('B', 'E'), ('B', 'G'), ('C', 'E'), ('C', 'F'),
    ('D', 'F'), ('E', 'F'), ('E', 'G'), ('F', 'G'),
]

nodo_incial_20_5 = 'A'
nodo_final_20_5 = 'Z'
dlr_20_5 = {"A": 60, "B": 40, "C": 33, "D": 12, "E": 25,
            "F": 15, "H": 22, "I": 44, "J": 11, "K": 44, "Z": 00}
nodos_20_5 = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'K', 'Z']
uniones_20_5 = [
    ('A', 'E'), ('A', 'D'), ('A', 'I'),
    ('E', 'C'), ('E', 'F'), ('E', 'H'),
    ('C', 'B'), ('C', 'Z'), ('I', 'J'),
    ('I', 'J'),
    ('B', 'F'), ('D', 'F'), ('D', 'J'),
    ('J', 'Z'), ('F', 'Z'), ('K', 'Z'),
    ('F', 'H'), ('H', 'K'), ('H', 'Z'),
]

nodo_incial_20_i = 'A'
nodo_final_20_i = 'Z'
dlr_20_i = {"A": 77, "E": 55, "F": 70, "D": 80, "X": 33, "Z": 00}
nodos_20_i = ['A', 'E', 'F', 'D', 'X', 'Z']
uniones_20_i = [
    ('A', 'E'), ('A', 'F'), ('A', 'D'),
    ('E', 'F'), ('E', 'X'), ('E', 'Z'),
    ('F', 'D'), ('X', 'Z'), ('D', 'Z'),
]


def dibujar_arbol():
    # Crear un grafo vacío
    G = nx.Graph()

    # Agregar nodos al grafo
    G.add_nodes_from(nodos)

    # Agregar aristas (conexiones entre nodos)
    G.add_edges_from(conexiones)

    # Dibujar el gráfico
    pos = nx.spring_layout(G, seed=1)  # Posiciones de los nodos

    # Crear una figura de Matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Asignar colores a los nodos
    node_colors = ['red' if node == nodo_inicial else 'green' if node ==
                   nodo_final else 'lightblue' for node in G.nodes()]

    # Dibujar el grafo en la figura
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color=node_colors,
            font_size=12, font_weight='bold', arrows=True, ax=ax)

    # Devolver la figura
    return fig


def cerrar_ventana():
    # Detener la ejecución del programa
    ventana.destroy()


def crear_ventana_inicial(info):
    print(info)
    # Definir ventana como variable global
    global ventana, nodo_inicial, nodo_final, nodos, distancias, conexiones
    nodo_inicial = info["nodo_inicial"]
    nodo_final = info["nodo_final"]
    nodos = info["nodos"]
    distancias = info["distancias"]
    conexiones = info["uniones"]

    # nodo_inicial = nodo_incial_20_i
    # nodo_final = nodo_final_20_i
    # nodos = nodos_20_i
    # distancias = dlr_20_i
    # conexiones = uniones_20_i

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Árbol y detalles")

    # Frame principal para el gráfico y la información
    frame_principal = ttk.Frame(ventana, borderwidth=2, relief="solid")
    frame_principal.pack(fill="both", expand=True)

    # Frame para el gráfico
    frame_grafico = ttk.Frame(frame_principal, borderwidth=2, relief="solid")
    frame_grafico.pack(side="left", fill="both", expand=True)

    # Dibujar el árbol y obtener la figura
    fig = dibujar_arbol()

    # Agregar el gráfico a la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Frame para la información adicional
    frame_info = ttk.Frame(frame_principal, borderwidth=2, relief="solid")
    frame_info.pack(side="right", fill="both", expand=True)

    # Frame para el botón
    frame_botones = ttk.Frame(frame_info, borderwidth=2, relief="solid")
    frame_botones.pack(side="top", fill="both")

    # Botón "Paso a Paso"
    boton_paso_a_paso = ttk.Button(
        frame_botones, text="Metodo Escalada Simple", command=mostrar_ventana_escalada_simple)
    boton_paso_a_paso.pack(fill="x", padx=10, pady=10)

    # Botón "Paso a Paso"
    boton_paso_a_paso = ttk.Button(
        frame_botones, text="Metodo Maxima Pendiente", command=mostrar_ventana_maxima_pendiente)
    boton_paso_a_paso.pack(fill="x", padx=10, pady=10)

    # Obtener información del árbol
    info = f"\n nodo inicial: {nodo_inicial} \n nodo final: {nodo_final}"

    # Label para la información adicional
    label_info = tk.Label(frame_info, text=info,
                          justify="left", anchor="nw")
    label_info.pack(fill="both", expand=True, padx=10, pady=10)

    # Configurar la función de cierre de ventana
    # ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    # Ajustar automáticamente el tamaño de la ventana al contenido
    ventana.update_idletasks()
    ventana.geometry("+100+100")  # Mover la ventana a una posición específica
    ventana.mainloop()


# FUNCIONES DE ESCALADA SIMPLE
def mostrar_ventana_escalada_simple():
    global estados_escalada_simple, nuevas_conexiones_escalada_simple, conexiones_escalada_simple, canvas_escalada_simple, fig_escalada_simple

    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Escalada Simple")

    # Establecer la ventana principal como maestra de la ventana secundaria
    ventana_secundaria.transient(ventana)

    # Frame para el contenido de la ventana secundaria
    frame_secundario = ttk.Frame(ventana_secundaria)
    frame_secundario.pack(fill="both", expand=True)

    # Frame para el gráfico
    frame_grafico = ttk.Frame(frame_secundario, borderwidth=2, relief="solid")
    frame_grafico.pack(side="left", fill="both", expand=True)

    # Reiniciar la lista de estados_escalada_simple para abrir una ventana nueva
    estados_escalada_simple = []
    nuevas_conexiones_escalada_simple = []
    conexiones_escalada_simple = conexiones.copy()
    canvas_escalada_simple = None
    fig_escalada_simple = None

    # Dibujar el árbol y obtener la figura
    fig_escalada_simple = dibujar_arbol_escalada_simple()

    # Crear el canvas si no existe
    if canvas_escalada_simple is None:
        canvas_escalada_simple = FigureCanvasTkAgg(
            fig_escalada_simple, master=frame_secundario)
        canvas_escalada_simple.draw()
        canvas_escalada_simple.get_tk_widget().pack(
            side="left", fill="both", expand=True)
    else:
        # Actualizar el contenido del canvas
        canvas_escalada_simple.figure = fig_escalada_simple
        canvas_escalada_simple.draw()

    # Frame para la información adicional y los botones
    frame_contenido = ttk.Frame(
        frame_secundario, borderwidth=2, relief="solid")
    frame_contenido.pack(side="right", fill="both")

    # Frame para los botones
    frame_botones = ttk.Frame(frame_contenido, borderwidth=2, relief="solid")
    frame_botones.pack(side="top", fill="both")

    # Botón "Paso a Paso"
    boton_paso_a_paso = ttk.Button(
        frame_botones, text="Anterior", command=eliminar_frame_escalada_simple)
    boton_paso_a_paso.pack(fill="x", padx=10, pady=10)
    boton_paso_a_paso = ttk.Button(
        frame_botones, text="Siguiente", command=lambda: insertar_frame_escalada_simple(frame_contenido))
    boton_paso_a_paso.pack(fill="x", padx=10, pady=10)

    # Frame para los botones
    frame_info = ttk.Frame(frame_contenido, borderwidth=2, relief="solid")
    frames.append(frame_info)
    frame_info.pack(side="top", fill="both")

    # Obtener información del árbol
    info = f"Estado Inicial: {estados_escalada_simple}"

    # Label para la información adicional
    label_info = tk.Label(frame_info, text=info,
                          justify="left", anchor="center")
    label_info.pack(fill="both", expand=True, padx=5, pady=5)


def dibujar_arbol_escalada_simple(fig=None):
    global G, node_colors, pos, agregar_frames_escalada_simple
    if nodo_inicial == nodo_final:
        return mb.showwarning("Se llego al objetivo", "El estado inicial es igual al estado objetivo")
    if len(estados_escalada_simple) == 0:
        agregar_frames_escalada_simple = True

        # Crear un grafo vacío
        G = nx.Graph()

        # Agregar nodos al grafo
        G.add_nodes_from(nodo_inicial)

        print(nodo_inicial)

        # Dibujar el gráfico
        pos = nx.spring_layout(G, seed=1)  # Posiciones de los nodos

        fig = plt.figure()

        ax = fig.add_subplot(111)

        # Dibujar el grafo en la figura
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color='red',
                font_size=12, font_weight='bold', arrows=True, ax=ax)

        estados_escalada_simple.append(nodo_inicial)

        # Devolver la figura
        return fig
    else:
        agregar_frames_escalada_simple = True

        # Estado actual utilizamos para marcar el camino hacia el nodo objetivo o para ver si hay algun min/max local
        estado_actual = estados_escalada_simple[-1]

        if estado_actual == nodo_final:
            node_colors = ['red' if node == nodo_inicial else 'green' if node ==
                           nodo_final else 'lightblue' for node in G.nodes()]
            conexiones = [(estados_escalada_simple[i], estados_escalada_simple[i+1])
                          for i in range(len(estados_escalada_simple)-1)]

            print(conexiones)

            # Usa la función esta_en_camino para determinar los colores de los edges
            edge_colors = [
                'lightblue' if con in conexiones else 'black' for con in nuevas_conexiones_escalada_simple]

            print(edge_colors)

            pos = nx.spring_layout(G, seed=1)  # Posiciones de los nodos
            fig = plt.figure()
            ax = fig.add_subplot(111)
            nx.draw(G, pos, with_labels=True, node_size=1000, node_color=node_colors, edge_color=edge_colors,
                    font_size=12, font_weight='bold', arrows=True, ax=ax)
            mb.showwarning("Objetivo Encontrado", f"El estado {
                           estado_actual} es el objetivo")
            agregar_frames_escalada_simple = False
            return fig

        conex_estado_actual = []
        print(f"Estado actual: {estado_actual}")
        for con in conexiones_escalada_simple:
            if con[0] == estado_actual and con[1] not in estados_escalada_simple:
                conex_estado_actual.append(con[1])
            elif con[1] == estado_actual and con[0] not in estados_escalada_simple:
                conex_estado_actual.append(con[0])

        print(f"conex al estado actual: {conex_estado_actual}")

        if not conex_estado_actual:
            ultimo_nodo = estados_escalada_simple[-1]
            node_colors[list(G.nodes()).index(ultimo_nodo)] = 'yellow'
            pos = nx.spring_layout(G, seed=1)  # Posiciones de los nodos
            fig = plt.figure()
            ax = fig.add_subplot(111)
            nx.draw(G, pos, with_labels=True, node_size=1000, node_color=node_colors,
                    font_size=12, font_weight='bold', arrows=True, ax=ax)
            mb.showwarning("Minimo Local", f"El estado {
                           estado_actual} es un minimo local")
            agregar_frames_escalada_simple = False
            return fig

        obtener_nodo_alfabeticamente = min(
            conex_estado_actual, key=lambda x: x)

        print(f"nodo alfabeticamente: {obtener_nodo_alfabeticamente}")

        nueva_conexion = (estado_actual, obtener_nodo_alfabeticamente)
        nueva_conexion_inversa = (obtener_nodo_alfabeticamente, estado_actual)

        # nuevas_conexiones_escalada_simple son las aristas del grafo
        nuevas_conexiones_escalada_simple.append(nueva_conexion)

        print(f"nuevas conex escalada: {nuevas_conexiones_escalada_simple}")

        if nueva_conexion in conexiones_escalada_simple:
            conexiones_escalada_simple.remove(nueva_conexion)
        elif nueva_conexion_inversa in conexiones_escalada_simple:
            conexiones_escalada_simple.remove(nueva_conexion_inversa)

        print(f'conexiones escalada: {conexiones_escalada_simple}')

        if distancias[obtener_nodo_alfabeticamente] < distancias[estado_actual]:
            estados_escalada_simple.append(obtener_nodo_alfabeticamente)

        print(f"estados escalada simple: {estados_escalada_simple}")

        nodos_a_graficar = [
            nodo for conexion in nuevas_conexiones_escalada_simple for nodo in conexion]
        nodos_a_graficar = list(set(nodos_a_graficar))

        print(f"Nodos a graficar: {nodos_a_graficar}")
        print(f"Nuevas conexiones: {nuevas_conexiones_escalada_simple} \n")

        # Crear un grafo con las nuevas conexiones
        G = nx.Graph()
        G.add_nodes_from(nodos_a_graficar)
        G.add_edges_from(nuevas_conexiones_escalada_simple)

        # Dibujar el grafo
        pos = nx.spring_layout(G, seed=1)  # Posiciones de los nodos

        fig = plt.figure()

        ax = fig.add_subplot(111)

        node_colors = ['red' if node ==
                       nodo_inicial else 'lightblue' for node in G.nodes()]
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color=node_colors,
                font_size=12, font_weight='bold', arrows=True, ax=ax)

        # Devolver la nueva figura
        return fig


def insertar_frame_escalada_simple(frame_contenido):
    global fig_escalada_simple, canvas_escalada_simple, agregar_frames_escalada_simple

    if agregar_frames_escalada_simple:
        # Frame para los botones
        frame_info = ttk.Frame(frame_contenido, borderwidth=2, relief="solid")
        frames.append(frame_info)
        frame_info.pack(side="top", fill="both")

        # Obtener información del árbol
        info = f"Paso: {pasos_escalada_simple +
                        1} \n Estados:\n- {estados_escalada_simple}"

        # Label para la información adicional
        label_info = tk.Label(frame_info, text=info,
                              justify="left", anchor="center")
        label_info.pack(fill="both", expand=True, padx=5, pady=5)

    # Dibujar el árbol y obtener la figura actualizada
    fig_escalada_simple = dibujar_arbol_escalada_simple(fig_escalada_simple)

    # Actualizar la figura en el canvas
    canvas_escalada_simple.figure = fig_escalada_simple
    canvas_escalada_simple.draw()


def eliminar_frame_escalada_simple():
    if len(frames) == 0:
        return mb.showwarning("Error Pasos", "No hay mas pasos para retroceder", parent=ventana)
    frame = frames.pop()
    frame.destroy()


# FUNCIONES DE MAXIMA PENDIENTE
def mostrar_ventana_maxima_pendiente():
    global estados_maxima_pendiente, nuevas_conexiones_maxima_pendiente, conexiones_maxima_pendiente, canvas_maxima_pendiente, fig_maxima_pendiente, succ

    # Crear la ventana secundaria
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Maxima Pendiente")

    # Establecer la ventana principal como maestra de la ventana secundaria
    ventana_secundaria.transient(ventana)

    # Frame para el contenido de la ventana secundaria
    frame_secundario = ttk.Frame(ventana_secundaria)
    frame_secundario.pack(fill="both", expand=True)

    # Frame para el gráfico
    frame_grafico = ttk.Frame(frame_secundario, borderwidth=2, relief="solid")
    frame_grafico.pack(side="left", fill="both", expand=True)

    # Reiniciar la lista de estados_maxima_pendiente para abrir una ventana nueva
    estados_maxima_pendiente = []
    nuevas_conexiones_maxima_pendiente = []
    conexiones_maxima_pendiente = conexiones.copy()
    canvas_maxima_pendiente = None
    fig_maxima_pendiente = None
    succ = []

    # Dibujar el árbol y obtener la figura
    fig_maxima_pendiente = dibujar_arbol_maxima_pendiente()

    # Crear el canvas si no existe
    if canvas_maxima_pendiente is None:
        canvas_maxima_pendiente = FigureCanvasTkAgg(
            fig_maxima_pendiente, master=frame_secundario)
        canvas_maxima_pendiente.draw()
        canvas_maxima_pendiente.get_tk_widget().pack(
            side="left", fill="both", expand=True)
    else:
        # Actualizar el contenido del canvas
        canvas_maxima_pendiente.figure = fig_maxima_pendiente
        canvas_maxima_pendiente.draw()

    # Frame para la información adicional y los botones
    frame_contenido = ttk.Frame(
        frame_secundario, borderwidth=2, relief="solid")
    frame_contenido.pack(side="right", fill="both")

    # Frame para los botones
    frame_botones = ttk.Frame(frame_contenido, borderwidth=2, relief="solid")
    frame_botones.pack(side="top", fill="both")

    # Botón "Paso a Paso"
    boton_paso_a_paso = ttk.Button(
        frame_botones, text="Anterior", command=eliminar_frame_maxima_pendiente)
    boton_paso_a_paso.pack(fill="x", padx=10, pady=10)
    boton_paso_a_paso = ttk.Button(
        frame_botones, text="Siguiente", command=lambda: insertar_frame_maxima_pendiente(frame_contenido))
    boton_paso_a_paso.pack(fill="x", padx=10, pady=10)

    # Frame para los botones
    frame_info = ttk.Frame(frame_contenido, borderwidth=2, relief="solid")
    frames.append(frame_info)
    frame_info.pack(side="top", fill="both")

    # Obtener información del árbol
    info = f"Estado Inicial: {estados_maxima_pendiente}"

    # Label para la información adicional
    label_info = tk.Label(frame_info, text=info,
                          justify="left", anchor="center")
    label_info.pack(fill="both", expand=True, padx=5, pady=5)


def dibujar_arbol_maxima_pendiente(fig=None):
    global G, node_colors, pos, agregar_frames_maxima_pendiente
    if nodo_inicial == nodo_final:
        return mb.showwarning("Se llego al objetivo", "El estado inicial es igual al estado objetivo")
    if len(estados_maxima_pendiente) == 0:
        agregar_frames_maxima_pendiente = True

        # Crear un grafo vacío
        G = nx.Graph()

        # Agregar nodos al grafo
        G.add_nodes_from(nodo_inicial)

        print(nodo_inicial)

        # Dibujar el gráfico
        pos = nx.spring_layout(G, seed=1)  # Posiciones de los nodos

        fig = plt.figure()

        ax = fig.add_subplot(111)

        # Dibujar el grafo en la figura
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color='red',
                font_size=12, font_weight='bold', arrows=True, ax=ax)

        estados_maxima_pendiente.append(nodo_inicial)

        # Devolver la figura
        return fig
    else:
        agregar_frames_maxima_pendiente = True

        # Estado actual utilizamos para marcar el camino hacia el nodo objetivo o para ver si hay algun min/max local
        estado_actual = estados_maxima_pendiente[-1]

        if estado_actual == nodo_final:
            node_colors = ['red' if node == nodo_inicial else 'green' if node ==
                           nodo_final else 'lightblue' for node in G.nodes()]
            conexiones = [(estados_maxima_pendiente[i], estados_maxima_pendiente[i+1])
                          for i in range(len(estados_maxima_pendiente)-1)]

            print(conexiones)

            # Usa la función esta_en_camino para determinar los colores de los edges
            edge_colors = [
                'lightblue' if con in conexiones else 'black' for con in nuevas_conexiones_maxima_pendiente]

            print(edge_colors)

            pos = nx.spring_layout(G, seed=1)  # Posiciones de los nodos
            fig = plt.figure()
            ax = fig.add_subplot(111)
            nx.draw(G, pos, with_labels=True, node_size=1000, node_color=node_colors, edge_color=edge_colors,
                    font_size=12, font_weight='bold', arrows=True, ax=ax)
            mb.showwarning("Objetivo Encontrado", f"El estado {
                           estado_actual} es el objetivo")
            agregar_frames_maxima_pendiente = False
            return fig

        conex_estado_actual = []
        print(f"Estado actual: {estado_actual}")
        for con in conexiones_maxima_pendiente:
            if con[0] == estado_actual and con[1] not in estados_maxima_pendiente:
                conex_estado_actual.append(con[1])
                if con[0] == estado_actual and con[1] not in succ:
                    succ.append(con[1])
            elif con[1] == estado_actual and con[0] not in estados_maxima_pendiente:
                conex_estado_actual.append(con[0])
                if con[1] == estado_actual and con[0] not in succ:
                    succ.append(con[0])

        print(f"conex al estado actual: {conex_estado_actual}")
        print(f"sucesores : {succ}")

        for con in conex_estado_actual:
            nueva_conexion = (estado_actual, con)
            nueva_conexion_inversa = (con, estado_actual)

            # nuevas_conexiones_maxima_pendiente son las aristas del grafo
            nuevas_conexiones_maxima_pendiente.append(nueva_conexion)

            if nueva_conexion in conexiones_maxima_pendiente:
                conexiones_maxima_pendiente.remove(nueva_conexion)
            elif nueva_conexion_inversa in conexiones_maxima_pendiente:
                conexiones_maxima_pendiente.remove(nueva_conexion_inversa)

        print(f"nuevas conex maxima pendiente: {
              nuevas_conexiones_maxima_pendiente}")

        print(f'conexiones maxima pendiente: {conexiones_maxima_pendiente}')

        filtered_data = {
            key: distancias[key] for key in conex_estado_actual if key in distancias}

        # if not filtered_data:

        min_key = min(filtered_data, key=filtered_data.get)

        if distancias[min_key] < distancias[estado_actual]:
            succ.remove(min_key)
            estados_maxima_pendiente.append(min_key)

        print(f"estados escalada simple: {estados_maxima_pendiente}")
        print(f"sucesores : {succ}")

        nodos_a_graficar = [
            nodo for conexion in nuevas_conexiones_maxima_pendiente for nodo in conexion]
        nodos_a_graficar = list(set(nodos_a_graficar))

        print(f"Nodos a graficar: {nodos_a_graficar}")
        print(f"Nuevas conexiones: {nuevas_conexiones_maxima_pendiente} \n")

        # Crear un grafo con las nuevas conexiones
        G = nx.Graph()
        G.add_nodes_from(nodos_a_graficar)
        G.add_edges_from(nuevas_conexiones_maxima_pendiente)

        # Dibujar el grafo
        pos = nx.spring_layout(G, seed=1)  # Posiciones de los nodos

        fig = plt.figure()

        ax = fig.add_subplot(111)

        node_colors = ['red' if node ==
                       nodo_inicial else 'lightblue' for node in G.nodes()]
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color=node_colors,
                font_size=12, font_weight='bold', arrows=True, ax=ax)

        # Devolver la nueva figura
        return fig


def insertar_frame_maxima_pendiente(frame_contenido):
    global fig_maxima_pendiente, canvas_maxima_pendiente, agregar_frames_maxima_pendiente

    if agregar_frames_maxima_pendiente:
        # Frame para los botones
        frame_info = ttk.Frame(frame_contenido, borderwidth=2, relief="solid")
        frames.append(frame_info)
        frame_info.pack(side="top", fill="both")

        # Obtener información del árbol
        info = f"Estados:\n- {estados_maxima_pendiente}"

        # Label para la información adicional
        label_info = tk.Label(frame_info, text=info,
                              justify="left", anchor="center")
        label_info.pack(fill="both", expand=True, padx=5, pady=5)

    # Dibujar el árbol y obtener la figura actualizada
    fig_maxima_pendiente = dibujar_arbol_maxima_pendiente(fig_maxima_pendiente)

    # Actualizar la figura en el canvas
    canvas_maxima_pendiente.figure = fig_maxima_pendiente
    canvas_maxima_pendiente.draw()


def eliminar_frame_maxima_pendiente():
    if len(frames) == 0:
        return mb.showwarning("Error Pasos", "No hay mas pasos para retroceder", parent=ventana)
    frame = frames.pop()
    frame.destroy()
