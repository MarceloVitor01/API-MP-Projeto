# Projeto de API com Flask e SQLAlchemy

Este projeto consiste em uma API desenvolvida utilizando Flask e SQLAlchemy para gerenciar usuários, produtos, restaurantes e pesquisas relacionadas a estes elementos.

## Configuração do Ambiente

1. **Instalação de dependências**
   Certifique-se de ter Python e Flask instalados. Para instalar as dependências, utilize o `requirements.txt`.

Se estiver no Windows, digite 'pip install -r requirements.txt' sem as aspas.
Se estiver no Linux, digite 'pip3 install -r requirements.txt' sem as aspas.

2. **Configuração do Banco de Dados**
O banco de dados utilizado é MySQL. Certifique-se de ter um banco de dados MySQL configurado e altere a variável de ambiente `SQLALCHEMY_DATABASE_URI` no arquivo `app.py` para sua própria configuração do banco de dados.

## Estrutura do Código

- `app.py`: Contém a lógica principal da API usando Flask.
- `models.py`: Define as classes de modelo para o SQLAlchemy.
- `templates`: Pasta que pode conter os arquivos HTML para renderizar em caso de erro.

## Uso da API

### Usuários

- `POST /login`: Autenticação de usuário.
- `GET /usuario`: Retorna todos os usuários.
- `GET /usuario/<id_usuario>`: Retorna um usuário específico.
- `POST /usuario`: Cria um novo usuário.
- `PUT /usuario/<id_usuario>`: Atualiza um usuário existente.
- `DELETE /usuario/<id_usuario>`: Deleta um usuário existente.

### Produtos

- `GET /produto`: Retorna todos os produtos.
- `GET /produto/<id_produto>`: Retorna um produto específico.
- `POST /produto`: Cria um novo produto.
- `PUT /produto/<id_produto>`: Atualiza um produto existente.
- `DELETE /produto/<id_produto>`: Deleta um produto existente.

### Restaurantes

- `POST /login_restaurante`: Autenticação de restaurante.
- `GET /restaurante`: Retorna todos os restaurantes.
- `GET /restaurante/<id_restaurante>`: Retorna um restaurante específico.
- `POST /restaurante`: Cria um novo restaurante.
- `PUT /restaurante/<id_restaurante>`: Atualiza um restaurante existente.
- `DELETE /restaurante/<id_restaurante>`: Deleta um restaurante existente.

### Pesquisas

- `GET /pesquisa_produto`: Retorna todas as pesquisas por produto.
- `GET /pesquisa_produto/<id_pesquisa_produto>`: Retorna uma pesquisa por produto específica.
- `POST /pesquisa_produto`: Cria uma nova pesquisa por produto.
- `DELETE /pesquisa_produto/<id_pesquisa_produto>`: Deleta uma pesquisa por produto existente.
- `GET /pesquisa_restaurante`: Retorna todas as pesquisas por restaurante.
- `GET /pesquisa_restaurante/<id_pesquisa_restaurante>`: Retorna uma pesquisa por restaurante específica.
- `POST /pesquisa_restaurante`: Cria uma nova pesquisa por restaurante.
- `DELETE /pesquisa_restaurante/<id_pesquisa_restaurante>`: Deleta uma pesquisa por restaurante existente.

### Outras Funcionalidades

- `GET /pesquisar_prato/<nome_produto>`: Pesquisa pratos pelo nome.
- `GET /filtrar_maior_distancia`: Filtra restaurantes por maior distância.
- `GET /filtrar_menor_distancia`: Filtra restaurantes por menor distância.
- `GET /filtrar_menor_preco`: Filtra produtos por menor preço.
- `GET /filtrar_maior_preco`: Filtra produtos por maior preço.

## Executando a Aplicação

Para iniciar o servidor Flask:

