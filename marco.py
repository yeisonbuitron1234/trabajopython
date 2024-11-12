def mostrar_marco(texto):
    palabras = texto.split()
    max_largo = 0
    for palabra in palabras:
        if len(palabra) > max_largo:
            max_largo = len(palabra)
    print('*' * (max_largo + 4))  # +4 para los espacios a cada lado
    for palabra in palabras:
        print('*', palabra.ljust(max_largo), '*')  # Alineamos las palabras a la izquierda y agregamos los bordes
    print('*' * (max_largo + 4))

# Pedir al usuario que ingrese un texto
texto = input("Introduce un texto: ")
# Mostrar el texto dentro del marco
mostrar_marco(texto)
