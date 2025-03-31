"""Crie uma classe chamada Carro. A classe deve ter um método construtor que inicializa os seguintes atributos:
marca: a marca do carro.
modelo: o modelo do carro.
ano: o ano de fabricação do carro.
cor: a cor do carro.
Crie dois objetos dessa classe, cada um com atributos diferentes, e imprima as informações dos carros."""



class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    
carro1 = Carro("Fiat", "Uno", 1998, "Prata")
carro2 = Carro("Ford", "Ka", 2022, "Branco")

print("Carro 1:")
print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"Ano: {carro1.ano}")
print(f"Cor: {carro1.cor}")

print("\nCarro 2:")
print(f"Marca: {carro2.marca}")
print(f"Modelo: {carro2.modelo}")
print(f"Ano: {carro2.ano}")
print(f"Cor: {carro2.cor}")