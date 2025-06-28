#identificación de tipo de caracter: verifica si un carácter es letra, númer, símbolo o espacio.
caracter= input("ingresa un caracter")
if '0'<= caracter <= '100':
    print("este caracter corresponde a un número")
elif ('a'<= caracter <= 'z') or ('A'<= caracter <= 'Z'):
    print("Este caracter corresponde a una letra")
elif caracter==' ':
    print ("este caracter corresponde a un espacio")
else:
    print("el caracter corresponde a un símbolo")

