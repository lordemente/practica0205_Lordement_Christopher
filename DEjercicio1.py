divisa = {"Euro": "€", "Dollar": "$", "Yen":"¥"}

while True:
    usuario = input('Introduzca la palabra clave: "Euro, Dollar, Yen": ').capitalize()
    
    if usuario in divisa:

        simbolo = divisa[usuario]

        print(f"Divisa ingresada: {usuario} simbolo: {simbolo}")

        break
    else:
        print("Esta 'divisa' no se encuentra en la base de datos, inténtelo de nuevo")











