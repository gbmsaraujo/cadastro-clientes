class CadastroType:
    def __init__(
        self,
        nome: str = None,
        idade: int = None,
        bairro: str = None,
        profissao: str = None,
    ):
        self.nome = nome
        self.idade = idade
        self.bairro = bairro
        self.profissao = profissao
