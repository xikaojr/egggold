# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

"""
IMPORTAÇÃO DE MODULOS
"""
from storage import Storage
modelStorage = Storage()
import entity

"""
DEFININDO CONFIGURAÇÕES DO APP
from replit import db
"""
app = Flask(__name__)
app.config['SECRET_KEY'] = 'egggold'
cors = CORS(
    resources={"/api/v1/*": {
        "origins": "*"
    }})

"""
CRIANDO ROTAS DA APLICAÇÃO
"""
@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def api():
    keys = dict(entity.get())
    return jsonify(keys)

@app.route('/collect', methods=['GET'])
@cross_origin()
def getAll():
    data = modelStorage.get()
    return jsonify(data)

@app.route('/collect', methods=['POST'])
@cross_origin()
def insert():
    data = request.get_json()
    modelStorage.create(data)
    return jsonify({"status":True, "message":"Coleta adiconada com sucesso"})

@app.route('/collect/<id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    result =  modelStorage.remove(id)
    return jsonify(result)

@app.route('/collect/<id>', methods=['GET'])
@cross_origin()
def getOne(id):
    data = dict(modelStorage.get(id))
    return jsonify(data)

@app.route('/collect', methods=['PUT'])
@cross_origin()
def updates():
    data = request.get_json()
    modelStorage.update(data)
    return jsonify({"status":True, "message":"Coleta atualizada com sucesso"})

"""
INICIADO APLICAÇÃO
"""
#if __name__ == '__main__':
app.run(host='0.0.0.0', port=8000, debug=True, use_reloader=True)