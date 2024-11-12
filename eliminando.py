def comparar_cadenas(str1, str2):
    out1 = ""  # Caracteres en str1 pero no en str2
    out2 = ""  # Caracteres en str2 pero no en str1

    for char1 in str1:
        if char1 not in str2:
            out1 += char1
    for char2 in str2:
        if char2 not in str1:
            out2 += char2
    
    # Imprimir los resultados
    print(f"out1: {out1}")
    print(f"out2: {out2}")

# Ejemplo de uso
str1 = "hola"
str2 = "mundo"
comparar_cadenas(str1, str2)

