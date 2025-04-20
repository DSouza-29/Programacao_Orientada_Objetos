from abc import ABC, abstractmethod

# Classe abstrata CartaoWeb
class CartaoWeb(ABC):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    @abstractmethod
    def showMessage(self):
        pass

# Cartão para o Dia dos Namorados
class DiaDosNamorados(CartaoWeb):
    def showMessage(self):
        print(f"Feliz Dia dos Namorados, {self.destinatario}\n"
              "Que o amor esteja presente todos os dias em nossas vidas!")

# Cartão de Natal
class Natal(CartaoWeb):
    def showMessage(self):
        print(f"Feliz Natal, {self.destinatario}\n"
              "Desejo muita paz, saúde e momentos especiais com sua família.")

# Cartão de Aniversário
class Aniversario(CartaoWeb):
    def showMessage(self):
        print(f"Feliz Aniversário, {self.destinatario}\n"
              "Que seu novo ciclo seja repleto de conquistas e alegrias.")
