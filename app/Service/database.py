import os
import sqlite3

def get_db_path():
    # Caminho absoluto para o banco de dados na raiz do projeto
    return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'Trello.db')

def get_connection():
    return sqlite3.connect(get_db_path())

server = ''
username = ''
password = ''
database = 'Trello.db'
conexao = sqlite3.connect(database)
print("Banco de dados Trello criado com sucesso!")