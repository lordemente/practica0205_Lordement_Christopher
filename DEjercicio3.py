precio = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}

usuario = input("Introduzca algún producto: ").capitalize()

cantidad = int(input("Introduzca un número de unidades: "))

cantidad_0 = cantidad * precio[usuario] 

if usuario in precio:
    
    diccionario = precio[usuario]

    print(f"\nProducto: {usuario} precio: {diccionario}'\ncantidad: {cantidad} total: {cantidad_0}")
else:
    print("Ese producto no está disponible")