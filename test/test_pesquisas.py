import pytest
from app import app, db, produtos

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://doadmin:AVNS_erI8p2wSSm0gckO83UU@banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com:25060/bd_for_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize("nome_restaurante", ["La Parrilla Argentina - Carnes Premium", "Green Bowl - Refeições Saudáveis"])
def test_pesquisa_restaurante(app, nome_restaurante):
    response = client.get("/pesquisa_restaurante/{}".format(nome_restaurante))
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data[0]["nome_restaurante"] == nome_restaurante

@pytest.mark.parametrize("nome_produto", ["Tiramisu", "Quindim"])
def test_pesquisa_prato(app, nome_produto):
    response = client.get("/pesquisar_prato/{}".format(nome_produto))
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data[0]["nome_produto"] == nome_produto

def test_filtrar_menor_preco(client):
    response = client.get("/filtrar_menor_preco")
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) > 0
    for produto in json_data:
        assert produto["preco"] > 0

def test_filtrar_maior_preco(client):
    response = client.get("/filtrar_maior_preco")
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) > 0
    for produto in json_data:
        assert produto["preco"] > 0

def test_filtrar_maior_distancia(client):
    response = client.get("/filtrar_maior_distancia")
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) > 0
    for restaurante in json_data:
        assert restaurante["distancia_totem"] > 0

def test_filtrar_menor_distancia(client):
    response = client.get("/filtrar_menor_distancia")
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) > 0
    for restaurante in json_data:
        assert restaurante["distancia_totem"] > 0