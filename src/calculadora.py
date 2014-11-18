# -*- coding: utf-8 -*-

"""
Para la librería matplotlib hice 
    > git clone git://github.com/matplotlib/matplotlib.git
    > cd matplotlib
    > python setup.py install
"""
import matplotlib.pyplot as plt
from math import sqrt


class calculadora():
    numero_1 = None
    numero_2 = None
    resultado = None
    media = None
    desvio = None
    datos = []

    def insertar(self):
        self.numero_1 = None
        self.numero_2 = None
        while (self.numero_1 is None) or (self.numero_2 is None):
            try:
                self.numero_1 = float(raw_input('ingrese el primer número:'))
                self.numero_2 = float(raw_input('ingrese el segundo número:'))
            except ValueError:
                print 'Debe ingresar sólo números'

    def suma(self, numero_1='', numero_2=''):
        if (numero_1 is not '') and (numero_2 is not ''):
            try:
                self.numero_1 = float(numero_1)
                self.numero_2 = float(numero_2)
            except ValueError:
                print 'Debe ingresar sólo números'
                self.insertar()
        elif (self.numero_1 is None) or (self.numero_2 is None):
            self.insertar()

        self.resultado = self.numero_1 + self.numero_2
        return self.resultado

    def resta(self, numero_1='', numero_2=''):
        if (numero_1 is not '') and (numero_2 is not ''):
            try:
                self.numero_1 = float(numero_1)
                self.numero_2 = float(numero_2)
            except ValueError:
                print 'Debe ingresar sólo números'
                self.insertar()
        elif (self.numero_1 is None) or (self.numero_2 is None):
            self.insertar()

        self.resultado = self.numero_1 - self.numero_2
        return self.resultado

    """
    Estos son porque lo dijiste de joda y me lo tomé personal xD 
    (na joda, andaba aburrido y no me acordaba mucho la sintaxis de python)
    """
    def calc_media(self):
        cantidad = int(raw_input('¿Cuántos datos desea ingresar?'))
        if cantidad < 0:
            print 'Debe ingresar un número positivo'
            self.calc_media()

        media = 0
        for i in range(cantidad):
            valor = None
            while valor is None:
                try:
                    valor = float(raw_input('ingrese el dato Nº '+str(i+1)+':'))
                except ValueError:
                    print 'Debe ingresar sólo números'
            self.datos.append(valor)
            media = media + self.datos[i]
        self.media = media / cantidad
        return self.media

    """
    Para esto usemos la función media
    """
    def calc_desvio(self):
        self.calc_media()
        desvio = 0
        for x in self.datos:
            desvio = desvio + (x - self.media)**2
        self.desvio = sqrt(desvio / len(self.datos))
        return self.desvio

    """
    Hagámoslo divertido y usemos la media y desvio calculados antes para 
    generar un gráfico
    """
    def grafico(self):
        print 'Primero necesitamos saber los datos para la media y desvio estandar'
        self.calc_desvio()
        cantidad = int(raw_input('¿Cuántos datos quiere graficar?:'))
        x_cord = []
        y_cord = []
        for x in range(cantidad):
            valor = float(raw_input('ingrese el dato Nº '+str(x+1)+':'))
            x_cord.append(valor)
            y_cord.append((valor*self.desvio)+self.media)
        plt.plot(x_cord, y_cord, 'r')
        plt.show()

"""
Este if sirve para distinguir a cuando se llama el archivo desde otro archivo
o desde la terminal. En caso de ser desde la terminal entonces entra al if.
"""
if __name__ == '__main__':
    calculadora = calculadora()
    calculadora.suma()
    calculadora.grafico()
