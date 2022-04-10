class Ejer02:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def calculo_total(self):
        return self.x * self.y + (self.a / self.b)

x = int(input('Ingrese el primer valor: '))
y = int(input('Ingrese el segundo valor: '))
a = int(input('Ingrese el tercer valor: '))
b = int(input('Ingrese el cuarto valor: '))

total = Ejer02(x, y, a, b)
print(f'El total es: {total.calculo_total()}')