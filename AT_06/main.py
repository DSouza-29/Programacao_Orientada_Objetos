from veiculo import Veiculo

veiculo1 = Veiculo("ABC-1234", "Fusca", 50.0)
veiculo2 = Veiculo("XYZ-5678", "Civic", 150.0)

veiculo1.alugar()
print(veiculo1.status())

veiculo1.devolver()
print(veiculo1.status())

Veiculo.mostrar_total_veiculos()

preco = Veiculo.calcular_preco_aluguel(5, veiculo1.diaria)
print(f"O preço total do aluguel é: R$ {preco:.2f}")

