# Clasificacion por edades

"""
Solicita la edad de una persona y cñasificala:
Niño: 0-12
Adolescente: 13-17
Adulto: 18-59
Adulto mayor: 60 o mas
"""

edad = int(input("Ingrese su edad: "))

if 0 <= edad <= 12:
    print("Clasificación: Niño")
elif 13 <= edad <= 17:
    print("Clasificación: Adolescente")
elif 18 <= edad <= 59:
    print("Clasificación: Adulto")
else:
    print("Clasificación: Adulto mayor")