from flask import Flask, jsonify, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://doadmin:AVNS_erI8p2wSSm0gckO83UU@banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com:25060/teste'

db = SQLAlchemy(app)

class teste(db.Model):
    id_teste = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)

    def to_json(self):
        return {'ID': self.id_teste, 'nome': self.nome, 'email': self.email}

#Seleciona todos
@app.route('/testes', methods=['GET'])
def seleciona_testes():
    testes_objetos = teste.query.all()
    testes_json = [teste.to_json() for teste in testes_objetos]
    
    return jsonify({'testes': testes_json}, 'ok')

#Seleciona por ID
@app.route('/teste/<id_teste>', methods=['GET'])
def seleciona_teste(id_teste):
    teste_objeto = teste.query.filter_by(id_teste=id_teste).first()
    teste_json = teste_objeto.to_json()
    
    return jsonify({'teste': teste_json}, 'ok')


@app.route('/teste', methods=['POST'])
def cria_teste():
    body = request.get_json()

    try:
        teste = teste(nome = body['nome'], email = body['email'])
        db.session.add(teste)
        db.session.commit()

        return jsonify({'teste': teste.to_json()}, 'Criado com sucesso!')
    
    except Exception as erro:
        print(erro)

        return jsonify({''}, 'Erro ao cadastrar')
    
app.run()