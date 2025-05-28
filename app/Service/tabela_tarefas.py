import sqlite3

conexao = sqlite3.connect("Trello.db")

cursor = conexao.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS task (
        id_task INTEGER PRIMARY KEY AUTOINCREMENT,
        id_part INTEGER,
        id_project INTEGER,
        name TEXT NOT NULL,
        desc TEXT NOT NULL,
        state TEXT NOT NULL,
        FOREIGN KEY (id_part) REFERENCES part (id_part),
        FOREIGN KEY (id_project) REFERENCES project (id_project)
)
    '''
)

cursor.close()
print("Tabela task criada com sucesso!")