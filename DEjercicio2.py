
nombre = input("Introduzca su nombre: ")
Edad = input("Introduzca su edad: ")
Direccion = input("Introduzca su dirección: ")
Telefono = input("Introduzca su número telefóno: ")


diccionario = {"nombre": nombre, "Edad": Edad, "Direccion": Direccion, "Telefono": Telefono}

print(f'Nombre: {diccionario["nombre"]}, Edad: {diccionario["Edad"]}, Dirección: {diccionario["Direccion"]}, Teléfono: {diccionario["Telefono"]}')

for i in diccionario:
    b = str(diccionario)
    print(i, end=(b))