class calculadora():
    numero_1 = None
    numero_2 = None
    resultado = None

    def suma(self):
    	self.resultado = self.numero_1 + self.numero_2

"""
Este if sirve para distinguir a cuando se llama el archivo desde otro archivo
o desde la terminal. En caso de ser desde la terminal entonces entra al if.
"""
if __name__ == '__main__':
	calculadora = calculadora()