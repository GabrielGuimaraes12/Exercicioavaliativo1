import pymongo # pip install pymongo


class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connection_string = "mongodb+srv://guimatw2012:P7DKXDtszxR9Tnwf@atividadeavaliativa1.bsdoguz.mongodb.net/test"
            self.clusterConnection = pymongo.MongoClient(
                connection_string,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try:
            self.db.drop_collection(self.collection)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)