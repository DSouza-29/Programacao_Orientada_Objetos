"""O proprietario deve conter nome, CPF, data de nascimento"""

from datetime import datetime

class Proprietario():
    def __init__(self, nome="Nome Padão", cpf=0, data_nascimento=datetime(1900, 1, 1)):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def set_cpf(self, cpf):
        self.cpf = cpf
    
    def get_cpf(self):
        return self.cpf
    
    def set_data_nascimento(self, dia, mes, ano):
        self.data_nascimento = datetime(dia,mes,ano)
    
    def get_data_nascimento(self):
        return self.data_nascimento
    
    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"CPF: {self.cpf}\n"
                f"Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%y')}\n")
    


