from datetime import datetime
from usuario import Usuario

class Conta:
    def __init__(self, agencia, usuario, data_abertura, saldo):
        self.agencia = agencia
        self.usuario = usuario
        self.data_abertura = data_abertura
        self.saldo = saldo

    def get_agencia(self):
        return self.agencia

    def get_usuario(self):
        return self.usuario

    def get_data_abertura(self):
        return self.data_abertura

    def get_saldo(self):
        return self.saldo

    def __str__(self):
        return f"Agencia: {self.agencia}\nUsuario: {self.usuario.nome}\nData de Abertura: {self.data_abertura.strftime('%d/%m/%Y %H:%M:%S')}\nSaldo: R${self.saldo:.2f}\n"
    
