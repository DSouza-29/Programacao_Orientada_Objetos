from restaurante import Restaurante


nome = input("Digite o nome do restaurante: ")
tipo = input("Digite o tipo de cozinha: ")


restaurante = Restaurante(nome, tipo)


print(f"\nClientes servidos (inicial): {restaurante.getNumeroServidos()}")


novo_valor = int(input("Digite um novo número de clientes servidos: "))
restaurante.setNumeroServidos(novo_valor)
print(f"Clientes servidos até agora: {restaurante.getNumeroServidos()}")


incremento = int(input("Quantos novos clientes foram servidos? "))
restaurante.incrementeNumeroServidos(incremento)
print(f"Clientes servidos ao final do dia: {restaurante.getNumeroServidos()}")


print("\nInformações completas do restaurante:")
print(restaurante)
