def distancias_manhattan(nodo_final, posiciones):
    pos_x_nodo_final = 0
    pos_y_nodo_final = 0

    distancias_manhattan = {}

    for key, value in posiciones.items():
        if key == nodo_final:
            distancias_manhattan[key] = 0
        else:
            diferencia = abs(int(value[0]) - pos_x_nodo_final) + \
                abs(int(value[1]) - pos_y_nodo_final)
            distancias_manhattan[key] = diferencia

    return distancias_manhattan


def distancias_linea_recta(nodo_final, posiciones):

    pos_nodo_final = 0

    distancias_linea_recta = {}

    for key, value in posiciones.items():
        if key == nodo_final:
            distancias_linea_recta[key] = 0
        else:
            diferencia = abs(int(value[0]) - pos_nodo_final)
            distancias_linea_recta[key] = diferencia

    return distancias_linea_recta
