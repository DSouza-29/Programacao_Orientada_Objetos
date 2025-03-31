"""4) Crie uma classe chamada Pessoa que tenha um método construtor com os seguintes atributos:
nome: o nome da pessoa.
idade: a idade da pessoa.
cidade: a cidade onde a pessoa mora.
Adicione também um método apresentar() que imprime uma mensagem como:
"Olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}."
Crie dois objetos dessa classe com dados diferentes e chame o método apresentar() para ambos."""




class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e moro em {self.cidade}.")


pessoa1 = Pessoa("Denner", 23, "Boa Vista-RR")
pessoa2 = Pessoa("Lineu", 120, "São Paulo")


pessoa1.apresentar()
pessoa2.apresentar()