# # ejemplo y explicacion de match
# op=0
# precio=0
# while op!=4:
#     print("1.- Radio Stereo Sony $70.000")
#     print("2.- LGTV 55 pulgadas Super Gamer $500.000")
#     print("3.- PS5 $580.000")
#     print("4.- Salir del programa")
#     op=int(input("Seleccione una opcion "))
#     match op:
#         case 1:
#             print("El precio a pagar es", 70000*1.19)
#             precio+=70000*1.19
#         case 2:
#             print("El precio a pagar es", 500000*1.19)
#             precio+=500000*1.19
#         case 3:
#             print("El precio a pagar es", 580000*1.19)
#             precio+= 580000*1.19
#         case 4:
#             print("Salaiendo del programa")
#             print("El precio a pagar es", precio)
#         case _:
#             print("Opcion no valida")  # Opcion por defecto


name="Carlos"
def saludo():
    print("Hola como van")

def chao():
    print("Ya nos vamos?", name)


def suma():
    num1=int(input("Porfavor ingrese un numero "))
    num2=int(input("Porfavor ingrese otro numero "))
    print("El resultado es", num1+num2)
def resta():
    num1=int(input("Porfavor ingrese un numero "))
    num2=int(input("Porfavor ingrese otro numero "))
    print("El resultado es", num1-num2)
def multi():
    num1=int(input("Porfavor ingrese un numero "))
    num2=int(input("Porfavor ingrese otro numero "))
    print("El resultado es", num1*num2)
def divi():
    num1=int(input("Porfavor ingrese un numero "))
    num2=int(input("Porfavor ingrese otro numero "))
    print("El resultado es", num1/num2)


def prom():
    n1=float(input("Ingrese un numero: "))
    n2=float(input("Ingrese otro numero: "))
    print("El promedio de notas es", (n1+n2)/2)

def pin():
    pin=3434
    pwd=int(input("Ingrese el PIN . "))
    if pin==pwd:
        print("PIN correcto, bienvenido")
    else:
        print("PIN invalido, vuelva a intentarlo")
        pwd=int(input())

def credito():
    ingreso=int(input("Ingrse su sueldo: "))
    print("1.- basico")
    print("2.- medio")
    print("3.- superior")
    edu=int(input("Ingrese su nivel educacional: "))
    nacionalidad=input("Ingrese nacionalidad (chilena/otra) ")
    credito=0
    if ingreso>500000 and ingreso<=1000000:
        credito=credito+300000
    elif ingreso>1000001 and ingreso<=1500000:
        credito=credito+650000
    elif ingreso>1500001:
        credito=credito+1000000

        if edu==1:
            print("No tienes beneficio por educacion")
        elif edu==2:
            credito=credito*1.3
        elif edu==3:
            credito=credito*1.5

    if nacionalidad=="chilena":
        credito=credito+300000
    else:
        print("No tiene bono de nacionalidad")
        
    print("Su puntaje de credito es:", credito)


# op=0
# while op!=5:
    # print("1.- Suma")
    # print("2.- Resta")
    # print("3.- Multiplicacion")
    # print("4.- Division")
    # print("5.- Salir")
    # op=int(input("ingrese una operaicon "))
    # match op:
    #     case 1:
    #         suma()
    #     case 2:
    #         resta()
    #     case 3:
    #         multi()
    #     case 4:
    #         divi()
    #     case 5:
    #         print("Saliendo del programa")
    #     case _:
    #         print("Opcion invalida, vuela a intentarlo")


op=0
while op!=4:
    print("1.- Promedio de 2 notas")
    print("2.- PIN")
    print("3.- Calculacion de credito")
    print("4.- Salir")
    op=int(input("ingrese una operacion "))
    match op:
        case 1:
            prom()
        case 2:
            pin()
        case 3:
            credito()
        case 4:
            print("Saliendo del programa")
        case _:
            print("Opcion invalida")