"""Exercício: Sistema de Cadastro de Veículos
Crie uma classe Proprietario que tenha os seguintes atributos:nome (string),cpf (int)
endereco (string),  data_nascimento (datetime)
O construtor deve permitir a passagem de valores como parâmetros ou, caso não sejam fornecidos, utilizar valores padrão.
Crie uma classe Veiculo com os atributos:placa (string),modelo (string),ano (int)
proprietario (do tipo Proprietario)
Implemente um programa que:
a) Instancie um objeto do tipo Proprietario apenas com os valores padrão.
b) Solicite os dados do proprietário (nome, CPF, endereço e data de nascimento) e atribua aos atributos do objeto usando métodos modificadores.
c) Instancie um objeto do tipo Veiculo, passando valores para todos os atributos no momento da instanciação.
Nota: A placa do veículo deve ser gerada automaticamente no formato "ABC-1234".
d) Exiba todas as informações do veículo e do proprietário, utilizando métodos de acesso."""

from datetime import datetime as dt

class Proprietario:
    def __init__(self, nome="None", cpf=0, endereco="None", data_nascimento=dt(1900, 1, 1)):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.data_nascimento = data_nascimento

    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome

    def get_cpf(self):
        return self.cpf
    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_endereco(self):
        return self.endereco
    def set_endereco(self, endereco):
        self.endereco = endereco

    def get_data_nascimento(self):
        return self.data_nascimento
    def set_data_nascimento(self,dia,mes,ano):
        self.data_nascimento = dt(ano,mes,dia)

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"CPF: {self.cpf}\n"
                f"Endereço: {self.endereco}\n"
                f"Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}")