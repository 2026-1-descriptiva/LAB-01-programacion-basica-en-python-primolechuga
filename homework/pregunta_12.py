"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    totals = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) < 5:
                continue
            letter = parts[0]
            entries = parts[4].split(",")
            row_sum = 0
            for entry in entries:
                if not entry:
                    continue
                row_sum += int(entry.split(":")[1])
            totals[letter] = totals.get(letter, 0) + row_sum
    return {key: totals[key] for key in sorted(totals)}
