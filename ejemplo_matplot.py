import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Definir ventana como variable global
ventana = None
frames = []



def dibujar_arbol():
    # Crear un grafo vacío
    G = nx.Graph()

    # Agregar nodos al grafo
    nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    G.add_nodes_from(nodos)

    # Agregar aristas (conexiones entre nodos)
    aristas = [('A', 'B'), ('A', 'C'), ('B', 'D'),
               ('B', 'E'), ('C', 'F'), ('C', 'G')]
    G.add_edges_from(aristas)

    # Dibujar el gráfico
    pos = nx.spring_layout(G)  # Posiciones de los nodos

    # Crear una figura de Matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Dibujar el grafo en la figura
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue',
            font_size=12, font_weight='bold', arrows=True, ax=ax)

    # Devolver la figura
    return fig


def cerrar_ventana():
    # Detener la ejecución del programa
    ventana.quit()


def crear_ventana():
    # Definir ventana como variable global
    global ventana

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
        frame_botones, text="Metodo Escalada Simple", command=mostrar_ventana_escalda_simple)
    boton_paso_a_paso.pack(fill="x", padx=10, pady=10)

    # Botón "Paso a Paso"
    boton_paso_a_paso = ttk.Button(
        frame_botones, text="Metodo Maxima Pendiente", command=mostrar_ventana_maxima_pendiente)
    boton_paso_a_paso.pack(fill="x", padx=10, pady=10)

    # Obtener información del árbol
    info = "\nInformación adicional:\n\n- Profundidad máxima: 3\n- Nodos terminales: D, E, F, G"

    # Label para la información adicional
    label_info = tk.Label(frame_info, text=info,
                          justify="left", anchor="nw")
    label_info.pack(fill="both", expand=True, padx=10, pady=10)

    # Configurar la función de cierre de ventana
    ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    # Ajustar automáticamente el tamaño de la ventana al contenido
    ventana.update_idletasks()
    ventana.geometry("+100+100")  # Mover la ventana a una posición específica
    ventana.mainloop()

# Función para crear y mostrar una ventana secundaria


def mostrar_ventana_escalda_simple():
    # Crear la ventana secundaria
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Escalada Simple")

    # Frame para el contenido de la ventana secundaria
    frame_secundario = ttk.Frame(ventana_secundaria)
    frame_secundario.pack(fill="both", expand=True)

    # Frame para el gráfico
    frame_grafico = ttk.Frame(frame_secundario, borderwidth=2, relief="solid")
    frame_grafico.pack(side="left", fill="both", expand=True)

    # Dibujar el árbol y obtener la figura
    fig = dibujar_arbol()

    # Agregar el gráfico a la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_secundario)
    canvas.draw()
    canvas.get_tk_widget().pack(side="left", fill="both", expand=True)

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
    info = "Información adicional:\n\n- Profundidad máxima: 3\n- Nodos terminales: D, E, F, G"

    # Label para la información adicional
    label_info = tk.Label(frame_info, text=info,
                          justify="left", anchor="center")
    label_info.pack(fill="both", expand=True, padx=5, pady=5)


def insertar_frame_escalada_simple(frame_contenido):
    # Frame para los botones
    frame_info = ttk.Frame(frame_contenido, borderwidth=2, relief="solid")
    frames.append(frame_info)
    frame_info.pack(side="top", fill="both")

    # Obtener información del árbol
    info = "Información de bokita adicional:\n\n- Profundidad máxima: 3\n- Nodos terminales: D, E, F, G"

    # Label para la información adicional
    label_info = tk.Label(frame_info, text=info,
                          justify="left", anchor="center")
    label_info.pack(fill="both", expand=True, padx=5, pady=5)


def eliminar_frame_escalada_simple():
    if len(frames) == 0:
        return mb.showwarning("Error Pasos", "No hay mas pasos para retroceder", parent=ventana)
    frame = frames.pop()
    frame.destroy()


def mostrar_ventana_maxima_pendiente():
    # Crear la ventana secundaria
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Maxima Pendiente")

    # Frame para el contenido de la ventana secundaria
    frame_secundario = ttk.Frame(ventana_secundaria)
    frame_secundario.pack(fill="both", expand=True)

    # Frame para el gráfico
    frame_grafico = ttk.Frame(frame_secundario, borderwidth=2, relief="solid")
    frame_grafico.pack(side="left", fill="both", expand=True)

    # Dibujar el árbol y obtener la figura
    fig = dibujar_arbol()

    # Agregar el gráfico a la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_secundario)
    canvas.draw()
    canvas.get_tk_widget().pack(side="left", fill="both", expand=True)

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
    info = "Información adicional:\n\n- Profundidad máxima: 3\n- Nodos terminales: D, E, F, G"

    # Label para la información adicional
    label_info = tk.Label(frame_info, text=info,
                          justify="left", anchor="center")
    label_info.pack(fill="both", expand=True, padx=5, pady=5)


def insertar_frame_maxima_pendiente(frame_contenido):
    # Frame para los botones
    frame_info = ttk.Frame(frame_contenido, borderwidth=2, relief="solid")
    frames.append(frame_info)
    frame_info.pack(side="top", fill="both")

    # Obtener información del árbol
    info = "Información de bokita adicional:\n\n- Profundidad máxima: 3\n- Nodos terminales: D, E, F, G"

    # Label para la información adicional
    label_info = tk.Label(frame_info, text=info,
                          justify="left", anchor="center")
    label_info.pack(fill="both", expand=True, padx=5, pady=5)


def eliminar_frame_maxima_pendiente():
    if len(frames) == 0:
        return mb.showwarning("Error Pasos", "No hay mas pasos para retroceder", parent=ventana)
    frame = frames.pop()
    frame.destroy()


# Llamar a la función para crear la ventana con el árbol y la información
crear_ventana()
