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
    nome_usuario = db.Column(db.String(100))
    funcao = db.Column(db.String(100))
    login = db.Column(db.String(100))
    senha = db.Column(db.String(100))

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

    try:
        db.session.delete(usuario_objeto)
        db.session.commit()

        return jsonify({'Usuário': usuario_objeto.to_json()}, 'Usuário deletado com sucesso')
    
    except Exception as erro:
        return jsonify({'Usuário: '}, 'Erro ao deletar usuário')
    
#rotas de erro
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')


app.run()