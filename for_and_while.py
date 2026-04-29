# uso y repaso de for
# import random
# num=random.randint(1,8)
# print(num)
# for i in range(num):
#     print("Hola", i)

# for i in "alonsonic":
    # print(i)


# op=0
# per=0
# total=0
# while op!=4:
#     print('''1 .- Niño (1-17) 1000
# 2 .- Adulto (18-64) 3000
# 3 .- Adulto Mayor (65+) 1500
# 4 .- Salir''')
#     op=int(input("Seleccione una opcion: "))
#     match op:
#         case 1:
#             print("Pagando el precio de niño")
#             cantN=int(input("Ingrese la cantidad de niños: "))
#             while cantN<1 or cantN>10:
#                 print("Cantidad fuera de rango (1-10)")
#                 cantN=int(input("Ingrese la cantidad de niños: "))
#             per+=cantN
#             total+=1000*cantN
#         case 2:
#             print("Pagando el precio de adulto")
#             cantA=int(input("Ingrese la cantidad de adultos: "))
#             while cantA<1 or cantA>10:
#                 print("Cantidad fuera de rango (1-10)")
#                 cantA=int(input("Ingrese la cantidad de adultos: "))
#             per+=cantA
#             total+=3000*cantA
#         case 3:
#             print("Pagando el precio de viejito")
#             cantV=int(input("Ingrese la cantidad de viejitos: "))
#             while cantV<1 or cantV>10:
#                 print("Cantidad fuera de rango (1-10)")
#                 cantV=int(input("Ingrese la cantidad de viejitos: "))
#             per+=cantV
#             total+=1500*cantV
#         case 4:
#             print("Saliendo del programa")
#             print(f"La cantidad de personas es {per}")
#             print(f"El total a pagar es {total}")
#         case _:
#             print("Opcion invalida")

total=0
folio=int(input("Ingrese su folio: "))
while folio<7000 or folio>21000:
    print("Folio fuera de rango")
    folio=int(input("Ingrese su folio: "))

cancha=input("Perfecto, ¿esta en cancha vip, general o tribuna? ")
match cancha:
    case "vip":
        total+=40000*1.8
        print(f"Total a pagar es {total}")
    case "general":
        total+=40000*1.4
        print(f"Total a pagar es {total}")
    case "tribuna":
        total+=40000*1.2
        print(f"Total a pagar es {total}")
    case _:
        print("Cancha invalida")
print("Saliendo")