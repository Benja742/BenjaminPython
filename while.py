# explicacion y ejemplos de while
cont=1
mult=1
num=10
while cont<=10:
    print("La tabla del", num, "es:", num, "*", mult, "=", num*mult)
    mult+=1
    cont+=1


# Codigo secreto
code=3434

pwd=int(input("Ingrese el pin "))

while code!=pwd:
    print("Error, intentelo otravez")
    pwd=int(input("Ingrese el pin "))
print("Accesos concedido")