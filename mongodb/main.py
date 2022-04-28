from pymongo import MongoClient

user = 'root'
password = 'root'


class MongoConection:

    # Connection method
    def __init__(self):
        client = MongoClient(
                f'mongodb://{user}:{password}@localhost:27017')

        self._db = client['blockchain']


    def send_data(self, collection_name, data):
        try:
            node_collection = self._db[collection_name]

            # Data object
            node_collection.insert_one(data)

        except Exception as e:
            print("Error {}".format(e))
            raise e

    def query(self):

            result = self._db.node_collection.find()

            for n in result:
                print(n)

