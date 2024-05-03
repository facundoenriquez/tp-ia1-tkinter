def distancias_manhattan(nodo_final, posiciones):
    posicion_final = posiciones.get(nodo_final)
    pos_x_nodo_final = int(posicion_final[0])
    pos_y_nodo_final = int(posicion_final[1])

    distancias_manhattan = {}

    for key, value in posiciones.items():
        diferencia = abs(int(value[0]) - pos_x_nodo_final) + abs(int(value[1]) - pos_y_nodo_final)
        distancias_manhattan[key] = diferencia

    return distancias_manhattan