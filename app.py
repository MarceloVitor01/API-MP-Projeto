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

class usuarios(db.Model):
    id_usuario = db.Column(db.Integer, primary_key = True)
    nome_usuario = db.Column(db.String(98))
    funcao = db.Column(db.String(98))
    login = db.Column(db.String(98))
    senha = db.Column(db.String(98))

    def to_json(self):
        return {'id_usuario': self.id_usuario,
                'nome_usuario': self.nome_usuario,
                'funcao': self.funcao,
                'login': self.login,
                'senha': self.senha
                }
    
#Seleciona todos os usuários
@app.route('/usuarios', methods=['GET'])
def seleciona_usuarios():
    usuarios_objetos = usuarios.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    
    return jsonify(usuarios_json)

#Seleciona um usuário com base no id_usuario
@app.route('/usuario/<id_usuario>', methods=['GET'])
def seleciona_usuario(id_usuario):
    usuario_objeto = usuarios.query.filter_by(id_usuario = id_usuario).first()
    usuario_json = usuario_objeto.to_json()
    
    return jsonify({'Usuários': usuario_json}, f'O usuário com id {id_usuario} foi listado')

#Cria um usuário
@app.route('/usuarios', methods=['POST'])
def cria_usuario():
    body = request.get_json()

    try:
        usuario_objeto = usuarios(nome_usuario = body['nome_usuario'], funcao = body['funcao'], login = body['login'], senha = body['senha'])
        db.session.add(usuario_objeto)
        db.session.commit()

        return jsonify({'Usuários': usuario_objeto.to_json()}, 'Usuário adicionado com sucesso')
    
    except Exception as erro:
        return jsonify({'Usuário: '}, 'Erro ao criar usuário')
    
#Atualiza um usuário com base no id_usuario
@app.route('/usuario/<id_usuario>', methods = ['PUT'])    
def atualiza_usuario(id_usuario):
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

        return jsonify({'Usuário': usuario_objeto.to_json()}, 'Usuário atualizado com sucesso')
    
    except Exception as erro:
        return jsonify({'Usuário: '}, 'Erro ao atualizar usuário')


#Deleta um usuário com base no id_usuario
@app.route('/usuario/<id_usuario>', methods = ['DELETE'])
def deleta_usuario(id_usuario):
    usuario_objeto = usuarios.query.filter_by(id_usuario = id_usuario).first()
    if usuarios.funcao == "ADM"
    try:
        db.session.delete(usuario_objeto)
        db.session.commit()

        return jsonify({'Usuário': usuario_objeto.to_json()}, 'Usuário deletado com sucesso')
    
    except Exception as erro:
        return jsonify({'Usuário: '}, 'Erro ao deletar usuário')
    
class restaurantes(db.Model):
    id_restaurantes = db.Column(db.Integer, primary_key = True)
    nome_restaurante = db.Column(db.String(98))
    distancia_totem = db.Column(db.String(98))
    def to_json(self):
        return {'id_restaurante': self.id_restaurante,
                'nome_restaurante': self.nome_restaurante,
                'distancia_totem': self.distancia_totem,
                }
    
#Seleciona todos os restaurantes
@app.route('/', methods=['GET'])
def seleciona_restaurantes():
    restaurantes_objetos = restaurantes.query.all()
    restaurantes_json = [restaurante.to_json() for restaurante in restaurantes_objetos]
    
    return jsonify(restaurantes_json)

#Seleciona um restaurante com base no id_restaurante
@app.route('/restaurante/<id_restaurante>', methods=['GET'])
def seleciona_restaurante(id_restaurante):
    restaurante_objeto = restaurantes.query.filter_by(id_restaurante = id_restaurante).first()
    restaurante_json = restaurante_objeto.to_json()
    
    return jsonify({'Restaurantes': restaurante_json}, f'O restaurante com id {id_restaurante} foi listado')

#Cria um restaurante
@app.route('/restaurantes', methods=['POST'])
def cria_restaurante():
    body = request.get_json()

    try:
        restaurante_objeto = restaurantes(nome_restaurante = body['nome_restaurante'], distancia_totem = ['distancia_totem'])
        db.session.add(restaurante_objeto)
        db.session.commit()

        return jsonify({'Restaurantes': restaurante_objeto.to_json()}, 'Usuário adicionado com sucesso')
    
    except Exception as erro:
        return jsonify({'Restaurante: '}, 'Erro ao criar restaurante')
    
#Atualiza um restauranterestaurante/<id_restaurante>', methods = ['PUT'])    
def atualiza_restaurante(id_restaurante):
    restaurante_objeto = restaurantes.query.filter_by(id_restaurante = id_restaurante).first()
    body = request.get_json()

    try:
        if('id_restaurante' in body):
            restaurante_objeto.id_restaurante = body['id_restaurante']

        if('nome_restaurante' in body):
            restaurante_objeto.nome_restaurante = body['nome_restaurante']

        if('distancia_totem' in body):
            restaurante_objeto.totem = body['distancia_totem']

        db.session.add(restaurante_objeto)
        db.session.commit()

        return jsonify({'Restaurante': restaurante_objeto.to_json()}, 'Restaurante atualizado com sucesso')
    
    except Exception as erro:
        return jsonify({'Restaurante: '}, 'Erro ao atualizar restaurante')


#Deleta um restaurante com base no id_restaurante
@app.route('/restaurante/<id_restaurante>', methods = ['DELETE'])
def deleta_restaurante(id_restaurante):
    restaurante_objeto = restaurantes.query.filter_by(id_restaurante = id_restaurante).first()

    try:
        db.session.delete(restaurante_objeto)
        db.session.commit()

        return jsonify({'Restaurante': restaurante_objeto.to_json()}, 'Restaurante deletado com sucesso')
    
    except Exception as erro:
        return jsonify({'Restaurante: '}, 'Erro ao deletar restaurante')
    

    
#rotas de erro
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')


app.run()