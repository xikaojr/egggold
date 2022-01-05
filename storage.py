from database import Model

class Storage:

  db = Model()
  collection = "collects"

  def get(self, id=None):
    if id is None:
      return self.db.all(self.collection)
    else:
      return self.db.one(self.collection, id)

  def create(self, document):
    self.db.document = [document]
    self.db.save(self.collection)
  
  def update(self, document):
    self.db.document = document
    self.db.save(self.collection)

  def remove(self, id):
    return self.db.delete(self.collection, id)