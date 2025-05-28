import sqlite3

server = ''
username = ''
password = ''
database = 'Trello.db'
conexao = sqlite3.connect(database)
print("Banco de dados Trello criado com sucesso!")