class Produto:
    '''Classe que representa o Produto'''
    def __init__(self, id_produto: int, nome_produto: str, fk_id_restaurante: int):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.fk_id_restaurante = fk_id_restaurante

    def get_id_produto(self) -> int:
        '''Função que retorna o id_produto'''
        return self.id_produto

    def set_id_produto(self, id_produto: int):
        '''Função que define o id_produto'''
        self.id_produto = id_produto

    def get_nome_produto(self) -> str:
        '''Função que retorna o nome_produto'''
        return self.nome_produto

    def set_nome_produto(self, nome_produto: str):
        '''Função que define o nome_produto'''
        self.nome_produto = nome_produto

    def get_fk_id_restaurante(self) -> int:
        '''Função que retorna o o id do restaurante responsável pelo prato'''
        return self.fk_id_restaurante

    def set_fk_id_restaurante(self, fk_id_restaurante: int):
        '''Função que define o o id do restaurante responsável pelo prato'''
        self.fk_id_restaurante = fk_id_restaurante
    
    def __str__(self):
        return f'ID do Produto: {self.id_produto}, Nome do Produto: {self.nome_produto}, ID do Restaurante {self.fk_id_restaurante}'
        