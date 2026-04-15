# Ejemplo y explicacion de for
# for i in range(5):
#     print(i+1)


# num=int(input("Ingrese un numero: "))
# for i in range(num):
#     print(i+1, "Hola ben")


# num=int(input("Ingrese un numero: "))

# for i in range(10):
#     print(num, "*", i+1, "=", num*(i+1))


# for i in range(1,11):
#     print(num, "*", i, "=", num*i)


# num=int(input("Ingrese un numero: "))
# suma=0
# for i in range(num):
#     suma=suma+i+1

# print("El resultado de la suma es", suma)


# notas=int(input("Ingrese la cantidad de notas: "))
# suma=0
# for i in range(notas):
#     n=float(input("Porfavor ingrese la nota: "))
#     suma=suma+n
# prom=suma/notas


# print("El promedio final es:", prom)
# if prom>=4:
#     print("Usted aprobo la clase")
# else:
#     print("Usted repitio la clase")


# nombre=input("Ingrse su nombre ")
# voca=0
# conso=0
# for i in nombre:
#     print(i)
#     if i in"aeiouAEIOU": 
#         voca+=1
#     else:
#         conso+=1
# print("La cantidad de vocales es", voca)
# print("La cantidad de consonantes es", conso)

aprob=0
reprob=0
alum=int(input("Ingrese la cantidad de alumnos: "))
for i in range(alum):
    notas=int(input(f"Ingrese la cantidad de notas del alumno {i+1}: "))
    suma=0
    for a in range(notas):
        n=float(input(f"Ingrese la nota {a+1}: "))
        suma=suma+n
    prom=suma/notas
    print("El promedio final es", prom)

    if prom>4:
        print("El almuno aprobo")
        aprob+=1
        
    else:
        print("El almuno reprobo")
        reprob+=1
print("El numero de estudiantes aprobados es", aprob)
print("El numero de estudiantes reprobados es", reprob)

