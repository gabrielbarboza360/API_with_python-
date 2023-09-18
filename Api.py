from flask import Flask, app,jsonify,request

API = Flask(__name__)


clientes = [
    {
        'id': 1,
        'name': 'Nicolas',
        'banco': 'Santander',
        'frase': '',
    },
    {
        'id': 2,
        'name': 'Leandro',
        'banco': 'Santander',
        'frase': '',
    },
    {
        'id': 3,
        'name': 'Fernando',
        'banco': 'Bradesco',
        'frase': '',
    },
    {
        'id': 4,
        'name': 'Renata',
        'banco': 'C6 Bank',
        'frase': '',
    },
]

# Consultar(todos clientes)
@API.route('/lista',methods=['GET'])
def todos_clientes():
    return jsonify(clientes)



# filtrar por id
@API.route('/lista/<int:id>', methods=['GET'])
def consulta_cliente(id):
    for cliente in clientes:
        if cliente.get('id') == id:
            return jsonify(cliente)

            

# Editar 
@API.route('/lista/<int:id>',methods=['PUT'])
def editar_cliente(id):
    cliente_alterado = request.get_json()
    for indice,cliente in enumerate(clientes):
        if cliente.get('id') == id:
            clientes[indice].update(cliente_alterado)
            return jsonify(clientes[indice])

  
  # Criar
@API.route('/listanovo',methods=['POST'])
def incluir_novo_cliente():
    novo_cliente = request.get_json()
    clientes.append(novo_cliente)
    return jsonify(clientes)



#atualizar a lista de frase
@API.route('/lista',methods=['PUT'])
def atualizar_lista():
    novo_cliente = request.get_json()
    clientes.append(novo_cliente)
    return jsonify(clientes)



# Excluir
@API.route('/lista/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, cliente in enumerate(clientes):
        if cliente.get('id') == id:
            del clientes[indice]

    return jsonify(clientes)

API.run(port=5000,host='localhost',debug=True)  

