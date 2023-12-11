import pytest
from app import app, db, restaurantes

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://doadmin:AVNS_erI8p2wSSm0gckO83UU@banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com:25060/bd_for_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.test_client() as client:
        yield client

def test_cria_restaurante(client):
    response = client.post("/restaurante", json={"nome_restaurante": "Burger Donalds", 'distancia_totem':10.5, 'url_logo':'google.com/images', 'login':'bkmc@test', 'senha':'123'})
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["nome_restaurante"] == "Burger Donalds"

def test_seleciona_restaurante(client):
    response = client.get("/restaurante/15")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["nome_restaurante"] == "Burger Donalds"

def test_atualizar_restaurante(client):
    response = client.put("/restaurante/15", json={"nome_restaurante": "McKing"})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["nome_restaurante"] == "McKing"

def test_excluir_restaurante(client):
    response = client.delete("/restaurante/15")
    assert response.status_code == 204

def test_login_certo_restaurante(client):
    response = client.post('/login_restaurante', json={'login':'bkmc@test', 'senha':'123'})
    assert response.status_code == 200

def test_login_errado_restaurante(client):
    response = client.post('/login_restaurante', json={'login':'fulano@gmail', 'senha':'1234'})
    assert response.status_code == 401