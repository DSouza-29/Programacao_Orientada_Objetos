from pessoa import Aluno, Professor
from disciplina import Disciplina
from persistencia import *
import datetime

def cadastrar_aluno(nome, cpf, nascimento, matricula):
    data_nasc = datetime.datetime.strptime(nascimento, "%Y-%m-%d").date()
    aluno = Aluno(nome, cpf, data_nasc, matricula)
    salvar_aluno(aluno)
    return aluno

def cadastrar_professor(nome, cpf, nascimento, siape):
    data_nasc = datetime.datetime.strptime(nascimento, "%Y-%m-%d").date()
    professor = Professor(nome, cpf, data_nasc, siape)
    salvar_professor(professor)
    return professor

def cadastrar_disciplina(codigo=0, nome="padrão", professor="padrão"):
    disciplina = Disciplina(codigo, nome, professor)
    salvar_disciplina(disciplina)
    return disciplina


#----------------------------------------------------



def desmatricular_aluno(cpf, disciplina_nome):
    aluno = next((a for a in alunos if a.get_cpf() == cpf), None)
    if not aluno:
        print(f"Aluno com CPF {cpf} não encontrado.")
        return None

    disciplina = next((d for d in disciplinas if d.nome == disciplina_nome), None)
    if not disciplina:
        print(f"Disciplina {disciplina_nome} não encontrada.")
        return None

    if disciplina not in aluno.disciplinas:
        print(f"Aluno {aluno.nome} não está matriculado na disciplina {disciplina_nome}.")
        return None

    aluno.disciplinas.remove(disciplina)
    disciplina.alunos_matriculados.remove(aluno)
    atualizar_aluno(aluno)
    atualizar_disciplina(disciplina)

    print(f"Aluno {aluno.nome} desmatriculado da disciplina {disciplina_nome} com sucesso.")

# def salvar_todos_alunos():
#     # Atualiza todos os dados dos alunos no arquivo
#     try:
#         with open(arquivo_alunos, "w", encoding="utf-8") as arquivo:
#             for aluno in alunos:
#                 dados_disciplinas = []
#                 for d in aluno.disciplinas:
#                     notas = aluno.notas_por_disciplina.get(d.nome, [])
#                     linha_disc = f"{d.nome}," + ",".join(map(str, notas))
#                     dados_disciplinas.append(linha_disc)

#                 # Monta a linha do aluno com os dados completos
#                 linha = f"{aluno.nome}|{aluno.get_cpf()}|{aluno.data_nascimento}|{aluno.get_matricula()}\n"
                
#                 # Inclui as disciplinas se houver
#                 if dados_disciplinas:
#                     linha += "|".join(dados_disciplinas)
                
#                 # Adiciona a quebra de linha para separar os alunos
#                 linha += "\n"
                
#                 # Escreve no arquivo
#                 arquivo.write(linha)
                
#     finally:
#         print("Todos os alunos foram salvos.")


def salvar_todos_alunos():
    try:
        with open(arquivo_alunos, "w", encoding="utf-8") as arquivo:
            for aluno in alunos:
                # Monta os dados básicos do aluno
                linha = f"{aluno.nome}|{aluno.get_cpf()}|{aluno.data_nascimento}|{aluno.get_matricula()}|"
                
                # Inclui as disciplinas e notas
                dados_disciplinas = []
                for d in aluno.disciplinas:
                    notas = aluno.notas_por_disciplina.get(d.nome, [])
                    linha_disc = f"{d.nome}," + ",".join(map(str, notas))
                    dados_disciplinas.append(linha_disc)
                
                # Adiciona as disciplinas, se existirem
                if dados_disciplinas:
                    linha += "|".join(dados_disciplinas)
                
                # Adiciona a quebra de linha para separar os alunos
                linha += "\n"
                
                # Escreve no arquivo
                arquivo.write(linha)
                
    finally:
        print("Todos os alunos foram salvos.")

def remover_disciplina_do_professor(professor_siape, codigo_disciplina):
    professor = next((p for p in professores if p.get_siape() == professor_siape), None)
    if not professor:
        print(f"Professor com SIAPE {professor_siape} não encontrado.")
        return None

    disciplina = next((d for d in professor.disciplinas if d.codigo == codigo_disciplina), None)
    if not disciplina:
        print(f"Disciplina com código {codigo_disciplina} não encontrada para o professor {professor.nome}.")
        return None

    # Remove a disciplina da lista do professor
    professor.disciplinas.remove(disciplina)

    # Remove o professor da disciplina
    disciplina.professor_responsavel = None

    # Atualiza os dados do professor e da disciplina
    atualizar_professor(professor)
    atualizar_disciplina(disciplina)

    print(f"Disciplina {disciplina.nome} removida do professor {professor.nome} com sucesso.")
