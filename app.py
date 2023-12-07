from flask import Flask, jsonify, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as connector
from flask_cors import CORS
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
    senha = db.Column(db.String(98))

    def to_json(self):
        '''Retorna um usuario no formato json'''
        return {'id_usuario': self.id_usuario,
                'nome_usuario': self.nome_usuario,
                'funcao': self.funcao,
                'login': self.login,
                'senha': self.senha
                }
    

@app.route('/usuarios', methods=['GET'])
def seleciona_usuarios():
    '''Seleciona todos os usuarios'''
    usuarios_objetos = usuarios.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    
    return jsonify(usuarios_json)

@app.route('/usuario/<id_usuario>', methods=['GET'])
def seleciona_usuario(id_usuario):
    '''Seleciona um usuario com base no id_usuario'''
    usuario_objeto = usuarios.query.filter_by(id_usuario = id_usuario).first()
    usuario_json = usuario_objeto.to_json()
    
    return jsonify(usuario_json)

@app.route('/usuarios', methods=['POST'])
def cria_usuario():
    '''Cria um novo usuario'''
    body = request.get_json()

    try:
        usuario_objeto = usuarios(nome_usuario = body['nome_usuario'], funcao = body['funcao'], login = body['login'], senha = body['senha'])
        db.session.add(usuario_objeto)
        db.session.commit()
        usuario_json = usuario_objeto.to_json()

        return jsonify(usuario_json)
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/usuario/<id_usuario>', methods = ['PUT'])    
def atualiza_usuario(id_usuario):
    '''Atualiza um usuario com base no id_usuario'''
    usuario_objeto = usuarios.query.filter_by(id_usuario = id_usuario).first()
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
    usuario_objeto = usuarios.query.filter_by(id_usuario = id_usuario).first()
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

    def to_json(self):
        '''Retorna um produto no formato json'''
        return {
                'id_produto': self.id_produto,
                'nome_produto': self.nome_produto,
                'fk_id_restaurante': self.fk_id_restaurante
                'preco': self.preco
                'descricao': self.descricao
                }

@app.route('/produtos', methods = ['GET'])
def seleciona_produtos():
    '''Sleciona todos os produtos'''
    produtos_objetos = produtos.query.all()
    produtos_json = [produto.to_json() for produto in produtos_objetos]

    return jsonify(produtos_json)

@app.route('/produto/<id_produto>', methods = ['GET'])
def seleciona_produto(id_produto):
    '''Seleciona um produto com base no id_produto'''
    produto_objeto = produtos.query.filter_by(id_produto = id_produto).first()
    produto_json = produto_objeto.to_json()

    return jsonify(produto_json)

@app.route('/produtos', methods = ['POST'])
def cria_produto():
    '''Cria um novo produto'''
    body = request.get_json()

    try:
        produto_objeto = produtos(nome_produto = body['nome_produto'], fk_id_restaurante = body['fk_id_restaurante'], preco = body['preco'], descricao = body['descricao'])
        db.session.add(produto_objeto)
        db.session.commit()
        produto_json = produto_objeto.to_json()

        return jsonify(produto_json)
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/produto/<id_produto>', methods = ['PUT'])
def atualiza_produto(id_produto):
    '''Atualiza um produto com base no id_produto'''
    produto_objeto = produtos.query.filter_by(id_produto = id_produto).first()
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
    produto_objeto = produtos.query.filter_by(id_produto = id_produto).first()

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

    def to_json(self):
        '''Retorna um restaurante no formato json'''
        return {
                'id_restaurante': self.id_restaurante,
                'nome_restaurante': self.nome_restaurante,
                'distancia_totem': self.distancia_totem
                }


@app.route('/restaurantes', methods = ['GET'])
def seleciona_restaurantes():
    '''Seleciona todos os restaurantes'''
    restaurantes_objetos = restaurantes.query.all()
    restaurantes_json = [restaurante.to_json() for restaurante in restaurantes_objetos]

    return jsonify(restaurantes_json)

@app.route('/restaurante/<id_restaurante>', methods = ['GET'])
def seleciona_restaurante(id_restaurante):
    '''Seleciona um restaurante com base no id_restaurante'''
    restaurante_objeto = restaurantes.query.filter_by(id_restaurante = id_restaurante).first()
    restaurante_json = restaurante_objeto.to_json()

    return jsonify(restaurante_json)

@app.route('/restaurantes', methods = ['POST'])
def cria_restaurante():
    '''Cria um novo restaurante'''
    body = request.get_json()

    try:
        restaurante_objeto = restaurantes(nome_restaurante = body['nome_restaurante'], distancia_totem = body['distancia_totem'])
        db.session.add(restaurante_objeto)
        db.session.commit()
        restaurante_json = restaurante_objeto.to_json()

        return jsonify(restaurante_json)
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/restaurante/<id_restaurante>', methods = ['PUT'])
def atualiza_restaurante(id_restaurante):
    '''Atualiza um restaurante com base no id_restaurante'''
    restaurante_objeto = restaurantes.query.filter_by(id_restaurante = id_restaurante).first()
    body = request.get_json()

    try:
        if('id_restaurante' in body):
            restaurante_objeto.id_restaurante = body['id_restaurante']

        if('nome_restaurante' in body):
            restaurante_objeto.nome_restaurante = body['nome_restaurante']

        if('distancia_totem' in body):
            restaurante_objeto.distancia_totem = body['distancia_totem']

        db.session.add(restaurante_objeto)
        db.session.commit()
        restaurante_json = restaurante_objeto.to_json()

        return jsonify(restaurante_json)
    
    except Exception as erro:
        return jsonify(erro)
    
@app.route('/restaurante/<id_restaurante>', methods = ['DELETE'])
def deleta_restaurante(id_restaurante):
    '''Deleta um restaurante com base no id_restaurante'''
    restaurante_objeto = restaurantes.query.filter_by(id_restaurante = id_restaurante).first()

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
    

@app.route('/pesquisas_produto', methods = ['GET'])
def seleciona_pesquisas_produto():
    '''Seleciona todas as pesquisas por produto'''
    pesquisas_produto_objetos = pesquisas_produto.query.all()
    pesquisas_produto_json = [pesquisa_produto.to_json() for pesquisa_produto in pesquisas_produto_objetos]

    return jsonify(pesquisas_produto_json)

@app.route('/pesquisa_produto/<id_pesquisa_produto>', methods = ['GET'])
def seleciona_pesquisa_produto(id_pesquisa_produto):
    '''Seleciona uma pesquisa por produto com base no id_pesquisa_produto'''
    pesquisa_produto_objeto = pesquisas_produto.query.filter_by(id_pesquisa_produto = id_pesquisa_produto).first()
    pesquisa_produto_json = pesquisa_produto_objeto.to_json()

    return jsonify(pesquisa_produto_json)

@app.route('/pesquisas_produto', methods = ['POST'])
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
    
@app.route('/pesquisa_produto/<id_pesquisa_produto>')
def deleta_pesquisa_produto(id_pesquisa_produto):
    '''Deleta uma pesquisa por produto com base no id_pesquisa_produto'''
    pesquisa_produto_objeto = pesquisas_produto.query.filter_by(id_pesquisa_produto = id_pesquisa_produto).first()

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
    data = db.Column(date(db.String(50))) #não testei ainda

    def to_json(self):
        '''Retorna uma pesquisa por restaurante no formato json'''
        return {
            'id_pesquisa_restaurante': self.id_pesquisa_restaurante,
            'fk_id_usuario': self.fk_id_usuario,
            'fk_id_restaurante': self.fk_id_restaurante,
            'data': self.data
        }
    

@app.route('/pesquisas_restaurante', methods = ['GET'])
def seleciona_pesquisas_restaurante():
    '''Seleciona todas as pesquisas por restaurante'''
    pesquisas_restaurante_objetos = pesquisas_restaurante.query.all()
    pesquisas_restaurante_json = [pesquisa_restaurante.to_json() for pesquisa_restaurante in pesquisas_restaurante_objetos]

    return jsonify(pesquisas_restaurante_json)

@app.route('/pesquisa_restaurante/<id_pesquisa_restaurante>', methods = ['GET'])
def seleciona_pesquisa_restaurante(id_pesquisa_restaurante):
    '''Seleciona uma pesquisa por restaurante com base no id_pesquisa_restaurante'''
    pesquisa_restaurante_objeto = pesquisas_restaurante.query.filter_by(id_pesquisa_restaurante = id_pesquisa_restaurante).first()
    pesquisa_restaurante_json = pesquisa_restaurante_objeto.to_json()

    return jsonify(pesquisa_restaurante_json)

@app.route('/pesquisas_restaurante', methods = ['POST'])
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
    
@app.route('/pesquisa_restaurante/<id_pesquisa_restaurante>')
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


@app.route('/consultar_produto', methods=['GET'])
def consultar_produto():
    # Obter o nome do produto a ser consultado dos parâmetros da solicitação
    nome_produto = request.args.get('nome_produto')

    # Executar a consulta no banco de dados
    query = "SELECT * FROM produtos WHERE nome = %s"
    cursor.execute(query, (nome_produto,))

    # Obter os resultados da consulta
    resultados = cursor.fetchall()

    # Criar uma lista de dicionários para os resultados
    produtos = []
    for resultado in resultados:
        produto = {
            'id_produto': resultado[0],
            'nome_produto': resultado[1],
            'fk_id_restaurante': resultado[2],
            'preco': resultado[3],
            'descricao': resultado[4],
        }
        produtos.append(produto)

    # Fechar o cursor após a consulta
    cursor.close()

    # Retornar os resultados como JSON
    return jsonify(produtos)


@app.route('/consultar_restaurante', methods=['GET'])
def consultar_restaurante():
    
    nome_restaurante = request.args.get('nome_restaurante')

 
    query = "SELECT * FROM restaurantes WHERE nome = %s"
    cursor.execute(query, (nome_restaurante,))

    # Obter os resultados da consulta
    resultados = cursor.fetchall()

    # Criar uma lista de dicionários para os resultados
    restaurantes = []
    for resultado in resultados:
        restaurante = {
            'id_restaurante': resultado[0],
            'nome_restaurante': resultado[1],
            'distancia_totem':resultado[2]
        }
        restaurantes.append(restaurante)

    # Fechar o cursor após a consulta
    cursor.close()

    # Retornar os resultados como JSON
    return jsonify(restaurantes)


#rotas de erro
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')


app.run()