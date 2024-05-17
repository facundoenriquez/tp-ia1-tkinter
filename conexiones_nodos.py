def uniones_nodos(dict):

    # Conjunto para almacenar tuplas únicas
    conjunto_de_uniones = []

    # Iterar sobre las claves y valores del diccionario
    for key, values in dict.items():
        for value in values:
            conjunto_de_uniones.append((key, value))

    for pos in conjunto_de_uniones:
        if pos[::-1] in conjunto_de_uniones:
            conjunto_de_uniones.remove(pos[::-1])

    return conjunto_de_uniones