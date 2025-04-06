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

from proprietario import Proprietario
from veiculo import Veiculo

proprietario1 = Proprietario()

nome = input("Digite o nome do proprietário: ")
cpf = int(input("Informe o CPF do proprietário: "))
endereco = input("Informe o Endereço do proprietário: ")
dia = int(input("Informe o dia de nascimento do proprietário: "))
mes = int(input("Informe o mês de nascimento do proprietário: "))
ano = int(input("Informe o ano de nascimento do proprietário: "))

proprietario1.set_nome(nome)
proprietario1.set_cpf(cpf)
proprietario1.set_endereco(endereco)
proprietario1.set_data_nascimento(dia,mes,ano)

veiculo1 = Veiculo("Volkswagen",2020,proprietario1)

print("Informações do Veículo:")
print(f"Placa: {veiculo1.get_placa()}")
print(f"Modelo: {veiculo1.get_modelo()}")
print(f"Ano: {veiculo1.get_ano()}")

print("\nInformações do Proprietário:")
print(f"Nome: {proprietario1.get_nome()}")
print(f"CPF: {veiculo1.get_proprietario().get_cpf()}")
print(f"Endereço: {veiculo1.get_proprietario().get_endereco()}")
print(f"Data de Nascimento: {veiculo1.get_proprietario().get_data_nascimento()}")