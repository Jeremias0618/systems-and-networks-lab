# Empresa de luz

"""
Una empresa cobra el consumo de luz electrica de la siguiente manera:
. Si el consumo es menor a 100 kwh entonces cobra 0.80 soles por kwh
. Si el consumo es entre 100 y 200 kwh entonces cobra 1.00 soles por kwh
. Si el consumo es mayor a 200 kwh entonces cobra 1.20 soles por kwh
Solicitar el consumo y calcula el monto a pagar. Mostrar como salida:
. Consumo
. Tarifa aplicada
. Monto a pagar
"""
consumo = float(input("Ingrese el consumo en kwh: "))

if consumo < 100: # si el consumo es menor a 100 kwh
    tarifa = 0.80
elif consumo <= 200: # si el consumo es entre 100 y 200 kwh
    tarifa = 1.00
else: # si el consumo es mayor a 200 kwh
    tarifa = 1.20

monto = consumo * tarifa

print("Consumo: ", consumo)
print("Tarifa aplicada: ", tarifa)
print("Monto a pagar: ", monto)