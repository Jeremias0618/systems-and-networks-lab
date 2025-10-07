# Descuento en una tienda

"""
Si el cliente gasta mas de 100 soles, aplica un 10% de descuento.
Mostrar el precio final y el descuento aplicado.
"""
precio = float(input("Ingrese el precio total de su compra: "))

if precio > 100: #si el precio es mayor a 100

    descuento = precio * 0.1
    precio_final = precio - descuento
    print("El descuento aplicado es:", descuento)
    print("El precio final es:", precio_final)

else: # no se aplica descuento
    print("No se aplica descuento.")
    print("El precio final es:" , precio)