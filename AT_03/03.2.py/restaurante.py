class Restaurante:
    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha

    def descrever_restaurante(self):
        print(f"Nome do Restaurante: {self.nome_restaurante}")
        print(f"Tipo de Cozinha: {self.tipo_cozinha}")

    def abrir_restaurante(self):
        print(f"O restaurante {self.nome_restaurante} está aberto!")

    def __str__(self):
        return f"Restaurante: {self.nome_restaurante}, Cozinha: {self.tipo_cozinha}"

