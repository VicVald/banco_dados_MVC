import sqlite3
from app.Service.database import get_db_path

conexao = sqlite3.connect(get_db_path())

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
        FOREIGN KEY (id_part) REFERENCES part (id_part) ON DELETE CASCADE,
        FOREIGN KEY (id_project) REFERENCES project (id_project) ON DELETE CASCADE
)
    '''
)

cursor.close()
print("Tabela task criada com sucesso!")