import sqlite3
from app.Service.database import get_db_path

conexao = sqlite3.connect(get_db_path())

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS part (
        id_part INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user INTEGER,
        id_project INTEGER,
        funcao TEXT NOT NULL,
        data_inicio TIMESTAMP,
        FOREIGN KEY (id_user) REFERENCES user (id_user),
        FOREIGN KEY (id_project) REFERENCES project (id_project) ON DELETE CASCADE
    )
''')

cursor.close()
print("Tabela participante criada com sucesso!")