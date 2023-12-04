from Conexao import ConexaoBD

conn = ConexaoBD.conecta_bd()

class Usuario:
    '''Classe representando o Usuário'''
    def __init__(self, id_usuario: int, nome_usuario: str, funcao: str, login: str, senha: str):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.funcao = funcao
        self.login = login
        self.senha = senha

    def get_id_usuario(self) -> int:
        '''Função que retorna o id_usuario'''
        return self.id_usuario
    
    def set_id_usuario(self, id_usuario: int):
        '''Função que define o id_usuario'''
        self.id_usuario = id_usuario

    def get_nome_usuario(self) -> str:
        '''Função que retorna o nome_usuario'''
        return self.nome_usuario
    
    def set_nome_usuario(self, nome_usuario: str):
        '''Função que define o nome_usuario'''
        self.nome_usuario = nome_usuario

    def get_funcao(self) -> str:
        '''Função que retorna a função do usuário'''
        return self.funcao
    
    def set_funcao(self, funcao: str):
        '''Função que define a função do usuário'''
        self.funcao = funcao

    def get_login(self) -> str:
        '''Função que retorna o login do usuário'''
        return self.login

    def set_login(self, login: str):
        '''Função que define o login do usuário'''
        self.login = login

    def get_senha(self) -> str:
        '''Função que retorna a senha do usuário'''
        return self.senha
    
    def set_senha(self, senha: str):
        '''Função que define a senha do usuário'''
        self.senha = senha

    def __str__(self):
        '''Função que retorna o usuário no formato "ID Usuário: Nome: Função: Login: "'''
        return f'\nID Usuário: {self.id_usuario}\nNome: {self.nome_usuario}\nFunção: {self.funcao}\nLogin: {self.login}\n'
    
    def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'nome': self.nome,
            'funcao': self.funcao,
            'login': self.login,
            'senha': self.senha
        }

class UsuarioDAO:
    def __init__(self, conn):
        self.conn = conn

    def criar_usuario(self, usuario: Usuario):
        sql = 'INSERT INTO usuarios (id_usuario, nome, funcao, login, senha) VALUES (%s, %s, %s, %s, %s)'

        id_usuario = usuario.get_id_usuario()
        nome = usuario.get_nome()
        funcao = usuario.get_funcao()
        login = usuario.get_login()
        senha = usuario.get_senha()

        cursor = self.conn.cursor()
        cursor.execute(sql, (id_usuario, nome, funcao, login, senha))
        self.conn.commit()
        cursor.close()