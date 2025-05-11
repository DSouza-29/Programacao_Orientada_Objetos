class Disciplina:
    def __init__(self, codigo, nome, professor_responsavel):
        self.codigo = codigo
        self.nome = nome
        self.professor_responsavel = professor_responsavel
        self.alunos_matriculados = []

        professor_responsavel.adicionar_disciplina(self) 

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_matriculados:
                self.alunos_matriculados.append(aluno)

    def exibir_dados(self):
        info = f"Disciplina: {self.nome} ({self.codigo})"
        info += f"\n  Professor Responsável: {self.professor_responsavel.nome}"
        if self.alunos_matriculados:
            info += "\n  Alunos Matriculados:"
            for aluno in self.alunos_matriculados:
                info += f"\n    - {aluno.nome}"
        return info
