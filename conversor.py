def convertir_a_milisegundos(dias, horas, minutos, segundos):
    milisegundos = 0
    milisegundos += dias * 24 * 60 * 60 * 1000
    milisegundos += horas * 60 * 60 * 1000
    milisegundos += minutos * 60 * 1000
    milisegundos += segundos * 1000
    
    return milisegundos

# Ejemplo de uso
dias = 1
horas = 2
minutos = 30
segundos = 45

resultado = convertir_a_milisegundos(dias, horas, minutos, segundos)
print(f"El total en milisegundos es: {resultado} ms")
