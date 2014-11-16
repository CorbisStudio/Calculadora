# -*- coding: utf-8 -*-

from calculadora import calculadora

calc = calculadora()
opciones = {
    'suma': calc.suma,
    'calc_media': calc.calc_media,
    'calc_desvio': calc.calc_desvio,
    'grafico': calc.grafico
}

def main():
    print 'Elija que desea hacer'
    for opcion in opciones:
        print opcion
    seleccion = raw_input('Ingrese el nombre de la opción:')
    while seleccion not in opciones:
        seleccion = raw_input('La opción debe ser una de las mostradas '
                    'intente nuevamente:')

    operacion = opciones[seleccion]
    operacion()

if __name__ == '__main__':
    main()