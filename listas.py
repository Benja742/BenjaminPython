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
def mostar_productos():
    for p in range(len(productos)):
        print(f"{p+1}.- {productos[p]}")
def eliminar_productos():
    try:
        print("-"*20)
        elim=int(input("¿Cual elemento quiere remover? "))
        productos.pop(elim-11)
    except:
        print("Producto no encontrado")
def agregar_productos():
    nombre=input("Ingrese el nombre del producto: ")
    precio=int(input("Ingrese el precio del producto: "))
    nuevo_producto={"nombre":nombre, "precio":precio}
    productos.append(nuevo_producto)
def actualizar_productos():
    print("-"*20)
    mostar_productos()
    actualizar=int(input("¿Cual producto quiere actualizar?"))
    productos[actualizar-1] =input("Ingrese el nuevo nombre: ")

while True:
    print("-"*20)
    print("1.- Agregar producto")
    print("2.- Mostrar productos")
    print("3.- Eliminar producto")
    print("4.- Actializar producto")
    print("5.- Salir")
    op=int(input("Seleccione una opcion: "))
    match op:
        case 1:
            agregar_productos()
        case 2:
            mostar_productos()
        case 3:
            eliminar_productos()
        case 4:
            actualizar_productos()
        case 5:
            print("Saliendo")
            break
        case _:
            print("Opcion invalida")