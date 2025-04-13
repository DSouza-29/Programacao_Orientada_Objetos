from datetime import datetime

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

    def consultarSaldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso."
        return "Valor inválido para depósito."

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso."
        return "Saldo insuficiente ou valor inválido."

    def transferir(self, conta_destino, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            return f"Transferência de R${valor:.2f} para {conta_destino.usuario.nome} realizada com sucesso."
        return "Saldo insuficiente ou valor inválido para transferência."

    def __str__(self):
        return f"Agência: {self.agencia}\nUsuário: {self.usuario.nome}\nData de Abertura: {self.data_abertura.strftime('%d/%m/%Y %H:%M:%S')}\nSaldo: R${self.saldo:.2f}"


class ContaPoupanca(Conta):
    def __init__(self, agencia, usuario, data_abertura, saldo, taxa_juros):
        super().__init__(agencia, usuario, data_abertura, saldo)
        self.taxa_juros = taxa_juros

    def render_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        return f"Juros de R${juros:.2f} aplicados. Novo saldo: R${self.saldo:.2f}"


class ContaCorrente(Conta):
    def __init__(self, agencia, usuario, data_abertura, saldo, limite):
        super().__init__(agencia, usuario, data_abertura, saldo)
        self.limite = limite

    def usar_limite(self, valor):
        if valor <= self.limite:
            self.saldo -= valor
            return f"Uso de limite de R${valor:.2f} realizado com sucesso."
        return "Limite insuficiente."


class ContaEspecial(ContaCorrente):
    def __init__(self, agencia, usuario, data_abertura, saldo, limite, limite_especial):
        super().__init__(agencia, usuario, data_abertura, saldo, limite)
        self.limite_especial = limite_especial

    def consultarSaldo(self):
        total_disponivel = self.saldo + self.limite + self.limite_especial
        return f"Saldo: R${self.saldo:.2f}\nLimite total disponível: R${total_disponivel:.2f}"

    def sacar(self, valor):
        total_disponivel = self.saldo + self.limite + self.limite_especial
        if 0 < valor <= total_disponivel:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso."
        return "Saldo/Limite insuficiente."

    def transferir(self, conta_destino, valor):
        total_disponivel = self.saldo + self.limite + self.limite_especial
        if 0 < valor <= total_disponivel:
            self.saldo -= valor
            conta_destino.saldo += valor
            return f"Transferência de R${valor:.2f} realizada com sucesso para {conta_destino.usuario.nome}"
        return "Saldo/Limite insuficiente para transferência."

    def usar_limite_especial(self, valor):
        if valor <= self.limite_especial:
            self.saldo -= valor
            return f"Uso de limite especial de R${valor:.2f} realizado com sucesso."
        return "Limite especial insuficiente."
