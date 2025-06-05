# # Ejercicios con condicionales y operaciones matemáticas

# #ejercicio1
# print("positivo,negativo o cero")
# numero=float(input("ingrese un numero"))
# elif numero>0:
#     print("el numero es positivo")
# elif numero<0:
#     print("el numero es negativo")
# else:
#     print("el numero es cero")


# #ejercicio 2
# print("Calcula el mayor de dos números ingresados")

# a = int(input("Ingresa el primer número: ")) 
# b = int(input("Ingresa el segundo número: ")) 
# print("Mayor:", a if a > b else b)

# #ejercicio 3
# print("Determina si un número es par o impar")

# n = int(input("Ingresa un número: ")) 
# print("Par" if n % 2 == 0 else "Impar")

# #ejercicio 4
# print("Verifica si está entre 10 y 20")

# n = int(input("Ingresa un número: ")) 
# print("Está entre 10 y 20" if 10 <= n <= 20 else "No está entre 10 y 20")

# #ejercicio 5
# print("Mayor de tres números")

# a = int(input("Ingresa primer número: "))
# b = int(input("Ingresa segundo número: ")) 
# c = int(input("Ingresa tercer número: ")) 
# print("Mayor:", max(a, b, c))

# #ejercicio 6
# print("Precio con descuento si total > $100.")

# total = float(input("Ingresa el total: $"))
# if total > 100: 
#     total *= 0.9 
#      print("Precio final:", total)

# # ejercicio 7 
# print("Verifica si puede votar.")

# edad = int(input("Ingresa tu edad: ")) 
# print("Puede votar" if edad >= 18 else "No puede votar")

# #ejercicio 8.
# print("Descuento solo para VIP.")

# precio = float(input("Precio: $"))
# tipo = input("Tipo de cliente (VIP o normal): ") 
# if tipo.upper() == "VIP": 
#     precio *= 0.8 
#     print("Precio final:", precio)

# #ejercicio 9. 
# print("Múltiplo de 3 y 5.")

# n = int(input("Ingresa un número: "))
# print("Múltiplo de 3 y 5" if n % 3 == 0 and n % 5 == 0 else "No lo es")

# #ejercicio 10. 
# print("Divisible entre dos números dados.")

# n = int(input("Número: ")) 
# d1 = int(input("Divisor 1: ")) 
# d2 = int(input("Divisor 2: ")) 
# if d1 != 0 and d2 != 0: 
#     print("Divisible por ambos" 
#           if n % d1 == 0 and n % d2 == 0 
#           else "No divisible por ambos") 
#     else: print("Divisores no válidos")

# #Ejercicios con Listas

# #ejercicio 11.
# print("Lista con 5 números, comparar el tercero.")

# lista = [4, 8, 12, 5, 9] 
# if lista[2] > 10: 
#     print("Mayor a 10") 
# else: print("Menor o igual a 10")

# #ejercicio 12. 
# print("Verificar si el número 7 está en la lista.")

# lista = [3, 5, 7, 9] 
# print("Está en la lista" if 7 in lista else "No está en la lista")

# #ejercicio 13. 
# print("Suma de dos primeros elementos y comparación.")

# lista = [4, 6, 2, 8]
# suma = lista[0] + lista[1] 
# print("Suma alta" if suma > 10 else "Suma baja")

# #ejercicio 14.
# print("Verificar último nombre de una lista.")

# nombres = ["Ana", "Luis", "Pedro", "Marta"] 
# ultimo = nombres[-1] 
# if ultimo == "Marta": 
#     print("Nombre correcto") 
# else: 
#     print("Nombre diferente")

# #ejercicio 15. 
# print("Lista con colores, cambia segundo si es azul.")

# colores = ["rojo", "azul", "verde"] 
# if colores[1] == "azul": 
#     colores[1] = "amarillo" 
#     print("Lista actualizada:", colores)

# #Ejercicios con Tuplas

# #ejercicio 16. 
# print("Verifica orden de valores en una tupla.")

# tupla = (5, 8, 12, 20) print("Orden ascendente" if tupla[0] < tupla[-1] else "Orden descendente")

# #ejercicio 17.
# print("Edad mayor a 30 en la segunda posición.")

# edades = (25, 32, 28) 
# print("Edad mayor a 30" if edades[1] > 30 else "Edad menor o igual a 30")

# #ejercicio 18. 
# print("Cambiar valor en tupla convertida a lista.")

# tupla = (1, 2, 3)
# lista = list(tupla) 
# if lista[1] == 2: 
#     lista[1] = 10 
#     tupla = tuple(lista) 
#     print(tupla)

# #ejercicio 19.
# print("Verificar coordenada alta.")

# coordenadas = (4, 9)
# print("Coordenada alta" 
#       if coordenadas[1] > 5 else "Coordenada baja")

# #ejercicio 20.
# print("Comparar tuplas.")

# t1 = (3, 4) 
# t2 = (3, 5) 
# print("Tuplas iguales" if t1 == t2 else "Tuplas diferentes")

# #Ejercicios con Diccionarios

# #ejercicio 21.
# print("Verificar edad en diccionario.")

# persona = {"nombre": "Juan", "edad": 17} 
# if persona["edad"] >= 18: 
#     print("Adulto") 
# else: 
#     print("Menor de edad")

# #ejercicio 22.
# print("Cambiar edad si es mayor a 18.")

# persona = {"nombre": "Lucía", "edad": 20} 
# if persona["edad"] > 18: 
#     persona["edad"] = 21 
#     print(persona)

# #ejercicio 23. 
# print("Agregar ciudad si no existe.")

# persona = {"nombre": "Carlos"} 
# if "ciudad" not in persona: 
#     persona["ciudad"] = "Bogotá" 
#     print(persona)

# #ejercicio 24. 
# print("Verificar existencia de clave precio.")

# producto = {"producto": "pan", "precio": 1200}
# if "precio" in producto: 
#     print(producto["precio"])
# else: 
#     print("No hay precio")

# #ejercicio 25. 
# print("Mostrar precio de producto si existe.")

# productos = {"pan": 1200, "leche": 2000} 
# if "pan" in productos: 
#     print(productos["pan"]) 
# else: 
#     print("Producto no disponible")
