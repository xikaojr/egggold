from pymongo import MongoClient
from bson.objectid import ObjectId
import sys

class Model:
    client = None
    db = None
    filter = None
    fields = None
    document = {}
    error = None
    url = "mongodb+srv://pedreiros:p3dr31r0s@cluster0.moktw.mongodb.net/pedreiros"

    def __init__(self):
        self.client = MongoClient(self.url)
        self.db = self.client['pedreiros']

    def one(self, collection, id=None):
        if id:
            result = self.db[collection].find_one({"_id": ObjectId(id)}, self.fields)
        if result:
            result["_id"] = str(result["_id"])
            return dict(result)
        else:
            return None

    def all(self, collection):
        result = list(self.db[collection].find(self.filter, self.fields))
        for i in range(len(result)):
            result[i]["_id"] = str(result[i]["_id"])
        return result

    def save(self, collection):
        if '_id' in self.document:
            id = ObjectId(self.document.get('_id'))
            self.document.pop('_id')
            self.db[collection].update_many({"_id": id},{"$set": self.document})
        else:
           self.db[collection].insert_many(self.document)

    def delete(self, collection, value):
        try:
            exists = self.one(collection, value)
            if exists:
                self.db[collection].delete_many({"_id": ObjectId(value)})
                return {'status': True, 'message': 'Registro removido com sucesso!'}
            else:
                return {'status': False, 'message': 'O id informado não foi encontrado!'}
        except Exception as error:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            return {'status': False, "message": str(error), "Exception_type": str(exception_type), "File_name": str(filename), "Line_number": str(line_number)}