## Uso y explicacion random

import random
import time


# num=random.randint(1,10)
# print(num)


# num=random.randint(1,10)

# for i in range(num):
#     print("Hola Checha")


# strike=random.randint(10,70)

# if strike>50:
#     print("Its a critical hit!. Damage", strike)
# else:
#     print("Its not very efective. Damage",strike)


# jug1=random.randint(60,190)
# jug2=random.randint(60,190)
# jug3=random.randint(60,190)

# print(f"El jugador 1 golpeo la pelota {jug1} metros")
# print(f"El jugador 2 golpeo la pelota {jug2} metros")
# print(f"El jugador 3 golpeo la pelota {jug3} metros")
# time.sleep(2)
# if jug1>jug2 and jug1>jug3:
#     print("El jugador 1 hizo el tiro mas lejano")
# elif jug2>jug3:
#     print("El jugador 2 hizo el tiro mas lejano")
# else:
#     print("El jugador 3 hizo el tiro mas lejano")


p1=input("Ingrese el primer peleador ")
p2=input("Ingrese el segundo peleador ")
pv1=100
pv2=100
turno=random.randint(1,2)

while pv1>0 and pv2>0:
    if turno%2==0:
        print(f"Turno de {p1}")
        atk=random.randint(7,18)
        print(f"El {p1} ataca con {atk}")
        pv2-=atk
        print(f"El hp de {p2} es {pv2}")
        time.sleep(1)
    else:
        print(f"Turno de {p2}")
        atk=random.randint(7,18)
        print(f"El {p2} ataca con {atk}")
        pv1-=atk
        print(f"El hp de {p1} es {pv1}")
        time.sleep(1)
    turno+=1
    print(p1, "█"*pv1)
    print(p2, "█"*pv2)
if pv1>pv2:
    print("El ganador es", p1)
else:
    print("El ganador es", p2)