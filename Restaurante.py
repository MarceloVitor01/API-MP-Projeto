class Restaurante:
    '''Classe que representa o Restaurante'''
    def __init__(self, id_restaurante: int, nome_restaurante: str, distancia_totem: float):
        self.id_restaurante = id_restaurante
        self.nome_restaurante = nome_restaurante
        self.distancia_totem = distancia_totem

    def get_id_restaurante(self) -> int:
        '''Função que retorna o id_restaurante'''
        return self.id_restaurante

    def set_id_restaurante(self, id_restaurante: int):
        '''Função que define o id_restaurante'''
        self.id_restaurante = id_restaurante

    def get_nome_restaurante(self) -> str:
        '''Função que retorna o nome_restaurante'''
        return self.nome_restaurante

    def set_nome_restaurante(self, nome_restaurante: str):
        '''Função que define o nome_restaurante'''
        self.nome_restaurante = nome_restaurante

    def get_distancia_totem(self) -> float:
        '''Função que retorna a distância do restaurante até o totem'''
        return self.distancia_totem

    def set_distancia_totem(self, distancia_totem: float):
        '''Função que define a distância do restaurante até o totem'''
        self.distancia_totem = distancia_totem

    def __str__(self):
        return f'ID do Restaurante: {self.id_restaurante}\nNome do Restaurante: {self.nome_restaurante}'