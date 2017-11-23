# -*- coding:utf-8 -*-
salida = True
cadena = str(raw_input('Introduzca un texto:'))

while (salida == True):
    def salir():
        print 'Adios'
        salida = False

    def contarCaracteres():
        print len(cadena)

    def remplazar():
        palabraCadena = str(raw_input('Introduzca la palabra que desea remplazar'))
        palabraDeseada = str(raw_input('Introduzca la palabra que desee'))
        cadena.replace(palabraCadena, palabraDeseada)
        print cadena

    def mayuscula():
        print cadena.upper()

    def minuscula():
        print cadena.lower()

    def operator():
        print 'Mi nombre es %s y tengo %d años' % ('Fernando', 21)
    opcion = {
            0: salir,
            1: contarCaracteres,
            2: remplazar,
            3: mayuscula,
            4: minuscula,
            5: operator
        }

    print '0. Salir'
    print '1. Contar caracteres del texto introducido'
    print '2. Remplazar una palabra'
    print '3. Convertir a mayusculas'
    print '4. Convertir a minusculas'
    print '5. Operadores'

    num = int(raw_input('Eliga una opcion: '))
    opcion.get(num)()