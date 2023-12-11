from flask import Flask, jsonify, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as connector
from flask_cors import CORS
from hashlib import sha256;
import json

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://doadmin:AVNS_erI8p2wSSm0gckO83UU@banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com:25060/teste'

db = SQLAlchemy(app)

#-----------------------------------Usuários-----------------------------------
class usuarios(db.Model):
    '''Classe que define a tabela usuarios do BD'''
    id_usuario = db.Column(db.Integer, primary_key = True)
    nome_usuario = db.Column(db.String(98))
    funcao = db.Column(db.String(98))
    login = db.Column(db.String(98))
    senha = db.Column(db.Text)

    def set_senha(self, senha: str):
        self.senha = sha256(senha.encode('utf-8')).hexdigest()

    def to_json(self):
        '''Retorna um usuario no formato json'''
        return {'id_usuario': self.id_usuario,
                'nome_usuario': self.nome_usuario,
                'funcao': self.funcao,
                'login': self.login,
                'senha': self.senha
                } 

@app.route('/login', methods=['POST'])
def login():
    login = request.json.get('login')
    senha = request.json.get('senha')

    usuario = usuarios.query.filter_by(login=login).first()
    if usuario and usuario.senha == sha256(senha.encode('utf-8')).hexdigest():
        # Autenticação bem-sucedida
        return jsonify({'authenticated': True, 'id_usuario': usuario.id_usuario, 'funcao': usuario.funcao}), 200
    else:
        # Autenticação falhou
        return jsonify('Usario e/ou Senha Inválida, ou caixa de função não foi preenchida'), 401

    
@app.route('/usuario', methods=['GET'])
def seleciona_usuarios():
    '''Seleciona todos os usuarios'''
    usuarios_objetos = usuarios.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    
    return jsonify(usuarios_json)

@app.route('/usuario/<id_usuario>', methods=['GET'])
def seleciona_usuario(id_usuario):
    '''Seleciona um usuario com base no id_usuario'''
    usuario_objeto = usuarios.query.get(id_usuario)
    usuario_json = usuario_objeto.to_json()
    
    return jsonify(usuario_json)

@app.route('/usuario', methods=['POST'])
def cria_usuario():
    '''Cria um novo usuario'''
    body = request.get_json()

    try:

        login_existente = usuarios.query.filter_by(login=body['login']).first()

        
        if login_existente:
            return jsonify({'error': 'Login já existe'}), 409
        
        usuario_objeto = usuarios(nome_usuario = body['nome_usuario'], funcao = body['funcao'], login = body['login'])
        usuario_objeto.set_senha(body['senha']) #Criptografando a senha
        db.session.add(usuario_objeto)
        db.session.commit()
        usuario_json = usuario_objeto.to_json()

        return jsonify(usuario_json), 201
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/usuario/<id_usuario>', methods = ['PUT'])    
def atualiza_usuario(id_usuario):
    '''Atualiza um usuario com base no id_usuario'''
    usuario_objeto = usuarios.query.get(id_usuario)
    body = request.get_json()

    try:
        if('id_usuario' in body):
            usuario_objeto.id_usuario = body['id_usuario']

        if('nome_usuario' in body):
            usuario_objeto.nome_usuario = body['nome_usuario']

        if('funcao' in body):
            usuario_objeto.funcao = body['funcao']

        if('login' in body):
            usuario_objeto.login = body['login']

        if('senha' in body):
            usuario_objeto.senha = body['senha']

        db.session.add(usuario_objeto)
        db.session.commit()
        usuario_json = usuario_objeto.to_json()

        return jsonify(usuario_json)
    
    except Exception as erro:
        return jsonify(erro)

@app.route('/usuario/<id_usuario>', methods = ['DELETE'])
def deleta_usuario(id_usuario):
    '''Deleta um usuario com base no id_usuario'''
    usuario_objeto = usuarios.query.get(id_usuario)
    # if usuarios.funcao == "ADM":
    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        usuario_json = usuario_objeto.to_json()

        return jsonify(usuario_json)
    
    except Exception as erro:
        return jsonify(erro)
    

#-----------------------------------Produtos-----------------------------------
class produtos(db.Model):
    '''Classe que define a tabela produtos do BD'''
    id_produto = db.Column(db.Integer, primary_key = True)
    nome_produto = db.Column(db.String(98))
    fk_id_restaurante = db.Column(db.Integer)
    preco = db.Column(db.Float)
    descricao = db.Column(db.String(298))
    url_imagem = db.Column(db.Text)

    def to_json(self):
        '''Retorna um produto no formato json'''
        return {
                'id_produto': self.id_produto,
                'nome_produto': self.nome_produto,
                'fk_id_restaurante': self.fk_id_restaurante,
                'preco': self.preco,
                'descricao': self.descricao,
                'url_imagem': self.url_imagem
                }

@app.route('/produto', methods = ['GET'])
def seleciona_produtos():
    #Seeciona todos os produtos
    produtos_objetos = produtos.query.all()
    produtos_json = [produto.to_json() for produto in produtos_objetos]

    return jsonify(produtos_json)

@app.route('/produto/<id_produto>', methods = ['GET'])
def seleciona_produto(id_produto):
    '''Seleciona um produto com base no id_produto'''
    produto_objeto = produtos.query.get(id_produto)
    produto_json = produto_objeto.to_json()

    return jsonify(produto_json)

@app.route('/produto', methods = ['POST'])
def cria_produto():
    '''Cria um novo produto'''
    body = request.get_json()

    try:
        produto_objeto = produtos(nome_produto = body['nome_produto'], fk_id_restaurante = body['fk_id_restaurante'], preco = body['preco'], descricao = body['descricao'], url_imagem = body['url_imagem'])
        db.session.add(produto_objeto)
        db.session.commit()
        produto_json = produto_objeto.to_json()

        return jsonify(produto_json)
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/produto/<id_produto>', methods = ['PUT'])
def atualiza_produto(id_produto):
    '''Atualiza um produto com base no id_produto'''
    produto_objeto = produtos.query.get(id_produto)
    body = request.get_json()

    try:
        if('id_produto' in body):
            produto_objeto.id_produto = body['id_produto']

        if('nome_produto' in body):
            produto_objeto.nome_produto = body['nome_produto']

        if('fk_id_restaurante' in body):
            produto_objeto.fk_id_restaurante = body['fk_id_restaurante']

        if('preco' in body):
            produto_objeto.preco= body['preco']

        if('descricao' in body):
            produto_objeto.descricao = body['descricao']


        db.session.add(produto_objeto)
        db.session.commit()
        produto_json = produto_objeto.to_json()

        return jsonify(produto_json)
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/produto/<id_produto>', methods = ['DELETE'])
def deleta_produto(id_produto):
    '''Deleta um produto com base no id_produto'''
    produto_objeto = produtos.query.get(id_produto)

    try:
        db.session.delete(produto_objeto)
        db.session.commit()
        produto_json = produto_objeto.to_json()

        return jsonify(produto_json)
    
    except Exception as erro:
        return jsonify(erro)
    

#-----------------------------------Restaurantes-----------------------------------    
class restaurantes(db.Model):
    '''Classe que define a tabela restaurantes do BD'''
    id_restaurante = db.Column(db.Integer, primary_key = True)
    nome_restaurante = db.Column(db.String(98))
    distancia_totem = db.Column(db.Float)
    url_logo = db.Column(db.Text)
    login = db.Column(db.String(98))
    senha = db.Column(db.Text)

    def set_senha(self, senha: str):
        self.senha = sha256(senha.encode('utf-8')).hexdigest()

    def to_json(self):
        '''Retorna um restaurante no formato json'''
        return {
                'id_restaurante': self.id_restaurante,
                'nome_restaurante': self.nome_restaurante,
                'distancia_totem': self.distancia_totem,
                'url_logo': self.url_logo,
                'login': self.login,
                'senha': self.senha
                }

@app.route('/login_restaurante', methods=['POST'])
def login_restaurante():
    login = request.json.get('login')
    senha = request.json.get('senha')

    restaurante = restaurantes.query.filter_by(login = login).first()
    if restaurante and restaurante.senha == sha256(senha.encode('utf-8')).hexdigest():
        # Autenticação bem-sucedida
        return jsonify({'authenticated': True, 'id_restaurante': restaurante.id_restaurante}), 200
    else:
        # Autenticação falhou
        return jsonify('Login ou Senha Inválida'), 401
    
@app.route('/restaurante', methods = ['GET'])
def seleciona_restaurantes():
    '''Seleciona todos os restaurantes'''
    restaurantes_objetos = restaurantes.query.all()
    restaurantes_json = [restaurante.to_json() for restaurante in restaurantes_objetos]

    return jsonify(restaurantes_json)

@app.route('/restaurante/<id_restaurante>', methods = ['GET'])
def seleciona_restaurante(id_restaurante):
    '''Seleciona um restaurante com base no id_restaurante'''
    restaurante_objeto = restaurantes.query.get(id_restaurante)
    restaurante_json = restaurante_objeto.to_json()

    return jsonify(restaurante_json)

@app.route('/restaurante', methods = ['POST'])
def cria_restaurante():
    '''Cria um novo restaurante'''
    body = request.get_json()

    try:
        login_existente = restaurantes.query.filter_by(login = body['login']).first()
        qtd_restaurantes = len(restaurantes.query.all())
        if login_existente:
            return jsonify({'error': 'Login já existe'}), 409
        if qtd_restaurantes>17:
            return jsonify({'error': 'Já existem 18 restaurantes, o limite da praça de alimentação.'}), 409

        restaurante_objeto = restaurantes(nome_restaurante = body['nome_restaurante'], distancia_totem = body['distancia_totem'], url_logo = body['url_logo'], login = body['login'])
        restaurante_objeto.set_senha(body['senha']) #Criptografando a senha
        db.session.add(restaurante_objeto)
        db.session.commit()
        restaurante_json = restaurante_objeto.to_json()

        return jsonify(restaurante_json)
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/restaurante/<id_restaurante>', methods = ['PUT'])
def atualiza_restaurante(id_restaurante):
    '''Atualiza um restaurante com base no id_restaurante'''
    restaurante_objeto = restaurantes.query.get(id_restaurante)
    body = request.get_json()

    try:
        if('id_restaurante' in body):
            restaurante_objeto.id_restaurante = body['id_restaurante']

        if('nome_restaurante' in body):
            restaurante_objeto.nome_restaurante = body['nome_restaurante']

        if('distancia_totem' in body):
            restaurante_objeto.distancia_totem = body['distancia_totem']

        if('login' in body):
            restaurante_objeto.login = body['login']

        if('senha' in body):
            restaurante_objeto.senha = body['senha']

        db.session.add(restaurante_objeto)
        db.session.commit()
        restaurante_json = restaurante_objeto.to_json()

        return jsonify(restaurante_json)
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/restaurante/<id_restaurante>', methods = ['DELETE'])
def deleta_restaurante(id_restaurante):
    '''Deleta um restaurante com base no id_restaurante'''
    restaurante_objeto = restaurantes.query.get(id_restaurante)

    try:
        db.session.delete(restaurante_objeto)
        db.session.commit()
        restaurante_json = restaurante_objeto.to_json()

        return jsonify(restaurante_json)
    
    except Exception as erro:
        return jsonify(erro)
    

#-----------------------------------Pesquisas Produtos-----------------------------------
class pesquisas_produto(db.Model):
    '''Classe que define uma pesquisa por produto no BD'''
    id_pesquisa_produto = db.Column(db.Integer, primary_key = True)
    fk_id_usuario = db.Column(db.Integer)
    fk_id_produto = db.Column(db.Integer)

    def to_json(self):
        '''Retorna uma pesquisa por produto no formato json'''
        return {
            'id_pesquisa_produto': self.id_pesquisa_produto,
            'fk_id_usuario': self.fk_id_usuario,
            'fk_id_produto': self.fk_id_produto
        }
    

@app.route('/pesquisa_produto', methods = ['GET'])
def seleciona_pesquisas_produto():
    '''Seleciona todas as pesquisas por produto'''
    pesquisas_produto_objetos = pesquisas_produto.query.all()
    pesquisas_produto_json = [pesquisa_produto.to_json() for pesquisa_produto in pesquisas_produto_objetos]

    return jsonify(pesquisas_produto_json)

@app.route('/pesquisa_produto/<id_pesquisa_produto>', methods = ['GET'])
def seleciona_pesquisa_produto(id_pesquisa_produto):
    '''Seleciona uma pesquisa por produto com base no id_pesquisa_produto'''
    pesquisa_produto_objeto = pesquisas_produto.query.get(id_pesquisa_produto)
    pesquisa_produto_json = pesquisa_produto_objeto.to_json()

    return jsonify(pesquisa_produto_json)

@app.route('/pesquisa_produto', methods = ['POST'])
def cria_pesquisa_produto():
    '''Cria uma nova pesquisa por produto'''
    body = request.get_json()

    try:
        pesquisa_produto_objeto = pesquisas_produto(fk_id_usuario = body['fk_id_usuario'], fk_id_produto = body['fk_id_produto'])
        db.session.add(pesquisa_produto_objeto)
        db.session.commit()
        pesquisa_produto_json = pesquisa_produto_objeto.to_json()

        return jsonify(pesquisa_produto_json)
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/pesquisa_produto/<id_pesquisa_produto>', methods = ['SET'])
def atualiza_pesquisa_produto(id_pesquisa_produto):
    '''Atualiza uma pesquisa_produto com base no id_pesquisa_produto'''
    pesquisa_produto_objeto = pesquisas_produto.query.filter_by(id_pesquisa_produto = id_pesquisa_produto).first()
    body = request.get_json()

    try:
        if('id_pesquisa_produto' in body):
            pesquisa_produto_objeto.id_pesquisa_produto = body['id_pesquisa_produto']

        if('fk_id_usuario' in body):
            pesquisa_produto_objeto.fk_id_usuario = body['fk_id_usuario']

        if('fk_id_produto' in body):
            pesquisa_produto_objeto.fk_id_produto = body['fk_id_produto']

        db.session.add(pesquisa_produto_objeto)
        db.session.commit()
        pesquisa_produto_json = pesquisa_produto_objeto.to_json()

        return jsonify(pesquisa_produto_json)
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/pesquisa_produto/<id_pesquisa_produto>', methods = ['DELETE'])
def deleta_pesquisa_produto(id_pesquisa_produto):
    '''Deleta uma pesquisa por produto com base no id_pesquisa_produto'''
    pesquisa_produto_objeto = pesquisas_produto.query.get(id_pesquisa_produto)

    try:
        db.session.delete(pesquisa_produto_objeto)
        db.session.commit()
        pesquisa_produto_json = pesquisa_produto_objeto.to_json()

        return jsonify(pesquisa_produto_json)
    
    except Exception as erro:
        return jsonify(erro)
    
    
#-----------------------------------Pesquisas Restaurantes-----------------------------------
class pesquisas_restaurante(db.Model):
    '''Classe que define uma pesquisa por restaurante no BD'''
    id_pesquisa_restaurante = db.Column(db.Integer, primary_key = True)
    fk_id_usuario = db.Column(db.Integer)
    fk_id_restaurante = db.Column(db.Integer)
    date = db.Column(db.String(50))

    def to_json(self):
        '''Retorna uma pesquisa por restaurante no formato json'''
        return {
            'id_pesquisa_restaurante': self.id_pesquisa_restaurante,
            'fk_id_usuario': self.fk_id_usuario,
            'fk_id_restaurante': self.fk_id_restaurante,
            'data': self.data
        }
    

@app.route('/pesquisa_restaurante', methods = ['GET'])
def seleciona_pesquisas_restaurante():
    '''Seleciona todas as pesquisas por restaurante'''
    pesquisas_restaurante_objetos = pesquisas_restaurante.query.all()
    pesquisas_restaurante_json = [pesquisa_restaurante.to_json() for pesquisa_restaurante in pesquisas_restaurante_objetos]

    return jsonify(pesquisas_restaurante_json)

@app.route('/pesquisa_restaurante/<id_pesquisa_restaurante>', methods = ['GET'])
def seleciona_pesquisa_restaurante(id_pesquisa_restaurante):
    '''Seleciona uma pesquisa por restaurante com base no id_pesquisa_restaurante'''
    pesquisa_restaurante_objeto = pesquisas_restaurante.query.get(id_pesquisa_restaurante)
    pesquisa_restaurante_json = pesquisa_restaurante_objeto.to_json()

    return jsonify(pesquisa_restaurante_json)

@app.route('/pesquisa_restaurante', methods = ['POST'])
def cria_pesquisa_restaurante():
    '''Cria uma nova pesquisa por restaurante'''
    body = request.get_json()

    try:
        pesquisa_restaurante_objeto = pesquisas_restaurante(fk_id_usuario = body['fk_id_usuario'], fk_id_restaurante = body['fk_id_restaurante'])
        db.session.add(pesquisa_restaurante_objeto)
        db.session.commit()
        pesquisa_restaurante_json = pesquisa_restaurante_objeto.to_json()

        return jsonify(pesquisa_restaurante_json)
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/pesquisa_restaurante/<id_pesquisa_restaurante>', methods = ['SET'])
def atualiza_pesquisa_restaurante(id_pesquisa_restaurante):
    '''Atualiza uma pesquisa_restaurante com base no id_pesquisa_restaurante'''
    pesquisa_restaurante_objeto = pesquisas_restaurante.query.filter_by(id_pesquisa_restaurante = id_pesquisa_restaurante).first()
    body = request.get_json()

    try:
        if('id_pesquisa_restaurante' in body):
            pesquisa_restaurante_objeto.id_pesquisa_restaurante = body['id_pesquisa_restaurante']

        if('fk_id_usuario' in body):
            pesquisa_restaurante_objeto.fk_id_usuario = body['fk_id_usuario']

        if('fk_id_restaurante' in body):
            pesquisa_restaurante_objeto.fk_id_restaurante = body['fk_id_restaurante']

        db.session.add(pesquisa_restaurante_objeto)
        db.session.commit()
        pesquisa_restaurante_json = pesquisa_restaurante_objeto.to_json()

        return jsonify(pesquisa_restaurante_json)
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/pesquisa_restaurante/<id_pesquisa_restaurante>', methods = ['DELETE'])
def deleta_pesquisa_restaurante(id_pesquisa_restaurante):
    '''Deleta uma pesquisa por restaurante com base no id_pesquisa_restaurante'''
    pesquisa_restaurante_objeto = pesquisas_restaurante.query.filter_by(id_pesquisa_restaurante = id_pesquisa_restaurante).first()

    try:
        db.session.delete(pesquisa_restaurante_objeto)
        db.session.commit()
        pesquisa_restaurante_json = pesquisa_restaurante_objeto.to_json()

        return jsonify(pesquisa_restaurante_json)
    
    except Exception as erro:
        return jsonify(erro)


@app.route('/pesquisa_restaurante/<nome_restaurante>', methods=['GET'])
def pesquisar_restaurante(nome_restaurante):
    #Seleciona restaurantes com base no nome
    restaurantes_pelo_nome = restaurantes.query.filter_by(nome_restaurante = nome_restaurante)
    restaurantes_pelo_nome_json = [restaurante.to_json() for restaurante in restaurantes_pelo_nome]

    return jsonify(restaurantes_pelo_nome_json)




@app.route('/pesquisar_prato/<nome_produto>', methods=['GET'])
def pesquisar_prato(nome_produto):
    #Seleciona pratos com base no nome
    produtos_pelo_nome = produtos.query.filter_by(nome_produto = nome_produto)
    produtos_pelo_nome_json = [produto.to_json() for produto in produtos_pelo_nome]

    return jsonify(produtos_pelo_nome_json)

@app.route('/filtrar_maior_distancia', methods=['GET'])
def filtrar_maior_distancia():
    #Lista os produtos em ordem descrescente de distância do restaurante
    restaurantes_menor_dist = restaurantes.query.order_by(restaurantes.distancia_totem)
    restaurantes_maior_dist = []

    for i in range(len(restaurantes_menor_dist)-1, -1, -1):
        restaurantes_maior_dist.append(restaurantes_menor_dist[i])

    restaurantes_ordenados_json = [restaurante_dist.to_json() for restaurante_dist in restaurantes_maior_dist]
    return jsonify(restaurantes_ordenados_json)

@app.route('/filtrar_menor_distancia', methods=['GET'])
def filtrar_menor_distancia():
    #Lista os produtos em ordem ascendente de distância do restaurante
    restaurantes_menor_dist = restaurantes.query.order_by(restaurantes.distancia_totem)

    restaurantes_ordenados_json = [restaurante_dist.to_json() for restaurante_dist in restaurantes_menor_dist]
    return jsonify(restaurantes_ordenados_json)


@app.route('/filtrar_menor_preco', methods=['GET'])
def filtrar_menor_preco():
    #Lista os produtos em ordem de menor preço
    produtos_menor_preco = produtos.query.order_by(produtos.distancia_totem)

    produtos_ordenados_json = [produto_barato.to_json() for produto_barato in produtos_menor_preco]
    return jsonify(produtos_ordenados_json)

@app.route('/filtrar_maior_preco', methods=['GET'])
def filtrar_maior_preco():
    #Lista os produtos em ordem de maior preço
    produtos_menor_preco = produtos.query.order_by(produtos.distancia_totem)
    produtos_maior_preco = []

    for i in range(len(produtos_menor_preco)-1, -1, -1):
        produtos_maior_preco.append(produtos_menor_preco[i])

    produtos_ordenados_json = [produto_caro.to_json() for produto_caro in produtos_maior_preco]
    return jsonify(produtos_ordenados_json)

#rotas de erro
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('internal_server_error.html')

app.run()