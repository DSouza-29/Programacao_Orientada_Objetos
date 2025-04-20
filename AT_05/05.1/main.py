from cartoes import DiaDosNamorados, Natal, Aniversario, CartaoWeb

if __name__ == "__main__":
    cartao: CartaoWeb
    
    nome1 = input("Digite o nome para o cartão de Dia dos Namorados: ")
    nome2 = input("Digite o nome para o cartão de Natal: ")
    nome3 = input("Digite o nome para o cartão de Aniversário: ")

    print("\n--- Mensagens dos Cartões ---\n")
    cartao = DiaDosNamorados(nome1)
    cartao.showMessage()

    print()

    cartao = Natal(nome2)
    cartao.showMessage()

    print()

    cartao = Aniversario(nome3)
    cartao.showMessage()

    # Polimorfismo ocorre quando a variável 'cartao', do tipo CartaoWeb,
    # é usada para referenciar objetos de diferentes subclasses.
    # Ao chamar o método showMessage(), o Python executa o método correspondente à classe real do objeto.
    # Isso permite reutilizar a mesma referência para diferentes comportamentos, dependendo do tipo do objeto atribuído.