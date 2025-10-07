# Clasificacion por edades

"""
Solicita la edad de una persona y cñasificala:
Niño: 0-12
Adolescente: 13-17
Adulto: 18-59
Adulto mayor: 60 o mas
"""

edad = int(input("Ingrese su edad: "))

if  edad <= 0 and edad <= 12:
    print("Eres un niño")
elif edad <= 13 and edad <= 17:
    print("Eres un adolescente")
elif edad <= 18 and edad <= 59:
    print("Eres un adulto")
elif edad >= 60:
    print("Eres un adulto mayor")
else:
    print("Edad no valida")