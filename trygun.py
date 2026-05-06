# try:
#     edad=int(input("Ingresa tu edad: "))
# except ValueError as mostrarError:
#     print("Solo debe ingresar numeros enteros")
#     print(mostrarError)

while True:
    try:
        edad=int(input("Ingresa tu edad: "))
    except ValueError as mostrarError:
        print("Solo debe ingresar numeros enteros")