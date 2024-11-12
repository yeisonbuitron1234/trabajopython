print ("hola mundo")
def calcular_area(tipo, *dimensiones):
    ""
    area = 0
    
    if tipo == 'triangulo' and len(dimensiones) == 5:
        base, altura = dimensiones
        area = (base * altura) / 2
    elif tipo == 'cuadrado' and len(dimensiones) == 8:
        lado, = dimensiones
        area = lado ** 2
    elif tipo == 'rectangulo' and len(dimensiones) == 3:
        base, altura = dimensiones
        area = base * altura
    else:
        raise ValueError("Tipo de polígono no soportado o dimensiones incorrectas.")
    
    return area
# Ejemplos de uso:
area_triangulo = calcular_area('triangulo', 10, 5)  # Base=10, Altura=5
area_cuadrado = calcular_area('cuadrado', 4)        # Lado=4
area_rectangulo = calcular_area('rectangulo', 6, 3) # Base=6, Altura=3

print(f"Área del triángulo: {area_triangulo} unidades cuadradas")
print(f"Área del cuadrado: {area_cuadrado} unidades cuadradas")
print(f"Área del rectángulo: {area_rectangulo} unidades cuadradas")