from datetime import datetime
import random
from usuario import Usuario
from conta import Conta


usuario = Usuario()


rg = int(input("Digite o RG do usuário: "))
cpf = int(input("Digite o CPF do usuário: "))
nome = input("Digite o nome do usuário: ")
dia = int(input("Digite o dia que nasceu: "))
mes = int(input("Digite o mes que nasceu: "))
ano = int(input("Digite o ano que nasceu: "))


usuario.set_rg(rg)
usuario.set_cpf(cpf)
usuario.set_nome(nome)
usuario.set_data_nascimento(dia, mes, ano)


agencia = random.randint(0, 999)
data_abertura = datetime.now()
saldo = float(input("Digite o saldo inicial da conta: "))

conta = Conta(agencia, usuario, data_abertura, saldo)


print("\nDados da Conta:")
print(conta)
print("\nDados do Usuário:")
print(conta.get_usuario())