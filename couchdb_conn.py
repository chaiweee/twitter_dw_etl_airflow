import couchdb
import auth

class CouchHandle:
    def __init__(self):
        url=f'http://{auth.creds["COUCH_USER"]}:{auth.creds["COUCH_PASSWORD"]}@127.0.0.1:5984'
        self.couch = couchdb.Server(url)

    def check_database_exists(self, db_name):
        return db_name in self.couch


    def deleteDB(self, db_name):
        if self.check_database_exists(db_name):
            self.couch.delete(db_name)
            print(f"Database '{db_name}' deleted.")
        else:
            print(f"Database '{db_name}' does not exist.")


    def createDB(self, db_name):
        if not self.check_database_exists(db_name):
            self.couch.create(db_name)
            print(f"Database '{db_name}' created.")
        else:
            print(f"Database '{db_name}' already exists.")

    def get_database(self, db_name):
        if self.check_database_exists(db_name):
            return self.couch[db_name]
        else:
            raise Exception(f"Database '{db_name}' does not exist.")

    
    def insertDoc(self, db_name, doc):
        db = self.get_database(db_name)
        db.save(doc)

    def deleteDoc(self, db_name, doc_id):
        db = self.get_database(db_name)
        doc = db[doc_id]
        db.delete(doc)
        print(f"Document '{doc_id}' deleted from '{db_name}' database.")
    