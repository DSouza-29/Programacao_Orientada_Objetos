from random import randint

class UsuarioBanco():
    def __init__(self, nome="Padrão", idade=18):
        self.nome = nome
        self.idade = idade

    def exibirInformacoes(self):
        mensagem = f"\nInformações\n"
        mensagem+= f"\nNome: {self.nome}\n"
        mensagem+= f"\nIdade: {self.idade}\n"
        return mensagem

class Cliente(UsuarioBanco):
    def __init__(self, nome, idade,):
        super().__init__(nome, idade)
        self.numero_conta = randint(10000,99999)

    def abrir_conta(self):
        mensagem = f"\nCliente\n"
        mensagem+= f"Nome: {self.nome}\n"
        mensagem+= f"Idade: {self.idade}\n"
        mensagem+= f"Numero da conta: {self.numero_conta}\n"   
        return mensagem


us = UsuarioBanco("denner", 18)

print(us.exibirInformacoes())