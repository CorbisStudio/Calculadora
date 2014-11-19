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
    datos = []

    def insertar(self):
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

    def division(self, numero_1='', numero_2=''):
        if (numero_1 is not '') and (numero_2 is not ''):
            try:
                self.numero_1 = float(numero_1)
                self.numero_2 = float(numero_2)
            except ValueError:
                print 'Debe ingresar sólo números'
                self.insertar()
        elif (self.numero_1 is None) or (self.numero_2 is None):
            self.insertar()

        if self.numero_2 == 0:
            print 'No puede dividir por 0'
            self.insertar()

        self.resultado = self.numero_1 / self.numero_2
        return self.resultado

    """
    Estos son porque lo dijiste de joda y me lo tomé personal xD 
    (na joda, andaba aburrido y no me acordaba mucho la sintaxis de python)
    datos toma un arreglo de datos [1, 2, 3, ....]
    """

    def calc_media(self, datos = ''):
        media = 0
        datos_aux = []
        
        if datos == '':
            datos = raw_input('Ingrese los datos separados por coma:')
            datos = datos.split(',')

            for elem in datos:
                try:
                    media = media + float(elem)
                    datos_aux += [float(elem)]
                except ValueError:
                    print 'Debe ingresar sólo números'
                    self.calc_media()
        else:
            for elem in datos:
                try:
                    elem = float(elem)
                    datos_aux += [float(elem)]
                except ValueError:
                    print 'Debe ingresar un arreglo de números'
                    self.calc_media()

                media = media + elem

        """
        Debemos guardar los datos para usarlos en calc_desv.
        """
        self.datos = datos_aux
        
        cantidad = len(datos)
        if cantidad != 0:
            self.media = media / cantidad
        else:
            self.media = 0
        return self.media

    """
    Para esto usemos la función media
    """
    def calc_desvio(self, datos=''):
        if datos == '':
            media = self.calc_media()
        else:
            media = self.calc_media(datos)
        desvio = 0
        for x in self.datos:
            desvio = desvio + (x - media)**2
        desvio = sqrt(desvio / len(self.datos))

        return desvio

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
