# Gestor de pacientes

pacientes=[

  {"nombre":"Aquiles Baeza", "prevision":"Fonasa", "temperatura":34.6, "grave": False}
]

def mostar_pacientes():
    print("-"*40)
    for p in range(len(pacientes)):
        print(f"{p+1}.- {pacientes[p]}")
    print("-"*40)

while True:
    try:
        print("1.- Ingresar Pacientes")
        print("2.- Ver Pacientes")
        print("3.- Pagar un paciente")
        print("4.- Salir")
        op=int(input("Ingrse una opcion: "))
        match op:
            case 1:
                nombre=input("Ingrese el nombre del paciente: ")
                if len(nombre)<1:
                    print("Porfavor no ingresar nada")
                else:
                    prev=input("Ingrese la prevision del paciente: ")
                    temp=float(input("Ingrese la temperatura del paciente: "))
                    if temp>=39:
                        nuevo_paciente={"nombre":nombre, "prevision":prev, "temperatura":temp, "grave":True}
                        pacientes.append(nuevo_paciente)
                    else:
                        nuevo_paciente={"nombre":nombre, "prevision":prev, "temperatura":temp, "grave":False}
                        pacientes.append(nuevo_paciente)
            case 2:
                mostar_pacientes()
            case 3:
                mostar_pacientes()
                try:
                    pagar=int(input("Ingrese el paciente que va a pagar: "))
                    pacientes[pagar-1]["prevision"]
                    if pacientes("prevision")=="Fonasa":
                        print("El precio a pagar es", 25000*0.46)
                        pacientes.pop(pagar-1)
                    elif pacientes.values("prevision")=="Isapre":
                        print("El precio a pagar es", 25000*0.73)
                        pacientes.pop(pagar-1)
                    elif pacientes.values("prevision")=="Fodesa":
                        print("El precio a pagar es", 25000*0.875)
                        pacientes.pop(pagar-1)
                except:
                    print("Numero de paciente no valido")
            case 4:
                print("Saliendo del gestor, que tenga un buen dia")
                break
            case _:
                print("Opcion invalida, vuelva a intentarlo")
    except Exception as e:
        print("Error",e)