import sqlite3

conexao = sqlite3.connect("Trello.db")

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS project (
        id_project INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        desc TEXT NOT NULL
    )
    ''')

cursor.close()
print("Tabela project criada com sucesso!")