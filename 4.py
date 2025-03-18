primer_nombre =input("ingrese su primeros nombres : " )
segundo_nombre = input("ingrese su segundo nombre: ")
nombre = primer_nombre+" "+segundo_nombre
mayusculas= nombre.upper()
minusculas= nombre.lower()
primeras = nombre.title()
titulo = nombre.capitalize()
nombres= {mayusculas,minusculas,primeras,titulo}
print(nombres)
