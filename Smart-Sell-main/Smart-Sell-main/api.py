from flask import Flask, request, jsonify
from flask_cors import CORS

from modules.dados import (
    carregar_estoque,
    salvar_estoque,
    carregar_vendas,
    salvar_vendas
)

app = Flask(__name__)
CORS(app)


@app.route('/estoque', methods=['GET'])
def obter_estoque():
    estoque = carregar_estoque()
    return jsonify(estoque)


@app.route('/estoque', methods=['POST'])
def salvar_estoque_api():
    dados = request.json
    salvar_estoque(dados)
    return jsonify({'ok': True})


@app.route('/vendas', methods=['GET'])
def obter_vendas():
    vendas = carregar_vendas()
    return jsonify(vendas)


@app.route('/vendas', methods=['POST'])
def salvar_vendas_api():
    dados = request.json
    salvar_vendas(dados)
    return jsonify({'ok': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)