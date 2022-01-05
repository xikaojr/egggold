from flask import request, jsonify
from storage import Storage
modelStorage = Storage()

class Collect: 

  def getAll(self):
    data = modelStorage.get()
    print(data)
    return jsonify(data)

  def insert(self):
    data = request.get_json()
    modelStorage.create(data)
    return jsonify({"status":True, "message":"Coleta adiconada com sucesso"})

  def delete(self,id):
    modelStorage.remove(id)
    return jsonify({"status": True, "message":"Coleta deletada"})

  def getOne(self,id):
    data = dict(modelStorage.get(id))
    return jsonify(data)