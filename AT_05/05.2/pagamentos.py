from abc import ABC, abstractmethod


class MetodoPagamento(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def pagar(self):
        pass


class CartaoCredito(MetodoPagamento):
    def pagar(self):
        valor_final = self.valor * 1.05
        print("Pagamento com Cartão de Crédito")
        print(f"Valor original: R${self.valor:.2f}")
        print(f"Valor final com taxa de 5%: R${valor_final:.2f}")


class BoletoBancario(MetodoPagamento):
    def pagar(self):
        valor_final = self.valor * 0.98
        print("Pagamento via Boleto ")
        print(f"Valor original: R${self.valor:.2f}")
        print(f"Valor final com 2% de desconto: R${valor_final:.2f}")


class Pix(MetodoPagamento):
    def pagar(self):
        print("Pagamento com PIX")
        print(f"Valor final: R${self.valor:.2f}")
