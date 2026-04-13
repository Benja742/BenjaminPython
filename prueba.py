# print("Hola mundo") 

# creando variables

# titulo="Clima de hoy"  # String
# diaDelMes=13  # Int
# mes=4  # Int

# temperatura=22.3  # float

# llueve=False # boolean

# print(titulo)
# print("Temperatura actual:", temperatura, "grados")
# print(diaDelMes, "-", mes)

# if llueve:
#     print("Tiene que llevar paraguas")
# else:
#     print("Puede llevar polera sin mangas")


# pedir password y pin
# pida al usuario password en palabra que debe ser "temu"
# ademas pida el pin que debe se 3435
# los dos deben estar correctos para acceder al sistema

# password="temu"
# pin=3435

# palabra=input("Ingrese la palabra secreta ")
# code=int(input("Ingrese el pin de 4 digitos "))
# if code==pin and password==palabra:
#     print("acceso concedido")
# else:
#     print("acceso denegado")

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