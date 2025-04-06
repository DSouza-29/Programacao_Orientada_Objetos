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

import random
import proprietario

class Veiculo:
    def __init__(self,modelo="None",ano=1900,proprietario=proprietario):
        self.placa = f"{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))}-{random.randint(1000, 9999)}"
        self.modelo = modelo
        self.ano = ano
        self.proprietario = proprietario
    
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_ano(self):
        return self.ano
    def set_ano(self, ano):
        self.ano = ano

    def get_proprietario(self):
        return self.proprietario
    def set_proprietario(self, proprietario):
        self.proprietario = proprietario

    def get_placa(self):
        return self.placa

    def __str__(self):
        return (f"Veículo:\n"
                f"  Placa: {self.placa}\n"
                f"  Modelo: {self.modelo}\n"
                f"  Ano: {self.ano}\n"
                f"  Proprietário: {self.proprietario}")