from datetime import datetime
import random

class Proprietario():
    def __init__(self, nome="Nome", cpf=0, endereco= "Padão", data_nascimento=datetime(1900,1,1)):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.data_nascimento = data_nascimento

    def set_nome(self,nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome
    
    def set_cpf(self,cpf):
        self.cpf = cpf
    
    def get_cpf(self):
        return self.cpf
    
    def set_endereco(self, endereco):
        self.endereco = endereco
    
    def get_endereco(self):
        return self.endereco
    
    def set_data_nascimento(self, dia, mes, ano):
        self.data_nascimento = datetime(dia, mes, ano)




    def __str__(self):
        obj_str = f"\\\\\ Proprietário /////"
        obj_str +=f"Nome: {self.nome}"
        obj_str +=f"CPF: {self.cpf}"
        obj_str +=f"Endereco: {self.endereco}"
        obj_str +=f"Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}"

class Veiculo():
    def __init__(self, marca = "padão", modelo = "padrão", ano = 0, proprietário= Proprietario):
        self.placa = f"{''.join(random.choice('ABCDEGHIJKLNOPQRSTUVWXYZ', K=3))}-{random.randint(1000,9999)}"
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.proprietario = proprietário

