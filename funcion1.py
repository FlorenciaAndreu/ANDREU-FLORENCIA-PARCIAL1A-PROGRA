#Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y 
#devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

precio_producto = float(input("Ingrese el precio de un producto: "))
porcentaje = 5
aumento = 0

def aplicar_aumento(precio_producto):
    aumento = (precio_producto * porcentaje) / 100
    total_con_aumento = precio_producto + aumento
    print("El total con aumento es ${}".format(total_con_aumento))

aplicar_aumento(precio_producto)