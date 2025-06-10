import sqlite3
from app.Service.database import get_db_path


conexao = sqlite3.connect(get_db_path())
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT
    )
""")

conexao.commit()
conexao.close()

if __name__ == "__main__":
    print("Tabela 'user' criada com sucesso!")