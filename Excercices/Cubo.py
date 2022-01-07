class Cubo:
    def __init__(self, largo, ancho, altura):
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

    def calcular_volumen(self):
        return self.largo * self.ancho * self.altura


largo = int(input('Ingrese el largo del cubo: '))
ancho = int(input('Ingrese el ancho del cubo: '))
altura = int(input('Ingrese la altura del cubo: '))

cubo1 = Cubo(largo, ancho, altura)
print(f'El volumen del cubo es: {cubo1.calcular_volumen()} m3')
