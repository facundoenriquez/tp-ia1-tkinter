import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def dibujar_grafo(nodos, distancias, uniones):

    nodos_principales = nodos.keys()
    # Crear Grafo Vacio
    G = nx.Graph()

    # Agregar nodos al grafo
    G.add_nodes_from(nodos_principales)

    # Agregar uniones al grafo
    G.add_edges_from(uniones)

    # Dibujar el grafo
    pos = nx.spring_layout(G)  # Posiciones de los nodos

    # Crear una figura de Matplotlib
    fig = plt.figure()

    # Dibujar el grafo en la figura
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue',
            font_size=12, font_weight='bold', ax=fig.add_subplot(111))

    crear_ventana(fig)


def crear_ventana(fig):
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Árbol y detalles")

    # Frame principal para el gráfico y la información
    frame_principal = tk.Frame(ventana, borderwidth=2, relief="solid")
    frame_principal.pack(fill="both", expand=True)

    # Frame para el gráfico
    frame_grafico = tk.Frame(frame_principal, borderwidth=2, relief="solid")
    frame_grafico.pack(side="left", fill="both", expand=True)

    # Agregar el gráfico a la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Frame para el botón y la información adicional
    frame_controles = tk.Frame(frame_principal, borderwidth=2, relief="solid")
    frame_controles.pack(side="right", fill="both", expand=True)

    # Botón "Paso a Paso"
    boton_paso_a_paso = tk.Button(frame_controles, text="Paso a Paso")
    boton_paso_a_paso.pack(fill="x", padx=10, pady=10)

    # Obtener información del árbol
    info = "\nInformación adicional:\n\n- Profundidad máxima: 3\n- Nodos terminales: D, E, F, G"

    # Label para la información adicional
    label_info = tk.Label(frame_controles, text=info,
                          justify="left", anchor="nw")
    label_info.pack(fill="both", expand=True, padx=10, pady=10)

    # Ajustar automáticamente el tamaño de la ventana al contenido
    ventana.update_idletasks()
    ventana.geometry("+100+100")  # Mover la ventana a una posición específica
    ventana.mainloop()
