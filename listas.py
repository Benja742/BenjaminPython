# Explicacion y uso de listas

# lista=[8, 20, 12, 87, 1024]
#      0  1    2  3     4

# print(lista)
# print(lista[4])
# for i in lista:
#     print("numero:",i)


# Crear una lista de 4 frutas
# Mostrar cada elemento individualmente

# frutas=["Platano", "Manzana", "Frambuesa", "Frutilla"]
# print(frutas[3][0])
# vocales="aeiou"
# for f in frutas:
#     if f[0].lower in vocales:
#         print(f"La fruta {f} comienza con vocal")
#     else:
#         print(f"La fruta {f} NO comienza con vocales")


# Hacer una lista de nombres y otra de apellidos
# mostrar las listas como si fueran nombres
# vale decir, Diego Robles, Adolfo Hinako, Luis Mussolini

# nombres=["Diego", "Julian", "Sebastian"]
# apellidos=["Robles", "Colon", "Afton"]

# for n in range(len(nombres)):
#     print(nombres[n], apellidos[n])

# la lisra puede tener datos disparejos
# dates=[4, 6.9, "Alonsonic", False]

# for d in dates:
#     print(d)

# matrix=[
#     [5,8,3],[79,"Link",24]
# ]
# print(matrix)
# print(matrix[1])
# print(matrix[1][2])

'''
Modificar el programa del carrito de compras
para poder utilizarlo con listas
el producto debe tener nombre y precio
'''

productos=[]
while True:
    print("1.- Agregar producto")
    print("2.- Mostrar productos")
    print("3.- Eliminar producto")
    print("4.- Actializar producto")
    print("5.- Salir")
    op=int(input("Seleccione una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese el nombre del producto: ")
            precio=int(input("Ingrese el precio del producto: "))
            nuevo_producto={"nombre":nombre, "precio":precio}
            productos.append(nuevo_producto)
        case 2:
            print(productos)
        case 3:
            print("")
        case 4:
            print("")
        case 5:
            print("Saliendo")
            break
        case _:
            print("Opcion invalida")