class AreaCirculo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2


radio = int(input('Ingrese el radio: '))

# Vamos a calcular el área de un círculo
Area = AreaCirculo(radio)
print(f'El area es: {Area.area()}')
