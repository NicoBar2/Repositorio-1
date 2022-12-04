class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        resultado = self.ancho * self.alto

        return resultado
    
    def perimetro(self):
        resultado = 2 * (self.ancho + self.alto)

        return resultado


r = Rectangulo(10, 7)
print('Área del rectángulo: %.2f' % r.area())
print('Perímetro del rectángulo: %.2f' % r.perimetro())
A.distancia(D)
B.distancia(D)
C.distancia(D)
 
R = Rectangulo(A, B)
R.base()
R.altura()
R.area()