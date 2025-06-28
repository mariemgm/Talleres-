#ejercicio 1
# total= 0
# num1=int(input("ingrese un numero (0 para terminar)"))
# while num1 !=0:
#     total += num1
#     num2=int(input("ingrese un numero (0 para terminar)"))
#     print("programa finalizado{total}")

#ejercicio 2
# clave=input("ingrese la contraseña")
# while clave !="python123":
#     print("contraseña incorrecta")
#     clave=input("intenta de nuevo")
#     print("acceso consedido")

#ejercicio 3
# productos=[]
# producto = input("ingrese un producto(fin para salir) ")
# while producto != "fin":
#         productos.append(producto)
#         producto = input("ingrese un producto(fin para salir) ")
# print(productos)
# print("has salido del programa")

# ejercicio 4
# contador=0
# pares=0
# impares=0
# while contador <10:
#     numero=int(input("ingresa un numero:"))
#     if numero %2==0:
#      pares+=1
#     else:
#      impares+=1
#     print("cantidad de numeros pares:", pares)
#     print("cantidad de numeros impares:", impares)

# ejercicio 5
# notas=[]
# while True:
#     nota=float(input("ingrese una nota del 0 al 5 (escriba un numero mayor a 5 para salir del programa)"))
#     if nota > 5:
#         break
#     notas.append(nota)
    
# if notas:
#     promedio=sum(notas)/len(notas)
#     print("notas ingresadas:", notas)
#     print("promedio", promedio)

# ejercicio 6
# numero=int(input("ingresa la tabla de multiplicar:"))
# contador=1
# while contador<=10:
#     resultado=numero*contador
#     print(f"{numero}*{contador}={resultado}")
#     contador+=1
    
#ejercicio 7
# numero_secreto = 17

# print("¡Adivina el número secreto entre 1 y 100!")

# while True:
#     intento = input("Ingresa tu número: ")

#     es_numero = True
#     for caracter in intento:
#         if caracter not in "0123456789":
#             es_numero = False
#             break

#     if not es_numero or intento == "":
#         print("Entrada no válida. Ingresa solo números.")
#         continue

#     intento = int(intento)

#     if intento < numero_secreto:
#         print("El número secreto es mayor.")
#     elif intento > numero_secreto:
#         print("El número secreto es menor.")
#     else:
#         print("¡Felicidades! Adivinaste el número secreto.")
#         break

# ejercicio 8
# Tupla con frutas
# frutas = ("manzana", "pera", "banana", "naranja", "uva")

# print("Adivina una fruta que esté en la tupla.")

# while True:
#     intento = input("Escribe el nombre de una fruta: ").lower()

#     if intento in frutas:
#         print("¡Correcto! Esa fruta está en la tupla.")
#         break
#     else:
#         print("Esa fruta no está. Intenta otra vez.")

# ejercicio 9
# diccionario = {
#     "gato": "cat",
#     "perro": "dog",
#     "casa": "house",
#     "mesa": "table",
#     "sol": "sun"
# }

# continuar = True

# while continuar:
#     palabra = input("Escribe una palabra en español (o escribe 'salir' para terminar): ")

#     if palabra == "salir":
#         continuar = False
#     else:
#         # Comparar directamente con cada clave sin usar 'in', 'list', ni 'for'
#         if palabra == "gato":
#             print("Traducción: cat")
#         elif palabra == "perro":
#             print("Traducción: dog")
#         elif palabra == "casa":
#             print("Traducción: house")
#         elif palabra == "mesa":
#             print("Traducción: table")
#         elif palabra == "sol":
#             print("Traducción: sun")
#         else:
#             print("Esa palabra no está en el diccionario.")

#ejercicio 10
# opcion = ""

# while opcion != "5":
#     print("\nCalculadora básica")
#     print("1. Sumar")
#     print("2. Restar")
#     print("3. Multiplicar")
#     print("4. Dividir")
#     print("5. Salir")

#     opcion = input("Elige una opción (1-5): ")

#     if opcion == "1":
#         a = float(input("Ingresa el primer número: "))
#         b = float(input("Ingresa el segundo número: "))
#         print("Resultado:", a + b)

#     elif opcion == "2":
#         a = float(input("Ingresa el primer número: "))
#         b = float(input("Ingresa el segundo número: "))
#         print("Resultado:", a - b)

#     elif opcion == "3":
#         a = float(input("Ingresa el primer número: "))
#         b = float(input("Ingresa el segundo número: "))
#         print("Resultado:", a * b)

#     elif opcion == "4":
#         a = float(input("Ingresa el primer número: "))
#         b = float(input("Ingresa el segundo número: "))
#         if b == 0:
#             print("No se puede dividir entre cero.")
#         else:
#             print("Resultado:", a / b)

#     elif opcion == "5":
#         print("Saliendo del programa...")

#     else:
#         print("Opción no válida.")

#ejercicio 11
# registro = {}
# continuar = True

# while continuar:
#     nombre = input("Ingresa un nombre (o escribe 'salir' para terminar): ")
    
#     if nombre == "salir":
#         continuar = False
#     else:
#         edad = input("Ingresa la edad de " + nombre + ": ")
#         registro[nombre] = edad

# # Mostrar el diccionario completo
# print("\nDiccionario completo de nombres y edades:")
# print(registro)

#ejercicio 12
# colores = ["azul", "rojo", "morado", "naranja", "verde"]
# print("Adivina un color que esté en la lista.")
# while True:
#      intento = input("Escribe el nombre de un color: ").lower()

#      if intento in colores:
#          print("¡Correcto! Ese color está en la lista.")
#          break
#      else:
#          print("Ese color no está. Intenta otra vez.")

#ejercicio 13
# numero=int(input("ingresa un numero:"))
# contador=1
# while contador <=5:
#     potencia=numero**contador
#     print(f"{numero}**{contador}={potencia}")
#     contador=contador+1

# ejercicio 14
# c1=0
# c2=0
# c3=0
# c4=0
# c5=0
# contador=1
# while contador<=5:
#     numero=int(input("ingresa un numero:"))
#     if contador==1:
#         c1=numero*numero
#     elif contador==2:
#         c2=numero*numero
#     elif contador==3:
#         c3=numero*numero
#     elif contador==4:
#         c4=numero*numero
#     elif contador==5:
#         c5=numero*numero
#     contador=contador+1
#     print("cuadrados ingresados")
#     print(c1,c2,c3,c4,c5)

#ejercicio 15
# estudiantes = {}
# continuar = True

# while continuar:
#     nombre = input("Ingresa el nombre del estudiante (o 'fin' para salir): ")

#     if nombre == "fin":
#         continuar = False
#     else:
#         nota = input("Ingresa la nota final de " + nombre + ": ")
#         estudiantes[nombre] = nota

# print("\nDiccionario de estudiantes con sus notas:")
# print(estudiantes)
    
        
