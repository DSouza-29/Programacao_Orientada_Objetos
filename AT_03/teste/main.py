"""Vou tentar replicar o programa do cadastro de proprietário de carro"""

from proprietario import Proprietario


proprietario1 = Proprietario()

nome = input("Digite seu nome: ")
cpf = int(input("Digite seu CPF: "))
dia = int(input("Digite o dia que nasceu: "))
mes = int(input("Digite o mes que naceu: "))
ano = int(input("Digite o ano em que naceu: "))

proprietario1.set_nome(nome)
proprietario1.set_cpf(cpf)
proprietario1.set_data_nascimento(dia, mes, ano)

print(proprietario1d)