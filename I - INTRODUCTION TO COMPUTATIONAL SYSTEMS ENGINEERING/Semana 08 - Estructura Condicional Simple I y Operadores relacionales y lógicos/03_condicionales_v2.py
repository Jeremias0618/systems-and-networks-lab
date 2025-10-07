# El uso de elif

"""
Solicita dos numeros enteros al usuario e indica cual de ellos es el mayor.
Si son iguales mostrar un mensaje indicandolo.
"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    print(f"{num1} es el mayor")

elif num2 > num1:
    print(f"{num2} es el mayor")
else:
    print("Ambos numeros son iguales.")