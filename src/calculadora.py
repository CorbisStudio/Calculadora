# -*- coding: utf-8 -*-

class calculadora():
    numero_1 = None
    numero_2 = None
    resultado = None

    def suma(self):
        self.resultado = self.numero_1 + self.numero_2

    """
    Este método devuelve una tupla con dos números ingresados por consola.
    """
    def insertar_valores(self):
        self.numero_1 = None
        self.numero_2 = None
        while self.numero_1 is None or self.numero_2 is None:
            try:
                self.numero_1 = float(raw_input('ingrese el primer número:'))
                self.numero_2 = float(raw_input('ingrese el segundo número:'))
            except ValueError:
                print 'Debe ingresar sólo números. Use punto para los decimales.'

    """
    Este método recibe dos parametros y devuelve el producto de ambos.
    Precondición: a y b deben ser numeros.
    """
    def multiplicacion(self):
        resultado = self.numero_1 * self.numero_2
        return resultado

"""
Este if sirve para distinguir a cuando se llama el archivo desde otro archivo
o desde la terminal. En caso de ser desde la terminal entonces entra al if.
"""
if __name__ == '__main__':
    calculadora = calculadora()
