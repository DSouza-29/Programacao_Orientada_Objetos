lista_tarefas = []

while True:
    print("\n---Lista de Tarefas---")
    print("1 - Adicionar Tarefa")
    print("2 - Concluir Tarefa")
    print("3 - Visualizar Tarefas")
    
    opcao = input("Digite a opção: ")
    
    if opcao == "1":
        titulo = input("Digite o título")
        descricao = input("Digite a descrição da tarefa")
        tarefa = {
            "Título" :  titulo,
            "Descrição" :  descricao,
            "Status" : "Pendente"
         }
        lista_tarefas.append(tarefa)
        print("Tarefa adicionada")
    
    elif opcao == "2":
        titulo = input("Digite o título da tarefa para Concluir")
        if tarefa in lista_tarefas:
            if tarefa["Título"] == titulo:
                tarefa ["Status"] = "Concluído"
                print("Tarefa concluída")
            else:
                print("Tarefa não encontrada.")
        else:
            print("Não há tarefas")
    
    elif opcao == "3":
        if lista_tarefas:
            print("\n-Tarefas Pendentes-")
            for tarefa in lista_tarefas:
                if tarefa["Status"] == "Pendente":
                    print(f" {tarefa['Título']} \n {tarefa['Descrição']}\n")
                
            print("\n-Tarefas Concluídas-")
            for tarefa in lista_tarefas:
                if tarefa["Status"] == "Concluído":
                    print(f" {tarefa['Título']}\n {tarefa['Descrição']}\n")