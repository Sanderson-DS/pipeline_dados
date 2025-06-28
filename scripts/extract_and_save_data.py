from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests

# Criando as funções:

# 1 - connect_mongo(uri): estabelece a conexão com a instância do MongoDB usando a URI fornecida. Ela retorna o cliente do MongoDB que permite interagir com o banco de dados.

def connect_mongo(uri):
    client = MongoClient(uri, server_api=ServerApi('1'))
    
    # Send a ping to confirm a successfull connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client

# 2 - create_connect_db(client, db_name): utiliza o(a) cliente do MongoDB para criar (se não existir) e conectar-se ao banco de dados especificado pelo parâmetro db_name. Ela retorna o objeto de banco de dados que pode ser usado para interagir com as coleções dentro dele.

def create_connect_db(client, db_name):
    db = client[db_name]
    return db

# 3 - create_connect_collection(db, col_name): cria (se não existir) e conecta-se à coleção especificada pelo parâmetro col_name dentro do banco de dados fornecido. Ela retorna o objeto de coleção que pode ser usado para interagir com os documentos dentro dela.

def create_connect_collection(db, col_name):
    collection = db[col_name]
    return collection

def extract_api_data(url):
    return requests.get(url).json()

def insert_data(col, data):
    docs = col.insert_many(data)
    n_docs_inseridos = len(docs.inserted_ids)
    return n_docs_inseridos


if __name__=="__main__":

    client = connect_mongo("mongodb+srv://sanderbgm:Spinf7896**@cluster0.egrwngz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = create_connect_db(client, "db_produtos")
    col = create_connect_collection(db, "produtos")

    data = extract_api_data("https://labdados.com/produtos")
    print(f"\n Quantidade de dados extraidos: {len(data)}")

    n_docs = insert_data(col, data)
    print(f"\n Quantidade de documentos inseridos: {n_docs}")

    client.close()
    