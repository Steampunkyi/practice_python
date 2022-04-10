class Ejer03:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calculo_total(self):
        return self.a * ((self.b + self.c) / self.d)

a = int(input('Ingrese el primer valor: '))
b = int(input('Ingrese el segundo valor: '))
c = int(input('Ingrese el tercer valor: '))
d = int(input('Ingrese el cuarto valor: '))

x = Ejer03(a, b, c, d)
print(f'El total es: {x.calculo_total()}')