han = open("mbox-short.txt")  # Lee el domcumento

for line in han:  # Por cada linea del texto
    line = line.rstrip()  # Quita espacios a la derecha
    wds = line.split()  # Divide la linea por espacios

    # Si la linea tiene menos de tres palabras (guardian) o no inicia con From, se la salta
    if len(wds) < 3 or wds[0] != "From":
        continue
    print(wds[2])  # Imprime la segunda palabra
