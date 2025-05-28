import sqlite3

conexao = sqlite3.connect("Trello.db")

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS part (
        id_part INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user INTEGER,
        id_project INTEGER,
        funcao TEXT NOT NULL,
        data_inicio TIMESTAMP,
        FOREIGN KEY (id_user) REFERENCES user (id_user),
        FOREIGN KEY (id_project) REFERENCES project (id_project)
    )
''')

cursor.close()
print("Tabela participante criada com sucesso!")