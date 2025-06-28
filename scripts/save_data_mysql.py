
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
from mysql.connector import ProgrammingError
from mysql.connector import InterfaceError

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

# 1 - connect_mysql(host_name, user_name, pw): estabelece a conexão com o servidor MySQL, utilizando os dados do host, usuário e senha. 
# A função deve retornar a conexão estabelecida.

def connect_mysql(host_name, user_name, pw):
    try:
        cnx =  mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        if cnx.is_connected():
            print("✅ Conexão estabelecida com sucesso!")
            # opcional: exibe versão do MySQL
            info = cnx.server_info
            print(f"Versão do servidor MySQL: {info}")


    except ProgrammingError as pe:
        print("❌ Erro de autenticação ou comando inválido:")
        print(pe)

    except InterfaceError as ie:
        print("❌ Erro de conexão (interface):")
        print(ie)

    except Error as e:
        print("❌ Outro erro com MySQL:")
        print(e)

    except Exception as ex:
        print("⚠️ Erro inesperado:")
        print(ex)

    return cnx

# 2 - create_cursor(cnx): cria e retorna um cursor, que serve para conseguirmos executar os comandos SQL, utilizando a conexão fornecida como argumento.

def create_cursor(cnx):
    try:
        cursor = cnx.cursor()
        print("✅ Cursor criado com sucesso!")
        return cursor
    except Error as e:
        print("❌ Erro ao criar o cursor:")
        print(e)
        return None
    
#  - create_database(cursor, db_name): cria um banco de dados com o nome fornecido como argumento. Para isso, a função deverá usar o cursor para executar o comando SQL de criação do banco de dados.

def create_database(cursor, db_name):
    try:
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name};')
        print(f"✅ Banco de dados '{db_name}' criado com sucesso!")
    except Error as e:
        print(f"❌ Erro ao criar o banco de dados '{db_name}':")
        print(e)    

# 4 - show_databases(cursor): exibe todos os bancos de dados existentes. Para isso, a função deve utilizar o cursor para executar o comando SQL que lista todos os bancos de dados existentes.

def show_databases(cursor):
    try:
        cursor.execute("SHOW DATABASES;")
        databases = cursor.fetchall()
        print("✅ Bancos de dados existentes:")
        for db in databases:
            print(f"- {db[0]}")
    except Error as e:
        print("❌ Erro ao listar os bancos de dados:")
        print(e)

# 5 - create_product_table(cursor, db_name, tb_name): cria uma tabela com o nome fornecido no banco de dados especificado. A tabela deve ter as colunas que correspondam aos dados que serão inseridos posteriormente.

def create_product_table(cursor, db_name, tb_name):
    try:
        cursor.execute(f"USE {db_name};")
        cursor.execute(f"""
            create table if not exists {db_name}.{tb_name}(
                    id VARCHAR(100),
                    Produto VARCHAR(100),
                    Categoria_Produto VARCHAR(100),
                    Preço FLOAT(10,2),
                    Frete FLOAT(10,2),
                    Data_Compra DATE,
                    Vendedor VARCHAR(100),
                    Local_compra VARCHAR(100),
                    Avaliação_compra INT,
                    Tipo_pagamento VARCHAR(100),
                    Qntd_parcelas INT,
                    latitude FLOAT(10,2),
                    longitude FLOAT(10,2),  

                    primary key (id) 
            );
        """)
        print(f"✅ Tabela '{tb_name}' criada com sucesso no banco de dados '{db_name}'!")
    except Error as e:
        print(f"❌ Erro ao criar a tabela '{tb_name}' no banco de dados '{db_name}':")
        print(e)


# 6 - show_tables(cursor, db_name): lista todas as tabelas existentes no banco de dados especificado. Para isso, a função deve utilizar o cursor para executar o comando SQL que lista todas as tabelas no banco de dados.

def show_tables(cursor, db_name):
    try:
        cursor.execute(f"USE {db_name};")
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print(f"✅ Tabelas no banco de dados '{db_name}':")
        for table in tables:
            print(f"- {table[0]}")
    except Error as e:
        print(f"❌ Erro ao listar as tabelas no banco de dados '{db_name}':")
        print(e)

# 7 - read_csv(path): lê um arquivo csv do caminho fornecido e retorna um DataFrame do pandas com esses dados.

def read_csv(path):
    try:
        import pandas as pd
        df = pd.read_csv(path)
        print(f"✅ Arquivo '{path}' lido com sucesso!")
        return df
    except FileNotFoundError as fnf_error:
        print(f"❌ Erro: arquivo não encontrado - {fnf_error}")
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo '{path}':")
        print(e)
        return None

    
# 8 - add_product_data(cnx, cursor, df, db_name, tb_name): insere os dados do DataFrame fornecido à tabela especificada no banco de dados especificado. 
# A função deve usar o cursor para executar o comando SQL de inserção de dados.

def add_product_data(cnx, cursor, df, db_name, tb_name):
    try:
       cursor.execute(f"truncate table {tb_name};")
       lista_dados = [tuple(row) for i, row in df.iterrows()]
       sql = f'insert into {db_name}.{tb_name} values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
       cursor.executemany(sql, lista_dados)
       cnx.commit()
       print(f"✅ Dados inseridos com sucesso na tabela '{tb_name}' do banco de dados '{db_name}'!")
    except Error as e:
        print(f"❌ Erro ao inserir dados na tabela '{tb_name}' do banco de dados '{db_name}':")
        print(e)    

if __name__ == "__main__":

    #conectar ao servidor MySQL;
    cnx = connect_mysql(host, user, password)

    # criar um cursor;
    cursor = create_cursor(cnx)

    # criar um banco de dados chamado "db_produtos_teste";
    create_database(cursor, "database_produtos")


    # exibir todos os bancos de dados existentes;
    show_databases(cursor)

    # criar uma tabela chamada "tb_livros" no banco de dados criado;
    create_product_table(cursor, "database_produtos", "tb_livros")

    # exibir todas as tabelas no banco de dados criado;
    show_tables(cursor, "database_produtos")

    # ler os dados do arquivo csv "tb_livros.csv";
    df = read_csv("../data/tabela_livros.csv")

    # adicionar os dados lidos à tabela criada.
    add_product_data(cnx, cursor, df,  "database_produtos" , "tb_livros")