from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'rojo')
print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')

# MRO - Method Resolution Order
print(Cuadrado.mro())