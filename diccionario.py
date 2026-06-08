# # uso u explicacion de diccionarios

# alumno={
#     "nombre":"Shinji Ikari",
#     "edad":14,
#     "carrera":"piloto"
# }

# print(alumno)
# print(alumno["carrera"])

# for key, value in alumno.items():
#     print(f"{key}={value}")

# print("--- Cambios de datos ---")

# # for dato, valor in alumno.items():
# #     print(dato, valor)

# alumno["email"]="Shinji@nerv.com"
# alumno["carrera"]="escritor"
# del alumno["edad"]
# for key, value in alumno.items():
#     print(f"{key}={value}")

productos={
    1:{"nombre": "Control inalambrico",
       "categoria": "Electronica",
       "precio": 45000},
    2:{"nombre": "Pilas recargables",
       "categoria": "Insumos",
       "precio": 5000},
    3:{"nombre": "Pasta termica",
       "categoria": "Computacion",
       "precio": 7000}
}

# print(productos[1]["nombre"])


vegetales={
   1:"Maracuya",
   2:"Pera",
   3:"Cebolla",
   4:"Papa"
}


# for num, nombre in vegetales.items():
#    print(f"{num}.- {nombre}")

# vegetales[5]="Palta"
# print("."*40)
# for num, nombre in vegetales.items():
#    print(f"{num}.- {nombre}")

def AgregarVegetal():
   print("."*40)
   agregar=input("Ingrese un vegetal: ")
   nevokey=list(vegetales.keys())[-1]
   vegetales[nevokey+1]=agregar
   print("."*40)

def MostrarVegetales():
   print("."*40)
   for num, nombre in vegetales.items():
      print(f"{num}.- {nombre}")
   print("."*40)

def EliminarVegetal():
   MostrarVegetales()
   elim=int(input("Cual vegetal eliminara?: "))
   del vegetales[elim]
   print("."*40)

def ActualizarVegetal():
   MostrarVegetales()
   act=int(input("Cual vegetal Actulaizara?: "))
   vegetales[act]=input("Ingrese nuevo nombre: ")
   print("Actualizado")
   print("."*40)

def VegetalesMenu():
   while True:
      try:
         print("."*40)
         print("1.- Agregar Vegetal")
         print("2.- Eliminar Vegetal")
         print("3.- Actualizar Vegetal")
         print("4.- Mostrar Vegetales")
         print("5.- Salir")
         op=int(input("Seleccione una opcion: "))
         match op:
            case 1:
               AgregarVegetal()
            case 2:
               EliminarVegetal()
            case 3:
               ActualizarVegetal()
            case 4:
               MostrarVegetales()
            case 5:
               print("Saliendo del programa")
               break
            case _:
               print("Opcion invalida")
      except Exception as e:
         print("Error",e)
# VegetalesMenu()


productosDicc={
   1:{"nombre":"Maracuya","precio": 3000},
   2:{"nombre":"Pera","precio": 1500},
   3:{"nombre":"Cebolla","precio": 1200}
}
productosDicc[4]={"nombre":"Piña","precio": 3500}

productoslist=[
   {"nombre:": "Maracuya", "precio": 3000},
   {"nombre:": "Pera", "precio": 1500},
   {"nombre:": "Cebolla", "precio": 1200}
]


def AgregarProductos():
   Nombre=input("Agrege nombre producto: ")
   precio=int(input("Agrege precio producto: "))
   nevokey=list(productosDicc.keys())[-1]
   productosDicc[nevokey+1]={"nombre": Nombre, "precio": precio}

def MostrarProductos():
   for key,producto in productosDicc.items():
      print(f"{key} .-{producto}")

def EliminarProductos():
   MostrarProductos()
   elim=int(input("Cual producto eliminara?: "))
   del productosDicc[elim]

def ActualizarProductos():
   MostrarProductos()
   act=int(input("Cual producto Actulaizara?: "))
   Nombre=input("Agrege nombre producto: ")
   precio=int(input("Agrege precio producto: "))
   productosDicc[act]={"nombre": Nombre, "precio": precio}
   print("Actualizado")

def VegetalesMenuDiccionario():
   while True:
      try:
         print("."*20)
         print("1.- Agregar Producto")
         print("2.- Eliminar Producto")
         print("3.- Actualizar Producto")
         print("4.- Mostrar Producto")
         print("5.- Salir")
         op=int(input("Seleccione una opcion: "))
         match op:
            case 1:
               AgregarProductos()
            case 2:
               EliminarProductos()
            case 3:
               ActualizarProductos()
            case 4:
               MostrarProductos()
            case 5:
               print("Saliendo del programa")
               break
            case _:
               print("Opcion invalida")
      except Exception as e:
         print("Error",e)
VegetalesMenuDiccionario()