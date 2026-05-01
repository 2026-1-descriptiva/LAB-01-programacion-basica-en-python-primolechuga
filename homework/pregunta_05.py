"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    stats = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) < 2:
                continue
            letter = parts[0]
            value = int(parts[1])
            if letter not in stats:
                stats[letter] = [value, value]
            else:
                stats[letter][0] = max(stats[letter][0], value)
                stats[letter][1] = min(stats[letter][1], value)
    return [(letter, stats[letter][0], stats[letter][1]) for letter in sorted(stats)]
