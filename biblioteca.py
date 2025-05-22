class Livro:
    def __init__(self, titulo, autor, ano_de_publicacao, status, ):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao
        self.status = status

    def editar_livro(self, novo_titulo, novo_autor, novo_ano_de_publicacao, novo_status, ):
        self.titulo = novo_titulo
        self.autor = novo_autor
        self.ano_de_publicacao = novo_ano_de_publicacao
        self.status = novo_status

    def informacoes_do_livro(self):
       return  f" Título: {self.titulo} \n Autor: {self.autor} \n Ano de publicação: {self.ano_de_publicacao} \n Status: {self.status}"
        
    def marcar_como_emprestado(self):
        self.status = "Emprestado"

    def marcar_como_disponivel(self):
        self.status = "Disponível"


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_livros = []

    def adicionar_livro(self, livro:Livro):
        self.lista_de_livros.append(livro)
      
    def listar_livros(self):
        if len(self.lista_de_livros) == 0:
            print("Nenhum livro cadastrado.\n ")
        for x in self.lista_de_livros:
            print(f"{x.informacoes_do_livro()} \n")
