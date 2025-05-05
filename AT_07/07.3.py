from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.__cpf = cpf
        self.data_nascimento = data_nascimento

    @abstractmethod
    def exibir_dados(self):
        pass

    def get_cpf(self):
        return self.__cpf

class Aluno(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, matricula):
        super().__init__(nome, cpf, data_nascimento)
        self.__matricula = matricula
        self.__notas = []
        self.disciplinas = []

    def adicionar_nota(self, nota):
        self.__notas.append(nota)

    def exibir_dados(self):
        print(f"Aluno: {self.nome}, CPF: {self.get_cpf()}, Nascimento: {self.data_nascimento}, Matrícula: {self.__matricula}")
        print(f"Notas: {self.__notas}")
        print("Disciplinas:")
        for d in self.disciplinas:
            print(f"  - {d.nome}")

class Professor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, siape):
        super().__init__(nome, cpf, data_nascimento)
        self.__siape = siape
        self.disciplinas = []

    def exibir_dados(self):
        print(f"Professor: {self.nome}, CPF: {self.get_cpf()}, Nascimento: {self.data_nascimento}, SIAPE: {self.__siape}")
        print("Disciplinas:")
        for d in self.disciplinas:
            print(f"  - {d.nome}")

class Disciplina:
    def __init__(self, codigo, nome, professor_responsavel):
        self.codigo = codigo
        self.nome = nome
        self.professor_responsavel = professor_responsavel
        self.alunos_matriculados = []

    def exibir_informacoes(self):
        print(f"Disciplina: {self.nome} (Código: {self.codigo})")
        print(f"Professor Responsável: {self.professor_responsavel.nome}")
        print("Alunos matriculados:")
        for aluno in self.alunos_matriculados:
            print(f"  - {aluno.nome}")



def ler_professores(caminho):
    professores = []
    disciplinas_criadas = []

    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            for linha in f:
                partes = linha.strip().split('|')
                siape, nome, cpf, data_nasc = partes[:4]
                nomes_disciplinas = partes[4].split(',')

                professor = Professor(nome, cpf, data_nasc, siape)

                for nome_disciplina in nomes_disciplinas:
                    d = Disciplina(codigo=f"D{len(disciplinas_criadas)+1:03}", nome=nome_disciplina.strip(), professor_responsavel=professor)
                    professor.disciplinas.append(d)
                    disciplinas_criadas.append(d)

                professores.append(professor)
    except FileNotFoundError:
        print(f"Arquivo {caminho} não encontrado.")
    except Exception as e:
        print(f"Erro ao ler professores: {e}")

    return professores, disciplinas_criadas

def ler_alunos(caminho, disciplinas_disponiveis):
    alunos = []
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            for linha in f:
                partes = linha.strip().split('|')
                nome, cpf, data_nasc, matricula = partes[:4]
                aluno = Aluno(nome, cpf, data_nasc, matricula)

                for bloco in partes[4:]:
                    dados = bloco.split(',')
                    nome_disciplina = dados[0].strip()
                    notas = list(map(float, dados[1:]))

                    disciplina = next((d for d in disciplinas_disponiveis if d.nome == nome_disciplina), None)
                    if disciplina:
                        aluno.disciplinas.append(disciplina)
                        disciplina.alunos_matriculados.append(aluno)
                        for nota in notas:
                            aluno.adicionar_nota(nota)
                    else:
                        print(f"Disciplina '{nome_disciplina}' não encontrada para o aluno {nome}.")

                alunos.append(aluno)
    except FileNotFoundError:
        print(f"Arquivo {caminho} não encontrado.")
    except Exception as e:
        print(f"Erro ao ler alunos: {e}")
    return alunos

def ler_disciplinas(caminho, professores, alunos):
    disciplinas = []
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            for linha in f:
                codigo, nome_disc, nome_prof, nomes_alunos = linha.strip().split('|')
                professor = next((p for p in professores if p.nome == nome_prof), None)
                if not professor:
                    print(f"Professor '{nome_prof}' não encontrado.")
                    continue

                disciplina = Disciplina(codigo, nome_disc.strip(), professor)
                professor.disciplinas.append(disciplina)

                for nome_aluno in nomes_alunos.split(','):
                    aluno = next((a for a in alunos if a.nome == nome_aluno.strip()), None)
                    if aluno:
                        disciplina.alunos_matriculados.append(aluno)
                        aluno.disciplinas.append(disciplina)
                    else:
                        print(f"Aluno '{nome_aluno}' não encontrado.")

                disciplinas.append(disciplina)
    except FileNotFoundError:
        print(f"Arquivo {caminho} não encontrado.")
    except Exception as e:
        print(f"Erro ao ler disciplinas: {e}")
    return disciplinas


professores, disciplinas_professores = ler_professores("professores.txt")
alunos = ler_alunos("alunos.txt", disciplinas_professores)
disciplinas_extras = ler_disciplinas("disciplinas.txt", professores, alunos)

todas_disciplinas = disciplinas_professores + [d for d in disciplinas_extras if d not in disciplinas_professores]

print("\n--- Alunos ---")
for a in alunos:
    a.exibir_dados()

print("\n--- Professores ---")
for p in professores:
    p.exibir_dados()

print("\n--- Disciplinas ---")
for d in todas_disciplinas:
    d.exibir_informacoes()
