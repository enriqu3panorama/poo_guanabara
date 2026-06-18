from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados=0):
        self.qtd_lados = qtd_lados
    
    @abstractmethod
    def perimetro(self):
        pass

    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado, qtd_lados=4):
        super().__init__(qtd_lados)
        self.lado = lado
    
    def perimetro(self):
        return self.lado*4
    
    def area(self):
        return self.lado**2

class Circulo(Poligono):
    def __init__(self, raio, qtd_lados=1):
        super().__init__(qtd_lados)
        self.raio = raio
    
    def perimetro(self):
        return f'{2*3.14*self.raio:.2f}'
    
    def area(self):
        return f'{3.14*(self.raio**2):.2f}'

        


    