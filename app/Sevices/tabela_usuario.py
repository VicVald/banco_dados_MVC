import sqlite3

conexao = sqlite3.connect("Trello.db")

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE user (
            id_user INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
);
    '''
)

cursor.close()
print("Tabela user criada com sucesso!")