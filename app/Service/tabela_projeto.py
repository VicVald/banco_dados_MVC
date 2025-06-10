import sqlite3
from app.Service.database import get_db_path

conexao = sqlite3.connect(get_db_path())

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS project (
        id_project INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        desc TEXT NOT NULL,
        status TEXT,
        start_date TEXT,
        end_date TEXT
    )
    ''')

cursor.close()
print("Tabela project criada com sucesso!")