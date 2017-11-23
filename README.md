# tutorialString
String en Python

¿Qué es String?
String es la librería encargada de poder crear cadenas de caracteres, es de las más usadas tanto en Python como ocurre también en otros lenguajes de programación.

Para declarar un String necesitamos de una variable que será igualada a una cadena de caracteres entre comillas simples o dobles.

cadena1 = 'Hola mundo'

 

Principales funcionalidades
len() -->  Se encarga de contar los caracteres de la variable. 
#Primero creamos una variable con una cadena
cadena = 'Hola mundo'

#Este paso será el encargado de contar los caracteres
print(len(cadena))

>>8
 

 

replace() --> Hace posible que podamos cambiar una palabra de una cadena por otra que deseemos 
#Primero creamos una variable con una cadena
cadena = 'Hola mundo'

#Cambiaremos hola por adios
cadena.replace("Hola","Adios")
print(cadena)

>>Adios mundo
 

 

upper() --> Convierte el texto a mayúsculas  
#Primero creamos una variable con una cadena
cadena = 'Hola mundo'

#Cambiaremos hola por adios
cadena.upper()
print(cadena)

>>HOLA MUNDO
 

 

lower() --> Convierte el texto a minúsculas
#Primero creamos una variable con una cadena
cadena = 'Hola Mndo'

#Cambiaremos hola por adios
cadena.lower()
print(cadena)

>>hola mundo
 

 

Operador string --> Sustituye los % por el valor que nosotros le demos.
#Usamos %s para convertirlo a un string y %d para un entero
print "Mi nombre es %s y tengo %d años" % ('Fernando', 21)


>>Mi nombre es Fernando y tengo 21 años
 

Otras funcionalidades
strip() --> Quita los espacios de los lados
lstrip() --> Quita los espacios de la derecha
rstrip() --> Quita los espacios de la izquierda
split("|") --> Divide una cadena que este montada con "|"
join() --> Hace lo contrario de split.
find() --> Le pasaremos una letra y nos devolverá el índice de donde se encuentra. 
