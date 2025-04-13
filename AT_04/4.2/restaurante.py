class Restaurante:
    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha
        self.numeroServidos = 0  # valor padrão

    def descrever_restaurante(self):
        print(f"Nome do Restaurante: {self.nome_restaurante}")
        print(f"Tipo de Cozinha: {self.tipo_cozinha}")

    def abrir_restaurante(self):
        print(f"O restaurante {self.nome_restaurante} está aberto!")

    def getNumeroServidos(self):
        return self.numeroServidos

    def setNumeroServidos(self, numero):
        if numero >= 0:
            self.numeroServidos = numero
        else:
            print("Número de servidos não pode ser negativo.")

    def incrementeNumeroServidos(self, quantidade):
        if quantidade > 0:
            novo_total = self.getNumeroServidos() + quantidade
            self.setNumeroServidos(novo_total)
        else:
            print("A quantidade deve ser positiva.")

    def __str__(self):
        return f"Restaurante: {self.nome_restaurante},\nCozinha: {self.tipo_cozinha},\nClientes Servidos no Total: {self.numeroServidos}"
