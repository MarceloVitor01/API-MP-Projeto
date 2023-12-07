import pytest
from app import app, db, usuarios, produtos, restaurantes, pesquisas_produto, pesquisas_restaurante

# Configurar o aplicativo para testes
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://doadmin:AVNS_erI8p2wSSm0gckO83UU@banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com:25060/teste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
client = app.test_client()

# Função para configurar o banco de dados
@pytest.fixture
def setup_database():
    db.create_all()

    # Adicionar dados de exemplo
    usuario_exemplo = usuarios(nome_usuario='Usuario Teste', funcao='Cliente', login='teste@teste@gmail.com', senha='123')
    db.session.add(usuario_exemplo)
    db.session.commit()

    yield db  # Fornecer o banco de dados para os testes

    db.drop_all()

def test_seleciona_usuarios(setup_database):
    response = client.get('/usuarios')
    assert response.status_code == 200

def test_cria_usuario(setup_database):
    novo_usuario = {'nome_usuario': 'Novo Usuario', 'funcao': 'Testador', 'login': 'novo_testador', 'senha': 'senha456'}
    response = client.post('/usuarios', json=novo_usuario)
    assert response.status_code == 200

def test_seleciona_produto(setup_database):
    novo_produto = {'nome_produto': 'Produto Teste', 'fk_id_restaurante': 1, 'preco': 10.99, 'descricao': 'Descrição do produto'}
    response = client.post('/produtos', json=novo_produto)

    response = client.get('/produto/1')
    assert response.status_code == 200

def test_cria_pesquisa_produto(setup_database):
    nova_pesquisa_produto = {'fk_id_usuario': 1, 'fk_id_produto': 1}
    response = client.post('/pesquisas_produto', json=nova_pesquisa_produto)
    assert response.status_code == 200