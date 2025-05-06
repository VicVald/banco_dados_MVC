import sqlite3
from Models.Usuario import User

def conectBD():
    conexao = sqlite3.connect("Empresa.db")
    return conexao

def includeUser(user):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
                    INSERT INTO funcionario (id_user, name, email)
                    VALUES (?, ?, ?)
                """, (
                    user.get_id_user(),
                    user.get_name(),
                    user.get_email(),
                )) 
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao inserir usuário: {e}")

def getUsers(user):
    conexao = conectBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM funcionario')
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Erro ao consultar usuário: {e}")

def updateUser(user):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
                    UPDATE funcionario
                    SET id_user = ?, name = ?, email = ?)
                    WHERE id_user = ?
                """, (
                    user.get_id_user(),
                    user.get_name(),
                    user.get_email(),
                    user.get_id_user()
                )) 
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao inserir usuário: {e}")
