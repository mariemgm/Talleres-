# #taller 1
# print("registro de producto y cálculo de costos")

# # Solicitar información
# nombre = input("Nombre del producto: ")
# precio = float(input("Precio unitario: "))
# cantidad = int(input("Cantidad comprada: "))

# # Estructuras de datos
# producto = (nombre, precio)
# lista_producto = [producto, cantidad]
# factura = {"producto": lista_producto}

# # Cálculo
# costo_total = precio * cantidad

# # Mostrar resultado
# print("\nFactura:")
# print(f"Producto: {producto[0]}")
# print(f"Precio unitario: ${producto[1]:.2f}")
# print(f"Cantidad: {cantidad}")
# print(f"Costo total: ${costo_total:.2f}")

# print("---------------------------------------------------------------------------------------------------------------")

# #taller 2
# print("factura de multiples productos")

# # Ingreso de datos
# nombre1 = input("Nombre del producto 1: ")
# precio1 = float(input("Precio unitario: "))
# cant1 = int(input("Cantidad: "))

# nombre2 = input("Nombre del producto 2: ")
# precio2 = float(input("Precio unitario: "))
# cant2 = int(input("Cantidad: "))

# nombre3 = input("Nombre del producto 3: ")
# precio3 = float(input("Precio unitario: "))
# cant3 = int(input("Cantidad: "))

# # Estructuras
# prod1 = [(nombre1, precio1), cant1]
# prod2 = [(nombre2, precio2), cant2]
# prod3 = [(nombre3, precio3), cant3]

# factura = {
#     "producto1": prod1,
#     "producto2": prod2,
#     "producto3": prod3
# }

# # Cálculos
# total1 = precio1 * cant1
# total2 = precio2 * cant2
# total3 = precio3 * cant3
# total_general = total1 + total2 + total3

# # Imprimir factura
# print("\nFactura:")
# for clave in factura:
#     nombre, precio = factura[clave][0]
#     cantidad = factura[clave][1]
#     total = precio * cantidad
#     print(f"{nombre} - Precio: ${precio:.2f}, Cantidad: {cantidad}, Total: ${total:.2f}")
# print(f"Total general: ${total_general:.2f}")

# print("------------------------------------------------------------------------------------------------------------------")

# #taller 3
# print("registro de notas de un estudiante")

# # Ingreso de datos
# nombre_estudiante = input("Nombre del estudiante: ")

# materias = []
# for i in range(1, 4):
#     asignatura = input(f"\nNombre de la asignatura {i}: ")
#     nota1 = float(input("Nota 1: "))
#     nota2 = float(input("Nota 2: "))
#     promedio = (nota1 + nota2) / 2
#     tupla_materia = (asignatura, promedio)
#     lista_materia = [tupla_materia, nota1, nota2]
#     materias.append(lista_materia)

# # Diccionario con la información
# boletin = {
#     "nombre": nombre_estudiante,
#     "materias": materias
# }

# # Calcular promedio final
# promedios = [m[0][1] for m in materias]
# promedio_final = sum(promedios) / len(promedios)

# # Imprimir boletín
# print(f"\nBoletín de calificaciones de {boletin['nombre']}")
# for m in boletin["materias"]:
#     asignatura, promedio = m[0]
#     print(f"{asignatura}: Nota 1 = {m[1]}, Nota 2 = {m[2]}, Promedio = {promedio:.2f}")
# print(f"Promedio final: {promedio_final:.2f}")





