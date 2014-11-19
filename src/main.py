# -*- coding: utf-8 -*-

from calculadora import calculadora

calc = calculadora()
opciones = {
    'insertar números': calc.insertar,
    'suma': calc.suma,
    'resta': calc.resta,
    'division': calc.division,
    'calc_media': calc.calc_media,
    'calc_desvio': calc.calc_desvio,
    'grafico': calc.grafico,
    'salir': 'chau'
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
    if seleccion != 'salir':
        resultado = operacion()
        if seleccion != 'insertar números' and seleccion != 'grafico':
            print 'El resultado de '+str(seleccion)+' es '+str(resultado)
        main()
    else:
        print 'CHAU!'

if __name__ == '__main__':
    main()
