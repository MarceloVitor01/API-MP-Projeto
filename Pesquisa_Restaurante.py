class Pesquisa_Restaurante:
    '''Classe que representa a Pesquisa por Restaurante'''
    def __init__(self, id_pesquisa_restaurante: int, fk_id_usuario: int, fk_id_restaurante: int) -> bool:
        self.id_pesquisa_restaurante = id_pesquisa_restaurante
        self.fk_id_usuario = fk_id_usuario
        self.fk_id_restaurante = fk_id_restaurante

    def get_id_pesquisa_restaurante(self) -> int:
        '''Função que retorna o id_pesquisa_restaurante'''
        return self.id_pesquisa_restaurante
    
    def set_id_pesquisa_restaurante(self, id_pesquisa_restaurante: int):
        '''Função que define o id_pesquisa_restaurante'''
        self.id_pesquisa_restaurante = id_pesquisa_restaurante

    def get_fk_id_usuario(self) -> int:
        '''Função que retorna o id do usuário que fez a pesquisa'''
        return self.fk_id_usuario
    
    def set_fk_id_usuario(self, fk_id_usuario: int):
        '''Função que define o id do usuário que fez a pesquisa'''
        self.fk_id_usuario = fk_id_usuario

    def get_fk_id_restaurante(self) -> int:
        '''Função que retorna o id do restaurante que está sendo pesquisado'''
        return self.fk_id_restaurante
    
    def set_fk_id_restaurante(self, fk_id_restaurante: int):
        '''Função que retorna o id do restaurante que está sendo pesquisado'''
        self.fk_id_restaurante = fk_id_restaurante