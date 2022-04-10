class Ejer01:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculo_total(self):
        return self.a * self.b + self.c * 5

a = int(input('Ingrese el primer valor: '))
b = int(input('Ingrese el segundo valor: '))
c = int(input('Ingrese el tercer valor: '))

total = Ejer01(a, b, c)
print(f'El total es: {total.calculo_total()}')