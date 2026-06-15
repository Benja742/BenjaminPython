parking={
    1:[],
    2:[],
    3:[],
    4:[]
}

while True:
    try:
        print("1.- Ingresar Vehiculo")
        print("2.- Contar Ganancias")
        print("3.- Contar Vehiculos")
        print("4.- Ganancias Promedio")
        print("5.- Ver pisos")
        print("6.- Salir")
        op=int(input("Ingrese una opicon: "))
        match op:
            case 1:
                auto=int(input("Ingrese el vehiculo: \n1.- Ligero\n2.- Mediano\n3.- Pesado "))
                piso=int(input("¿Cual piso quiere?: "))
                if len(parking[piso])<10:
                    if auto==1:
                        parking[piso].append(2000)
                    elif auto==2:
                        parking[piso].append(3000)
                    elif auto==3:
                        parking[piso].append(3500)
                    else:
                        print("Vehiculo no valido")
                else:
                    print("El piso esta lleno")
            case 2:
                totalGanancias=0
                for pesos in parking.values():
                    totalGanancias+=sum(pesos)
                print(f"El total acumulado actual es {totalGanancias}")
            case 3:
                totalAutos=0
                for pesos in parking.values():
                    totalAutos+=len(pesos)
                print(f"El total de autos es {totalAutos}")
            case 4:
                totalProm=0
                PisosUsados=0
                for pesos in parking.values():
                    if len(pesos)==0:
                        valor=0
                    else:
                        valor=sum(pesos) / len(pesos)
                        PisosUsados+=1
                        totalProm+=valor
                print("El promedio actual es", totalProm/PisosUsados)
            case 5:
                for piso, espacios in parking.items():
                    print(f"Piso {piso}:{espacios}")
            case 6:
                print("Saliendo")
                break
            case _:
                print("Numero fuera de rango")
    except Exception as e:
        print("Error",e)