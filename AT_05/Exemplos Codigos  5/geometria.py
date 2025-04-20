import math
from abc import ABC,abstractmethod

class FormasGeometricas(ABC): #Classe Abstrata (Herda de ABC e possui métodos abstratos)
    def __init__(self,cor="ind"):
        self.cor = cor

    #Métodos concretos
    def get_cor(self):
        return self.cor
    def set_cor(self,nova_cor):
        self.cor = nova_cor
    
    @abstractmethod #método abstrato
    def calcular_area(self):
        pass
    
    @abstractmethod #método abstrato
    def calcular_perimetro(self):
        pass


class Circulo(FormasGeometricas):
    def __init__(self, cor="ind",raio=0):
        super().__init__(cor)
        self.raio = raio

    def get_raio(self):
        return self.raio
    def set_raio(self, novo_raio):
        self.raio = novo_raio
    
    def calcular_area(self):
        area = 2*math.pi*self.raio*self.raio
        return area
    
    def calcular_perimetro(self):
        perimetro = 2*math.pi*self.raio
        return perimetro

class Quadrado(FormasGeometricas):
    def __init__(self, cor="ind",lado=0):
        super().__init__(cor)
        self.lado = lado

    def get_lado(self):
        return self.lado
    def set_lado(self, novo_lado):
        self.lado = novo_lado
    
    def calcular_area(self):
        area = self.lado*self.lado
        return area
    
    def calcular_perimetro(self):
        perimetro = self.lado*4
        return perimetro

circulo = Circulo("Preto",10)
quadrado = Quadrado("Rosa",20)
#forma_geometrica = FormasGeometricas("Vermelho") #Errado pois não se instancia classes abstratas
