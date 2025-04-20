from abc import ABC,abstractmethod

#Interface: criar um contrato de implementação de código.
#Toda classe que implementar Animal, precisa implementar todos os métodos
class Animal(ABC):
    @abstractmethod
    def fazer_barulho(self):
        pass

    @abstractmethod
    def nascer(self):
        pass

    @abstractmethod
    def morrer(self):
        pass

class Cachorro(Animal):

    def nascer(self):
        return "Cachorro nasceu."
    
    def fazer_barulho(self):
        return "Cachorro fez Au Au au"
    
    def morrer(self):
        return "Cachorro morreu."

    def __str__(self) -> str:
        return "Sou um cachorro."

class Gato(Animal):

    def nascer(self):
        return "Gato nasceu."

    def fazer_barulho(self):
        return "Gato fez miau miau"

    def morrer(self):
        return "Gato morreu."

    def __str__(self) -> str:
        return "Sou um Gato."

cachorro = Cachorro()
gato = Gato()

print(cachorro.nascer())
print(cachorro.fazer_barulho())
print(cachorro.morrer())

print(gato.nascer())
print(gato.fazer_barulho())
print(gato.morrer())

