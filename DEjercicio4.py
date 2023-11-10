datos = {}

# contador = 0
# for i in range(1):
# while contador <1:
# while True:
print("Introduce tus datos\n")
nombre = input("¿Cuál es tu nombre y apellido?: ")
edad = input("¿Cuál es tu edad?: ")
sexo = input("¿Cuál es tu sexo?: ")
telefono = input("¿Cuál es tu número de telefono?: ")
correo = input("¿Cuál es tu número de correo electronico?: ")
    # contador += 1

datos["Nombre"] = nombre
datos["Edad"] = edad
datos["Sexo"] = sexo
datos["Telefono"] = telefono
datos["Correo electronico"] = correo

print("\nInformación actualizada")
#.items() nos muestra los datos guardados en el diccionario y también es iterable
for clave, valor in datos.items(): 
        
    print(f" {clave}: {valor}")


