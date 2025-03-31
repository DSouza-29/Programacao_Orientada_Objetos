class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco



livro1 = Livro("Capitães de Areia", "Jorge Amado", 1937, 65.90)
livro2 = Livro("Auto da Compadecida", "Ariano Suassuna", 1955, 52.50)


print(f"Título: {livro1.titulo}, Autor: {livro1.autor}, Ano: {livro1.ano_publicacao}, Preço: R${livro1.preco:.2f}")
print(f"Título: {livro2.titulo}, Autor: {livro2.autor}, Ano: {livro2.ano_publicacao}, Preço: R${livro2.preco:.2f}")