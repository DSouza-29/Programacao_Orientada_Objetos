estoque = {}

while True:
    print("----- Gerenciador de Produtos -----")
    print(" 1 - Adicionar item")
    print(" 2 - Revover item")
    print(" 3 - Exibir itens")
    print(" 4 - Alterar quantidade")
    print(" 5 - Sair")
    escolha = int(input("Digite o numero de sua escolha"))
    
    if 1 <= escolha <= 5:
        if escolha == 1:
            nome = input("Produto")
            if nome in estoque:
                print(f"O produto {nome} já exite, por favor alterar a quantidade no local correto. ")
                
                
            else:
                quantidade = int(input("Digite a quantidade"))
                estoque[nome] = quantidade
                print(f"Produto {nome} adicionado com sucesso.")
                
                
        elif escolha == 2:
            nome = input("Digite o produto para exclusão")
            if nome in estoque:
                del estoque[nome]
                print(f"Produto ({nome}) exclido com sucesso.")
                
                
            else:
                print("Produto não encontrado")
        
        elif escolha == 3:
            if not estoque:
                print("Não há itens no estoque")
                
            
            else:
                print("\n --- Lista de Produtos ---1")
                for nome, quantidade in estoque.items():
                    print(f"{nome}: {quantidade} unidades. ")
                    
                
        elif escolha == 4:
            nome = input("Digite o produto que deseja alterar a quantidade")
            if nome in estoque:
                nova_quantidade = int(input("Digite a nova quantidade"))
                estoque[nome] = nova_quantidade
                print(f"Quantidade do produto {nome} alterada para {nova_quantidade}.")
            
            else:
                print("Produto não encontrato.")

            
        elif escolha == 5:
            break
            print("")