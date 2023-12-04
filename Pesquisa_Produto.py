class Pesquisa_Produto:
    '''Classe que representa a Pesquisa por Produto'''
    def __init__(self, id_pesquisa_produto: int, fk_id_usuario: int, fk_id_produto: int) -> bool:
        self.id_pesquisa_produto = id_pesquisa_produto
        self.fk_id_usuario = fk_id_usuario
        self.fk_id_produto = fk_id_produto

    def get_id_pesquisa_produto(self) -> int:
        '''Função que retorna o id_pesquisa_produto'''
        return self.id_pesquisa_produto
    
    def set_id_pesquisa_produto(self, id_pesquisa_produto: int):
        '''Função que define o id_pesquisa_produto'''
        self.id_pesquisa_produto = id_pesquisa_produto

    def get_fk_id_usuario(self) -> int:
        '''Função que retorna o id do usuário que fez a pesquisa'''
        return self.fk_id_usuario
    
    def set_fk_id_usuario(self, fk_id_usuario: int):
        '''Função que define o id do usuário que fez a pesquisa'''
        self.fk_id_usuario = fk_id_usuario

    def get_fk_id_produto(self) -> int:
        '''Função que retorna o id do produto que está sendo pesquisado'''
        return self.fk_id_produto
    
    def set_fk_id_produto(self, fk_id_produto: int):
        '''Função que retorna o id do produto que está sendo pesquisado'''
        self.fk_id_produto = fk_id_produto