def es_numero_armstrong(numero):
    numero_str = str(numero)
    cantidad_digitos = len(numero_str)
    suma = 0
    for digito_str in numero_str:
        digito = int(digito_str)
        suma += digito ** cantidad_digitos
    # Verificamos si la suma es igual al número original
    if suma == numero:
        return True  # El número es de Armstrong
    else:
        return False  # El número no es de Armstrong
numero = int(input("Introduce un número: "))
# Comprobamos si el número es de Armstrong
if es_numero_armstrong(numero):
    print(f"{numero} es un número de Armstrong.")
else:
    print(f"{numero} no es un número de Armstrong.")


