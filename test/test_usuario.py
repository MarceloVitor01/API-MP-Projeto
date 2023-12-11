import pytest
from app import app, db, usuarios

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://doadmin:AVNS_erI8p2wSSm0gckO83UU@banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com:25060/bd_for_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.test_client() as client:
        yield client

def test_get_usuarios(client):
    response = client.get('/usuario')
    assert response.status_code == 200

def test_cria_usuario(client):
    response = client.post('/usuario', json = {"nome_usuario": "Fulano", 'funcao':'Pessoa Fisica', 'login':'fulano1@gmail', 'senha':'123'})
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['nome_usuario'] == 'Fulano'
    assert json_data['senha'] == 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'

def test_deleta_usuario(client):
    response = client.delete('/usuario/18')
    assert response.status_code == 200

def test_seleciona_usuario(client):
    response = client.get('/usuario/1')
    assert response.status_code == 200