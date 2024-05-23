import couchdb
import auth

class CouchHandle:
    def __init__(self):
        url=f'http://{auth.creds["COUCH_USER"]}:{auth.creds["COUCH_PASSWORD"]}@127.0.0.1:5984'
        self.couch = couchdb.Server(url)
        
        db_name = 'twitter_data_staging'
        if db_name not in self.couch:
            self.db = self.couch.create(db_name)
        else:
            self.db = self.couch[db_name]
    
    def insert(self, doc):
        self.db.save(doc)

    def delete(self, doc):
        self.db.delete(doc)
    
    def deleteDB(self):
        self.couch.delete("staging")