import sqlite3

conexao = sqlite3.connect("Trello.db")

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE task (
            id_task INTEGER PRIMARY KEY,
            id_member INTEGER,
            id_project INTEGER,
            name TEXT NOT NULL,
            desc TEXT NOT NULL,
            state TEXT NOT NULL,
            FOREIGN KEY (id_member) REFERENCES member (id_member),
            FOREIGN KEY (id_project) REFERENCES project (id_project)
);
    '''
)

cursor.close()
print("Tabela task criada com sucesso!")