# # uso u explicacion de diccionarios

# alumno={
#     "nombre":"Shinji Ikari",
#     "edad":14,
#     "carrera":"piloto"
# }

# print(alumno)
# print(alumno["carrera"])

# for key, value in alumno.items():
#     print(f"{key}={value}")

# print("--- Cambios de datos ---")

# # for dato, valor in alumno.items():
# #     print(dato, valor)

# alumno["email"]="Shinji@nerv.com"
# alumno["carrera"]="escritor"
# del alumno["edad"]
# for key, value in alumno.items():
#     print(f"{key}={value}")

productos={
    1:{"nombre": "Control inalambrico",
       "categoria": "Electronica",
       "precio": 45000},
    2:{"nombre": "Pilas recargables",
       "categoria": "Insumos",
       "precio": 5000},
    3:{"nombre": "Pasta termica",
       "categoria": "Computacion",
       "precio": 7000}
}

print(productos[1]["nombre"])