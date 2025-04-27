

class Veiculo:
    total_veiculos = 0

    def __init__(self, placa, modelo, diaria):
        self.__placa = placa
        self.modelo = modelo
        self.diaria = diaria
        self.__alugado = False
        Veiculo.total_veiculos += 1 

    @property
    def placa(self):
        """Propriedade para acessar a placa (apenas leitura)"""
        return self.__placa

    @placa.setter
    def placa(self, valor):
        """Impedir alteração da placa e exibir mensagem"""
        print("A placa não pode ser modificada.")

    def alugar(self):
        """Marca o veículo como alugado (se estiver disponível)"""
        if not self.__alugado:
            self.__alugado = True
            print(f"Veículo {self.modelo} ({self.placa}) alugado com sucesso!")
        else:
            print(f"Veículo {self.modelo} ({self.placa}) já está alugado.")

    def devolver(self):
        """Marca o veículo como disponível (se estiver alugado)"""
        if self.__alugado:
            self.__alugado = False
            print(f"Veículo {self.modelo} ({self.placa}) devolvido com sucesso!")
        else:
            print(f"Veículo {self.modelo} ({self.placa}) não está alugado.")

    def status(self):
        """Exibe o status do veículo (alugado ou disponível)"""
        if self.__alugado:
            return f"Veículo {self.modelo} ({self.placa}) está alugado."
        else:
            return f"Veículo {self.modelo} ({self.placa}) está disponível."

    @classmethod
    def mostrar_total_veiculos(cls):
        """Exibe o total de veículos cadastrados"""
        print(f"Total de veículos cadastrados: {cls.total_veiculos}")

    @staticmethod
    def calcular_preco_aluguel(dias, diaria):
        """Calcula o preço do aluguel com base nos dias e valor da diária"""
        return dias * diaria

