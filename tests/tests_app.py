import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db, usuarios, produtos, restaurantes, pesquisas_produto, pesquisas_restaurante

# Configurar o aplicativo para testes
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://doadmin:AVNS_erI8p2wSSm0gckO83UU@banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com:25060/defaultdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
client = app.test_client()

def test_app(app):
    with app.test_client() as client:
        yield client

####################################################################################

def test_cria_usuario(app):
    response = app.test_client().post("/usuario", json={"nome_usuario": "Fulano", 'funcao':'Pessoa Fisica', 'login':'fulano@gmail', 'senha':'123'})
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["nome_usuario"] == "Fulano"
    assert json_data['senha'] == 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'

def test_seleciona_usuario(app):
    response = app.test_client().get("/usuario/1")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["nome_usuario"] == "Fulano"
    assert json_data['login'] == 'fulano@gmail'

def test_atualiza_usuario(app):
    response = app.test_client().put("/usuario/1", json={"nome_usuario": "Beltrano"})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["nome_usuario"] == "Beltrano"

def test_login_certo_usuario(app):
    response = app.test_client().post('/login', json={'login':'fulano@gmail', 'senha':'123'})
    assert response.status_code == 200

def test_login_errado_usuario(app):
    response = app.test_client().post('/login', json={'login':'fulano@gmail', 'senha':'1234'})
    assert response.status_code == 401

def test_deleta_usuario(app):
    response = app.test_client().delete("/usuarios/1")
    assert response.status_code == 204

####################################################################################

def test_criar_produto(app):
    response = app.test_client().post("/produto", json={"nome_produto": "Arroz", 'fk_id_restaurante':1, 'preco':10, 'descricao':'entrada', 'url_imagem':'google.com/images'})
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["nome_produto"] == "Arroz"

def test_seleciona_produto(app):
    response = app.test_client().get("/produto/1")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["nome_produto"] == "Arroz"

def test_atualiza_produto(app):
    response = app.test_client().put("/produto/1", json={"nome_produto": "Feijão"})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["nome"] == "Feijão"

def test_deleta_produto(app):
    response = app.test_client().delete("/produto/1")
    assert response.status_code == 204

####################################################################################

def test_cria_restaurante(app):
    response = app.test_client().post("/restaurante", json={"nome_restaurante": "Burger Donalds", 'distancia_totem':10.5, 'url_logo':'google.com/images', 'login':'bkmc@test', 'senha':'123'})
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["nome_restaurante"] == "Burger Donalds"

def test_seleciona_restaurante(app):
    response = app.test_client().get("/restaurante/1")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["nome_restaurante"] == "Burger Donalds"

def test_atualizar_restaurante(app):
    response = app.test_client().put("/restaurante/1", json={"nome_restaurante": "McKing"})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["nome_restaurante"] == "McKing"

def test_excluir_restaurante(app):
    response = app.test_client().delete("/restaurante/1")
    assert response.status_code == 204

def test_login_certo_restaurante(app):
    response = app.test_client().post('/login_restaurante', json={'login':'bkmc@test', 'senha':'123'})
    assert response.status_code == 200

def test_login_errado_restaurante(app):
    response = app.test_client().post('/login_restaurante', json={'login':'fulano@gmail', 'senha':'1234'})
    assert response.status_code == 401

####################################################################################

@pytest.mark.parametrize("nome_restaurante", ["Restaurante 1", "Restaurante 2"])
def test_pesquisa_restaurante(app, nome_restaurante):
    response = app.test_client().get("/pesquisa_restaurante/{}".format(nome_restaurante))
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data[0]["nome_restaurante"] == nome_restaurante

@pytest.mark.parametrize("nome_produto", ["Prato 1", "Prato 2"])
def test_pesquisa_prato(app, nome_produto):
    response = app.test_client().get("/pesquisar_prato/{}".format(nome_produto))
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data[0]["nome_produto"] == nome_produto

####################################################################################

def test_filtrar_menor_preco(app):
    response = app.test_client().get("/filtrar_menor_preco")
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) > 0
    for produto in json_data:
        assert produto["preco"] > 0

def test_filtrar_maior_preco(app):
    response = app.test_client().get("/filtrar_maior_preco")
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) > 0
    for produto in json_data:
        assert produto["preco"] > 0

def test_filtrar_maior_distancia(app):
    response = app.test_client().get("/filtrar_maior_distancia")
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) > 0
    for restaurante in json_data:
        assert restaurante["distancia_totem"] > 0

def test_filtrar_menor_distancia(app):
    response = app.test_client().get("/filtrar_menor_distancia")
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) > 0
    for restaurante in json_data:
        assert restaurante["distancia_totem"] > 0
