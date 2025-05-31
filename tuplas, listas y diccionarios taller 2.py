#Taller 1: Registro simple de producto y cálculo de costos.

# Solicita los datos del producto
# nombre_producto = input("Ingrese el nombre del producto: ")
# precio_unitario = float(input("Ingrese el precio unitario: "))
# cantidad_comprada = int(input("Ingrese la cantidad comprada: "))

# Almacena la información en las estructuras indicadas
# producto = (nombre_producto, precio_unitario)
# registro = [producto, cantidad_comprada]
# factura = {"producto": registro}

# Calcula el costo total
#costo_total = precio_unitario * cantidad_comprada

# Muestra el resultado
# print("\nFactura")
# print("Producto:", producto[0])
# print("Precio unitario: $", producto[1])
# print("Cantidad:", cantidad_comprada)
# print("Costo total: $", costo_total)

#Taller 2:Factura de múltiples productos (versión fija sin bucles)

# Registro de tres productos
# nombre1 = input("Producto 1 - Nombre: ")
# precio1 = float(input("Producto 1 - Precio unitario: "))
# cant1 = int(input("Producto 1 - Cantidad: "))

# nombre2 = input("Producto 2 - Nombre: ")
# precio2 = float(input("Producto 2 - Precio unitario: "))
# cant2 = int(input("Producto 2 - Cantidad: "))

# nombre3 = input("Producto 3 - Nombre: ")
# precio3 = float(input("Producto 3 - Precio unitario: "))
# cant3 = int(input("Producto 3 - Cantidad: "))

# Crear tuplas y listas
# producto1 = [(nombre1, precio1), cant1]
# producto2 = [(nombre2, precio2), cant2]
# producto3 = [(nombre3, precio3), cant3]

# Diccionario con productos
# factura = {
#     "producto1": producto1,
#     "producto2": producto2,
#     "producto3": producto3
# }

# Cálculos individuales
# total1 = producto1[0][1] * producto1[1]
# total2 = producto2[0][1] * producto2[1]
# total3 = producto3[0][1] * producto3[1]
# total_general = total1 + total2 + total3

# Imprimir factura bien organizada sin usar bucles
# print("\n--- Factura ---")

# print("Producto 1:", producto1[0][0])
# print("Precio unitario:", producto1[0][1])
# print("Cantidad:", producto1[1])
# print("Subtotal:", total1)

# print("\nProducto 2:", producto2[0][0])
# print("Precio unitario:", producto2[0][1])
# print("Cantidad:", producto2[1])
# print("Subtotal:", total2)

# print("\nProducto 3:", producto3[0][0])
# print("Precio unitario:", producto3[0][1])
# print("Cantidad:", producto3[1])
# print("Subtotal:", total3)

# print("\nTotal general de la factura: $", total_general)

#Taller 3: Registro de notas de un estudiante

# Solicitar datos del estudiante
#nombre_estudiante = input("Ingrese el nombre del estudiante: ")

# Primera asignatura
# materia1 = input("Nombre de la primera asignatura: ")
# nota1_1 = float(input("Primera nota de esa asignatura: "))
# nota1_2 = float(input("Segunda nota de esa asignatura: "))
# prom1 = (nota1_1 + nota1_2) / 2
# asig1 = [(materia1, prom1), [nota1_1, nota1_2]]

# Segunda asignatura
# materia2 = input("Nombre de la segunda asignatura: ")
# nota2_1 = float(input("Primera nota de esa asignatura: "))
# nota2_2 = float(input("Segunda nota de esa asignatura: "))
# prom2 = (nota2_1 + nota2_2) / 2
# asig2 = [(materia2, prom2), [nota2_1, nota2_2]]

# Tercera asignatura
# materia3 = input("Nombre de la tercera asignatura: ")
# nota3_1 = float(input("Primera nota de esa asignatura: "))
# nota3_2 = float(input("Segunda nota de esa asignatura: "))
# prom3 = (nota3_1 + nota3_2) / 2
# asig3 = [(materia3, prom3), [nota3_1, nota3_2]]

# Crear el diccionario final
# registro = {
#     "nombre": nombre_estudiante,
#     "materias": [asig1, asig2, asig3]
# }

# Calcular promedio final
#promedio_final = (prom1 + prom2 + prom3) / 3

# Imprimir boletín bien formateado sin bucles
# print("\n--- Boletín de calificaciones ---")
# print("Estudiante:", registro["nombre"])

# Materia 1
# print("Asignatura:", asig1[0][0])
# print("Notas:", asig1[1])
# print("Promedio:", asig1[0][1])

# Materia 2
# print("Asignatura:", asig2[0][0])
# print("Notas:", asig2[1])
# print("Promedio:", asig2[0][1])

# Materia 3
# print("Asignatura:", asig3[0][0])
# print("Notas:", asig3[1])
# print("Promedio:", asig3[0][1])

# Promedio general
#print("\nPromedio final del estudiante:", round(promedio_final, 2))