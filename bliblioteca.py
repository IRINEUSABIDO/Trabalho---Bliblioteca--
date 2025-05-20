class Livro:
    def __init__(self, titulo:str, autor:str, ano_de_publicacao:int, status:str):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao
        self.status = status

    def editar_livro(self, novo_titulo:str, novo_autor:str, novo_ano_de_publicacao:int, novo_status:str):
        self.titulo = novo_titulo
        self.autor = novo_autor
        self.ano_de_publicacao = novo_ano_de_publicacao
        self.status = novo_status

    def informacoes_do_livro(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de publicação: {self.ano_de_publicacao}")
        print(f"Status: {self.status}")
        

class Biblioteca:
    def __init__(self, nome:str):
        self.nome = nome
        self.lista_de_livros = []

    def adicionar_livro(self, livro:Livro):
        self.lista_de_livros.append(livro)
      
    def listar_livros(self):
        for x in self.lista_de_livros:
            x.informacoes_do_livro()


Senhor_dos_aneis = Livro("O senhor dos aneis", "J.R.R. Tolkien", 1954, "Disponível")
Pedro = Biblioteca("Biblioteca do Pedro")

Pedro.adicionar_livro(Senhor_dos_aneis)
Pedro.listar_livros()