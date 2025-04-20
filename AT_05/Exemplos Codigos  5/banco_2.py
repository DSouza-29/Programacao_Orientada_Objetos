"""Nosso banco precisa tributar dinheiro de alguns bens que nossos clientes possuem. Para isso, vamos criar um sistema:

Crie uma interface Tributavel() que possui o método calcula_tributos().

Alguns bens são tributáveis e outros não, ContaPoupanca() não é tributável, já para ContaCorrente() você precisa pagar 1% da conta e o SeguroDeVida() tem uma taxa fixa de 42 reais.

As classes ContaCorrente() e ContaPoupanca() herdam de uma classe Conta().
Essa classe Conta() possui um saldo e os métodos sacar(), depositar() e obterSaldo() que retorna o saldo da conta.

Ao final, instancie objetos para testar o funcionamento do sistema completo.
"""

from abc import ABC,abstractmethod
from random import randint

#Interface
class Tributavel(ABC):

    @abstractmethod
    def calcular_tributos(self):
        pass

class Conta:
    def __init__(self):
        self.saldo = 0
        self.agencia = randint(1000,9999)

    def sacar(self,valor_saque):
        self.saldo -= valor_saque
        print(f"Foi realizado um saque de R${valor_saque}.\n")
        print(f"Novo saldo: R${self.saldo}\n")

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        print(f"Foi realizado um depósito de R${valor_deposito}.\n")
        print(f"Novo saldo: R${self.saldo}\n")

    def obter_saldo(self):
        print(f"Saldo: R${self.saldo}\n")

    def __str__(self):
        obj_str = "\nDados da conta\n"
        obj_str += f"Agência: {self.agencia}\n"
        obj_str += f"Saldo: R${self.saldo}"
        return obj_str
    
class ContaCorrente(Conta,Tributavel):

    def __init__(self):
        super().__init__()
        self.tributo = 0

    def calcular_tributos(self):
        self.tributo = self.saldo*0.01
        return self.tributo
    
    def __str__(self):
        obj_str = super().__str__()
        obj_str += f"\nTributo: {self.calcular_tributos()}"
        return obj_str
    
class ContaPoupanca(Conta):
    pass

class SeguroDeVida(Tributavel):
    def __init__(self):
        self.tributo = 0

    def calcular_tributos(self):
        self.tributo = 42
        return self.tributo

    def __str__(self):
        obj_str = "\nSeguro de Vida\n"
        obj_str += f"Tributo: R${self.calcular_tributos()}\n"
        return obj_str

conta_corrente = ContaCorrente()
conta_poupanca = ContaPoupanca()
seguro_de_vida = SeguroDeVida()

print(conta_corrente)
print(conta_poupanca)
print(seguro_de_vida)
