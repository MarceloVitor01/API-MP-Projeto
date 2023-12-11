import pytest
from app import app, db, produtos

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://doadmin:AVNS_erI8p2wSSm0gckO83UU@banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com:25060/bd_for_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.test_client() as client:
        yield client

def test_criar_produto(client):
    response = client.post("/produto", json={"nome_produto": "Arroz", 'fk_id_restaurante':1, 'preco':10, 'descricao':'entrada', 'url_imagem':'google.com/images'})
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["nome_produto"] == "Arroz"

def test_seleciona_produto(client):
    response = client.get("/produto/39")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["nome_produto"] == "Arroz"

def test_atualiza_produto(client):
    response = client.put("/produto/39", json={"nome_produto": "Feijão"})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["nome_produto"] == "Feijão"

def test_deleta_produto(client):
    response = client.delete("/produto/39")
    assert response.status_code == 204
