import pickle

class p_wrapper:
    def __init__(self):
        self.db_file = None

    def load(self):
        while True:
            try:
                with open(self.db_file, 'rb') as f:
                    return pickle.load(f)
            except FileNotFoundError:
                with open(self.db_file, 'wb') as f:
                    pickle.dump([], f)


    def insert(self,insertable):
        db = self.load()
        
        if isinstance(insertable, dict):
            if len(db) > 0:
                insertable.update({'id': db[-1]['id'] + 1})
            else:
                insertable.update({'id': 0})

            db.append(insertable)
            with open(self.db_file, 'wb') as f:
                pickle.dump(db, f)
                
        if isinstance(insertable, list):
            for i in insertable:
                if len(db) > 0:
                    i.update({'id': db[-1]['id'] + 1})
                else:
                    i.update({'id': 0})
                db.append(i)
            with open(self.db_file, 'wb') as f:
                pickle.dump(db, f)
    
    def redump_db(self, full_db):
         with open(self.db_file, 'wb') as f:
                pickle.dump(full_db, f)

    def query_one(self,query:dict): #query = {'test': 2}
        db_ = self.load()

        for k, v in query.items():
            for item in db_:
                if item.get(k) == v:
                    return item
        
        return None
    
    def query_many(self, query:dict): #query = {'test': 2}
        db_ = self.load()

        ret = []

        for k, v in query.items():
            for item in db_:
                if item.get(k) == v:
                    ret.append(item)
        
        return ret

    def delete_all(self, query:dict):
        db_ = self.load()
        new_db = []
        for k, v in query.items():
            for item in db_:
                if item.get(k) != v:
                    new_db.append(item)
        self.redump_db(new_db)
        