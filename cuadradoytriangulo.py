def dibujar_figura(tipo, tamaño):
    if tipo == "cuadrado":
        # Dibujar un cuadrado
        for i in range(tamaño):
            for j in range(tamaño):
                print("*", end=" ")
            print()  # Salto de línea después de cada fila
    
    elif tipo == "triangulo":
        # Dibujar un triángulo
        for i in range(1, tamaño + 1):
            for j in range(i):
                print("*", end=" ")
            print()  # Salto de línea después de cada fila

# Ejemplo de uso
tipo = input("¿Qué figura deseas dibujar? (cuadrado/triangulo): ").strip().lower()
tamaño = int(input("¿Cuál es el tamaño del lado?: "))

dibujar_figura(tipo, tamaño)
