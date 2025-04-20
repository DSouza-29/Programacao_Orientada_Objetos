""" 1)	Implemente a classe Funcionario com nome, rg, salario, data de admissão na empresa (datetime) e os métodos aumentar_salario( ), calcular_salario_anual( ) e __srt__( ) - imprime os valores do funcionário de maneira organizada. A data de admissão do funcionário será informada nada instanciação do objeto e o salário anual considera o décimo terceiro.

A.	Crie a classe Assistente, que é filha de Funcionário, que possui um número de matrícula (faça os métodos getters e setters). Sobrescreva o método __srt__().

B.	O número de matrícula é um número aleatório entre 2000 e 9999.

C.	Sabendo que os Assistentes Técnicos possuem um bônus salarial e que os Assistentes Administrativos possuem um turno (dia ou noite) e um adicional noturno, crie as classes Tecnico e Administrativo e sobrescreva o método calcular_salario_anual( ) de ambas as classes (Administrativo e Tecnico). Pense numa maneira de lidar com bônus e adicional.

D.	Por fim, crie um arquivo separado que importe todas as classes, instancie um objeto de cada classe e faça uso de todos os métodos criados em todas as classes. Teste também o método __str__( ). """

from datetime import datetime as dt
from random import randint as ri

class Funcionario:
    def __init__(self,nome="Não Informado",rg=000,salario=000):
        self.nome = nome
        self.rg = rg
        self.salario = salario
        self.data_admissao = dt.now()

    def aumentar_salario(self, aumento): #Aumento é em percentual (10%)
        self.salario += self.salario*(aumento/100)
        print(f"Houve um aumento salarial de {aumento}%")
        print(f"Novo salário é de {self.salario} reais")
    
    def calcular_salario_anual(self):
        print(f"Salário Anual: {13*self.salario}")
    
    def get_nome(self):
        return self.nome
    def set_nome(self,novo_nome):
        self.nome = novo_nome

    def get_rg(self):
        return self.rg
    def set_rg(self,novo_rg):
        self.rg = novo_rg

    def get_salario(self):
        return self.salario
    def set_salario(self,novo_salario):
        self.salario = novo_salario

    def __str__(self):
        obj_str = "\nDados Funcionais\n"
        obj_str+= f"Nome: {self.nome}\nRG: {self.rg}\nSalário: R${self.salario},00\n"
        return obj_str

class Assistente(Funcionario):
    def __init__(self, nome="Não Informado", rg=0, salario=0):
        super().__init__(nome, rg, salario)
        self.matricula = ri(2000,9999)

    def get_matricula(self):
        return self.matricula
    def set_matricula(self,nova_matricula):
        self.matricula = nova_matricula
    
    def __str__(self):
        obj_str = super().__str__()
        obj_str+= f"Matrícula: {self.matricula}\n"
        return obj_str

class AssistenteTecnico(Assistente):
    def __init__(self, nome="Não Informado", rg=0, salario=0):
        super().__init__(nome, rg, salario)
        self.bonus = 20 #20% de bônus
        self.salario = self.salario + self.salario*(self.bonus/100)
    
    def __str__(self):
        obj_str = super().__str__()
        obj_str+= f"Bônus: {self.bonus}%\n"
        return obj_str

funcionario = Funcionario("Kaio",100200300400,5000)
assistente = Assistente("Jaio",800700600,4000)
assistente_tecnico = AssistenteTecnico("Maio",400300500600,20000)
print(funcionario)
print(assistente)
print(assistente_tecnico)
