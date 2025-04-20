"""Nosso banco precisa tributar dinheiro de alguns bens que nossos clientes possuem. Para isso, vamos criar um sistema:

Crie uma interface Tributavel() que possui o método calcula_tributos().

Alguns bens são tributáveis e outros não, ContaPoupanca() não é tributável, já para ContaCorrente() você precisa pagar 1% da conta e o SeguroDeVida() tem uma taxa fixa de 42 reais.

As classes ContaCorrente() e ContaPoupanca() herdam de uma classe Conta().
Essa classe Conta() possui um saldo e os métodos sacar(), depositar() e obterSaldo() que retorna o saldo da conta.

Ao final, instancie objetos para testar o funcionamento do sistema completo.
"""

from abc import ABC,abstractmethod
from random import randint

class Tributavel(ABC):

    @abstractmethod
    def calcular_tributo(self):
        pass

class Conta:
    def __init__(self):
        self.saldo = 0
        self.agencia = randint(1000,9999)

    def sacar(self,valor_saque):
        self.saldo -= valor_saque
        print(f"O valor de R${valor_saque} foi sacado da conta em questão.")

    def depositar(self,valor_deposito):
        self.saldo += valor_deposito
        print(f"O valor de R${valor_deposito} foi depositado na conta em questão.")

    def obter_saldo(self):
        print(f"O saldo da conta é: R${self.saldo}")

    def __str__(self):
        obj_str = "\nDados da Conta\n"
        obj_str += f"Agência: {self.agencia}\n"
        obj_str += f"Saldo: RS{self.saldo}"
        return obj_str

class ContaCorrente(Conta,Tributavel):
    def calcular_tributo(self):
        valor_tributo = self.saldo*0.01
        #print(f"O valor do tributo é R${valor_tributo}")
        return valor_tributo

    def __str__(self):
        obj_str = super().__str__()
        obj_str += f"\nTributo: R${self.calcular_tributo()}"
        obj_str += "\nTipo de Conta: Conta Corrente"
        return obj_str

class ContaPoupanca(Conta):
    def __str__(self):
        obj_str = super().__str__()
        obj_str += "\nTipo de Conta: Conta Poupança\n"
        return obj_str

class SeguroDeVida(Tributavel):
    def calcular_tributo(self):
        valor_tributo = 42
        #print(f"O valor do tributo é R${valor_tributo}")
        return valor_tributo

    def __str__(self):
        obj_str = "Dados\n"
        obj_str += "Tipo: Seguro de Vida\n"
        obj_str += f"Tributos: R${self.calcular_tributo()}"
        return obj_str

conta_corrente = ContaCorrente()
conta_poupanca = ContaPoupanca()
seguro_de_vida = SeguroDeVida()

print(conta_corrente)
print(conta_poupanca)
print(seguro_de_vida)
