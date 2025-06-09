import sqlite3


conexao = sqlite3.connect("Trello.db")
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