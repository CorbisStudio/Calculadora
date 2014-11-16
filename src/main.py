# -*- coding: utf-8 -*-

from calculadora import calculadora

FUNCIONES = ['insertar', 'suma', 'calc_media', 'calc_desvio', 'grafico']

def main():
    print 'Elija que desea hacer'
    for funcion in FUNCIONES:
        print funcion
    opcion = raw_input('Ingrese el nombre de la opción:')
    while opcion not in FUNCIONES:
        opcion = raw_input('La opción debe ser una de las mostradas '
                    'intente nuevamente:')
    calc = calculadora()
    if opcion == 'suma':
        calc.suma()
    elif opcion == 'calc_media':
        calc.calc_media()
    elif opcion == 'calc_desvio':
        calc.calc_desvio()
    elif opcion == 'grafico':
        calc.grafico()

if __name__ == '__main__':
    main()