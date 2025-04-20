from abc import ABC,abstractmethod

class Veiculo(ABC): #Classe abstrata
    def __init__(self,marca = "Genérica", modelo = "Genérico") -> None:
        self.marca = marca
        self.modelo = modelo

    @abstractmethod #decorador
    def ligar_luzes(self):
        pass

    @abstractmethod
    def desligar_luzes(self):
        pass

    def __str__(self) -> str:
        obj_str = f"\nMarca: {self.marca}\nModelo: {self.modelo}"
        return obj_str

class Rodoviario(Veiculo): #Obrigatório a implementação dos métodos abstratos.
    def __init__(self, marca="Genérica", modelo="Genérico",qtd_rodas=0, pressao_pneus=0) -> None:
        super().__init__(marca, modelo)
        self.qtd_rodas = qtd_rodas
        self.pressao_pneus = pressao_pneus

    def __str__(self) -> str:
        obj_str = super().__str__()
        obj_str += f"\nQtd Rodas: {self.qtd_rodas}\nPressão Pneus: {self.pressao_pneus}"
        return obj_str

    def ligar_luzes(self):
        print("Ligando Luzes.")

    def desligar_luzes(self):
        print("Desligando Luzes.")

class Bicicleta(Rodoviario):
    def __init__(self, marca="Genérica", modelo="Genérico", qtd_rodas=2, pressao_pneus=0) -> None:
        super().__init__(marca, modelo, qtd_rodas, pressao_pneus)

    def ligar_luzes(self):
        print("\nSou uma bicicleta e não tenho luzes.\n")

veiculos = []

#marca = input("Digite a marca: ")
#modelo = input("Digite o modelo: ")
#veiculo = Veiculo(marca, modelo) #erro: instanciando um objeto de uma classe abstrata
#veiculos.append(veiculo)

marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
qtd_rodas = int(input("Digite a quantidade de rodas: "))
pressao_pneus = float(input("Digite a pressão ideal dos pneus"))
veiculo = Rodoviario(marca,modelo,qtd_rodas,pressao_pneus)
veiculos.append(veiculo)

veiculo = Bicicleta("Monark", "Barra Circular", 2, 18)
veiculos.append(veiculo)

for veiculo in veiculos:
    print(veiculo)
