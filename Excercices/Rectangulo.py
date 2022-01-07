class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = int(input('Ingrese la base del rectangulo: '))
altura = int(input('Ingrese la altura del rectangulo: '))

rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')

base = int(input('Ingrese la base del rectangulo: '))
altura = int(input('Ingrese la altura del rectangulo: '))

rectangulo2 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo2.calcular_area()}')
