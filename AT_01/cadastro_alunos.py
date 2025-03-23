alunos = {}



while True:
    print("\n ---- Alunos ----")
    print(" 1 - Adicionar aluno.")
    print(" 2 - Altualizar notas.")
    print(" 3 - Remover Aluno.")
    print(" 4 - Exibir todos os alunos.")
    print(" 5 - Calcular e exibir a nota de cada aluno.")
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        nome = input("Digite o nome do aluno")
        if nome in alunos:
            print("Aluno já cadastrado")
        else:
            n1 = float(input("Digite nota 1: "))
            n2 = float(input("Digite nota 2: "))
            n3 = float(input("Digite nota 3: "))
            n4 = float(input("Digite nota 4: "))
            
            alunos[nome] = [n1, n2, n3, n4]
            print(f" # Aluno {nome} cadastrado com sucesso. #\n")
            
    elif opcao == 2:
        nome = input("Digite o nome do Aluno: ")
        if nome in alunos:
            nova_nota_1 = float(input("Digite a nova nota 1: "))
            nova_nota_2 = float(input("Digite a nova nota 2: "))
            nova_nota_3 = float(input("Digite a nova nota 3: "))
            nova_nota_4 = float(input("Digite a nova nota 4: "))
            alunos[nome] = [nova_nota_1, nova_nota_2, nova_nota_3, nova_nota_4]
            print("Notas atualizadas\n")
            
        else:
            print("Aluno não encontrado. \n")
            
    elif opcao == 3:
        nome = input("Digite o nome do aluno: ")
        if nome in alunos:
            del alunos[nome]
            print("Aluno excluido com sucesso\n")
            
        else:
            print("\nAluno não encontrado.")
        
    elif opcao == 4:
        if alunos:
            print("---Lista de Alunos---\n")
            for nome, notas in alunos.items():
                print(f"Nome: {nome}\nNotas: {notas}\n")
        

    elif opcao == 5:
        if alunos:
            print("---Média dos Alunos---")
            for nome, notas in alunos.items():
                media = sum(notas) / len(notas)
                print(f"Aluno: {nome}\nMédia: {media:.2f}")
                if media >= 7:
                    print("Aluno Aprovado\n")
                elif media < 7:
                    print("Aluno de Recuperação\n")
        else:
            print("Sem alunos cadastrados.")