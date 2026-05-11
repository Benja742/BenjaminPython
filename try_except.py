# while True:
#     try:
#         edad=int(input("Ingrese su edad: ")) # Si aparece un error,
#         # Salata a la linea 7, donde esta except para manejar el error.
#         print("Su edad es", edad)
#         break
#     except ValueError as e:
#         print("Solo se aceptan numeros enteros")
#         print(e)


# for i in range(10):
#     n1=int(input("Ingrede un numero: "))
#     if n1%2!=0:
#         break


# num=0
# while True:
#     try:
#         n1=int(input("Ingrese un numero: "))
#         num+=n1
#         if n1==0:
#             break
#     except:
#         print("Solo numeros enteros")
# print(f"El total es {num}")


# Ejemplo de menu con try except

# op=0
# precio=0
# cantPRod=0
# while op!=4:
#     try:
#         print("1.- Radio Stereo Sony $70.000")
#         print("2.- LGTV 55 pulgadas Super Gamer $500.000")
#         print("3.- PS5 $580.000")
#         print("4.- Salir")
#         print("Seleccione una opcion:")
#         op=int(input())
#         match op:
#             case 1:
#                 print("El precio a pagar es", 70000*1.19)
#                 precio+=70000*1.19
#                 cantPRod+=1
#             case 2:
#                 print("El precio a pagar es", 500000*1.19)
#                 precio+=500000*1.19
#                 cantPRod+=1
#             case 3:
#                 print("El precio a pagar es", 580000*1.19)
#                 precio+= 580000*1.19
#                 cantPRod+=1
#             case 4:
#                 print("Saliendo del programa")
#                 print("El precio a pagar es", precio)
#                 print(f"La cantidad de productos es {cantPRod}")
#             case _:
#                 print("Opcion no valida")  # Opcion por defecto
#     except:
#         print("Solo numeros enteros")


porc=float(input("Ingrese el porcentaje de rucos en su comuna"))

if porc>0 and porc<100:
    print("Porcentaje correcto")
else:
    print("Porcentaje fura de rango")