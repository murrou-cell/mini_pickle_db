from pickle_wrapper import p_wrapper
import os 

db = p_wrapper()

db_file_path = 'db'

db_file_name = 'simple_db.db'

db.db_file = os.path.join(db_file_path, db_file_name)

single_doc = {
    'test_1': 1,
    'test_2': 2
}

db.insert(single_doc)

print(db.load())

multiple_docs = [
    {
        'test_1': 1,
        'test_2': 2
    },
    {
        'test_3': 3,
        'test_4': 4
    }
]
db.insert(multiple_docs)

print(db.load())

print(db.query_one({'test_2': 2}))

print(db.query_many({'test_2': 2}))