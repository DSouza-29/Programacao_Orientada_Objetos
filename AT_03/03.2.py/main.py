from restaurante import Restaurante


restaurante1 = Restaurante("Sabores do Brasil", "Brasileira")
restaurante2 = Restaurante("Cantina Italiana", "Italiana")
restaurante3 = Restaurante("Sushi Zen", "Japonesa")

restaurante1.descrever_restaurante()
restaurante2.descrever_restaurante()
restaurante3.descrever_restaurante()

print("\nInformações dos restaurantes usando __str__:")
print(restaurante1)
print(restaurante2)
print(restaurante3)