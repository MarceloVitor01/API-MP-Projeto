from flask import Flask, jsonify, request
from Conexao import ConexaoBD
from Usuario import Usuario, UsuarioDAO

conn = ConexaoBD.conecta_bd()

app = Flask(__name__)

usuario_dao = UsuarioDAO(conn)

@app.route('/usuarios', methods=['GET'])
def criar_usuario():
    dados = request.get_json()
    id_usuario = dados.get('id_usuario')
    nome = dados.get('nome')
    funcao = dados.get('funcao')
    login = dados.get('login')
    senha = dados.get('senha')

    if id_usuario and nome and funcao and login and senha:
        usuario = Usuario(id_usuario, nome, funcao, login, senha)

        usuario_dao.criar_usuario(usuario)

        return jsonify({'mensagem': f'Usuário com ID:{id_usuario} cadastrado com sucesso!'}), 201

    else:
        return jsonify({'erro': 'Dados incompletos para criar o usuário'}), 400
    
if __name__ == '__main__':
    app.run(debug=True)