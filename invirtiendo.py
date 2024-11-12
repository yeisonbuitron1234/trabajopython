def invertir_cadena(cadena):
    cadena_invertida = ""
    
    for i in range(len(cadena) - 1, -1, -1):
        cadena_invertida += cadena[i]
    
    return cadena_invertida

# Pedir al usuario que ingrese una cadena de texto
texto = input("Introduce tu texto: ")

texto_invertido = invertir_cadena(texto)

print(f"La cadena invertida es: {texto_invertido}")

