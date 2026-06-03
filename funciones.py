# sin argumento y sin retorno
def saludo():
    print("Hola que tal?")




# sin argumento y con retorno
def suma():
    num1=3
    num2=5
    return(num1 + num2)


def esMayor():
    edad=24
    if edad>=18:
        return True
    else:
        return False

resultado=suma()

# print(esMayor())





# con argumento y sin retorno
def saludaMe(name):
    print("Hola", name)

# saludaMe("Kirby")


def calculaIVA(neto):
    print(f"El precio con IVA es {neto*1.19}")

# calculaIVA(4000)




# con argumento y sin retorno
def sumaCA(n1,n2):
    return(n1 + n2)


def calculaIVAca(neto):
    return neto*1.19

# print("El resultado es:" , sumaCA(7, 10))
# print("El total con IVA es:" , calculaIVAca(30000))



# v=int(input("Ingrese el valor neto: "))

# print("El total con IVA es:" , calculaIVAca(v))




def calculaDescuento(valor, desc):
    return valor-(valor*desc/100)
datos=[29500, 22]
# print("El valor con descuento es", calculaDescuento(*datos))
# print("El valor con descuento es", calculaDescuento(29500, 22))




# # num=input("Ingrese una lista de números enteros separados por espacios: ")
# # numeros=num.split()

# # for a in range(len(numeros)):
# #      numeros[a]=int(numeros[a])

# # numeros_impares=[]
# # numeros_pares=[]

# # for i in numeros:
# #     if i%2==0:
# #         numeros_pares.append(i)
# #     else:
# #         numeros_impares.append(i)

# # print("numeros pares:",numeros_pares)
# # print("numeros impares:",numeros_impares)





# Cree una funcion para pedir notas
# y ponerlas en el argumento
# para sacar el promedio

cNotas=int(input("Ingrse la cantidad de notas: "))
notas=[]
for n in range(cNotas):
    nota=int(input(f"Ingrese la nota {n+1}: "))
    notas.append(nota)

def calcPromedio(notas):
    return sum(notas)/len(notas)

print("El promedio de notas es:",calcPromedio(notas))