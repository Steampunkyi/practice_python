class Ejer04:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculo_total(self):
        return (self.a + self.b) / 2

a = int(input('Ingrese el primer valor: '))
b = int(input('Ingrese el segundo valor: '))

num = Ejer04(a, b)
print(f'El total es: {num.calculo_total()}')