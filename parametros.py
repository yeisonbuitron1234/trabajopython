def obtener_parametros(url):
    parametros = {}
    inicio = -1
    for i in range(len(url)):
        if url[i] == '?':
            inicio = i
            break
    if inicio == -1:
        return parametros
    parametros_url = url[inicio + 1:]
    clave = ""
    valor = ""
    parametro = ""
    # Recorrer la parte de la URL que contiene los parámetros
    for i in range(len(parametros_url)):
        if parametros_url[i] == '=':
            clave = parametro  # La parte antes del '=' es la clave
            parametro = ""  # Limpiar la variable 'parametro' para el valor
        elif parametros_url[i] == '&':
            valor = parametro  # La parte antes del '&' es el valor
            parametros[clave] = valor  # Guardamos el parámetro en el diccionario
            parametro = ""  # Limpiar la variable 'parametro' para el siguiente parámetro
        else:
            parametro += parametros_url[i]
    if parametro:
        parametros[clave] = parametro
    return parametros
# Pedir al usuario que ingrese la URL
url = input("Introduce una URL con parámetros: ")
# Obtener los parámetros de la URL
parametros = obtener_parametros(url)
# Mostrar los parámetros encontrados
print("Parámetros obtenidos:")
for clave, valor in parametros.items():
    print(f"{clave} = {valor}")

