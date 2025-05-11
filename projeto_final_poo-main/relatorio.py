from persistencia import *
from persistencia import professores, inicializar_dados
# Função para relatar alunos aprovados
def relatorio_alunos_aprovados():
    print("\n\\\\\\Alunos Aprovados//////")
    for aluno in alunos:
        for disciplina in aluno.disciplinas:
            notas = aluno.notas_por_disciplina.get(disciplina.nome, [])
            if len(notas) >= 3:  # Verificando se temos as 3 notas
                media = notas[2]  # A terceira nota é a média
                if media >= 7:
                    print(f"Aluno: {aluno.nome}\nDisciplina: {disciplina.nome}\nMédia: {media}\n")

# Função para relatar alunos reprovados
def relatorio_alunos_reprovados():
    print("\n\\\\\Alunos Reprovados//////")
    for aluno in alunos:
        for disciplina in aluno.disciplinas:
            notas = aluno.notas_por_disciplina.get(disciplina.nome, [])
            if len(notas) >= 3:  # Verificando se temos as 3 notas
                media = notas[2]  # A terceira nota é a média
                if media < 7:
                    print(f"Aluno: {aluno.nome}\nDisciplina: {disciplina.nome}\nMédia: {media}\n")


"""1"""
# Função para relatar professores com mais de X alunos
# def relatorio_professores_com_mais_de_x_alunos(x):
#     print(f"\n\\\\\\Professores com mais de 10 alunos//////")
#     for professor in professores:
#         for disciplina in professor.disciplinas:
#             num_alunos = len(disciplina.alunos_matriculados)
#             if num_alunos > 2:
#                 print(f"Professor: {professor.nome} | Disciplina: {disciplina.nome} | Alunos: {num_alunos}")

"""2"""
# def relatorio_professores_com_mais_de_x_alunos(x):
#     x = 4
#     print(f"\\\Professores com mais de {x} alunos//////")
#     for professor in professores:
#         total_alunos = 0
#         for disciplina in professor.disciplinas:
#             num_alunos = len(disciplina.alunos_matriculados)
#             total_alunos += num_alunos
#         if total_alunos > x:
#             print(f"Professor: {professor.nome} | Total de Alunos: {total_alunos}")
#             for disciplina in professor.disciplinas:
#                 num_alunos = len(disciplina.alunos_matriculados)
#                 print(f"  - Disciplina: {disciplina.nome} | Alunos: {num_alunos}")



"""3"""
def relatorio_professores_com_mais_de_x_alunos(x):
    
    print(f"\\\\Professores com mais de {x} alunos//////")
    for professor in professores:
        total_alunos = sum(len(disciplina.alunos_matriculados) for disciplina in professor.disciplinas)
        if total_alunos > x:
            print(f"Professor: {professor.nome} | Total de Alunos: {total_alunos}")

# Função para relatar estatísticas gerais
def relatorio_estatisticas_gerais():
    total_alunos = len(alunos)
    total_professores = len(professores)
    total_disciplinas = len(disciplinas)

    print("\nEstatísticas Gerais:")
    print(f"Número total de alunos: {total_alunos}")
    print(f"Número total de professores: {total_professores}")
    print(f"Número total de disciplinas: {total_disciplinas}")

    print("\nMédia Geral de Notas por Disciplina:")
    for disciplina in disciplinas:
        notas_totais = []
        for aluno in disciplina.alunos_matriculados:
            notas = aluno.notas_por_disciplina.get(disciplina.nome, [])
            if len(notas) >= 3:  # Verificando se temos as 3 notas
                notas_totais.append(notas[2])  # Adicionando a média de cada aluno
        if notas_totais:
            media_disciplina = sum(notas_totais) / len(notas_totais)
            print(f"Disciplina: {disciplina.nome} | Média Geral: {media_disciplina:.2f}")

# Função principal para inicializar dados e gerar os relatórios
def gerar_relatorios():
    inicializar_dados()

    # Relatórios
    relatorio_alunos_aprovados()
    relatorio_alunos_reprovados()
    relatorio_professores_com_mais_de_x_alunos(5)  # Exemplo: X = 5 alunos
    relatorio_estatisticas_gerais()


