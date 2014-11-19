# -*- coding: utf-8 -*-

from calculadora import calculadora

calc = calculadora()
suma = calc.suma(1, 5)
print 'Suma: '+str(suma)

resta = calc.resta(5, 10)
print 'Resta: '+str(resta)

div = calc.division(3, 2)
print 'División: '+str(div)

media = calc.calc_media((1,2,3,5,84,65))
print 'Media: '+str(media)

desvio = calc.calc_desvio((1,2,3,5,84,65))
print 'Desvio: '+str(desvio)