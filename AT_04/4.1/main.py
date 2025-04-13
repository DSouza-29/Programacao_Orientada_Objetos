from datetime import datetime
import random
from usuario import Usuario
from conta import Conta, ContaPoupanca, ContaCorrente, ContaEspecial


print("=== Cadastro de Usuário ===")
rg = int(input("Digite o RG do usuário: "))
cpf = int(input("Digite o CPF do usuário: "))
nome = input("Digite o nome do usuário: ")
dia = int(input("Digite o dia que nasceu: "))
mes = int(input("Digite o mês que nasceu: "))
ano = int(input("Digite o ano que nasceu: "))

usuario = Usuario()
usuario.set_rg(rg)
usuario.set_cpf(cpf)
usuario.set_nome(nome)
usuario.set_data_nascimento(dia, mes, ano)



print("\nTipos de Conta:")
print("1 - Conta Comum")
print("2 - Conta Poupança")
print("3 - Conta Corrente")
print("4 - Conta Especial")
tipo = int(input("Escolha o tipo da conta: "))

agencia = random.randint(100, 999)
data_abertura = datetime.now()
saldo = float(input("Digite o saldo inicial da conta: "))



if tipo == 1:
    conta = Conta(agencia, usuario, data_abertura, saldo)
elif tipo == 2:
    taxa_juros = float(input("Digite a taxa de juros (ex: 0.02 para 2%): "))
    conta = ContaPoupanca(agencia, usuario, data_abertura, saldo, taxa_juros)
elif tipo == 3:
    limite = float(input("Digite o limite da conta corrente: "))
    conta = ContaCorrente(agencia, usuario, data_abertura, saldo, limite)
elif tipo == 4:
    limite = float(input("Digite o limite comum: "))
    limite_especial = float(input("Digite o limite especial: "))
    conta = ContaEspecial(agencia, usuario, data_abertura, saldo, limite, limite_especial)
else:
    print("Tipo inválido, criando Conta Comum por padrão.")
    conta = Conta(agencia, usuario, data_abertura, saldo)


print("\n=== Dados do Usuário ===")
print(usuario)
print("=== Dados da Conta ===")
print(conta)
