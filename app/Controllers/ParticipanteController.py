import sqlite3
from Models.Participante import Participante

def conectBD():
    conexao = sqlite3.connect("Trello.db")
    return conexao

def includeParticipante(participante):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        # Verificar se o participante já existe
        cursor.execute('SELECT * FROM part WHERE id_user = ? AND id_project = ?', 
                      (participante.id_user, participante.id_project))
        if cursor.fetchone():
            return None  # Participante já existe
        
        cursor.execute("""
            INSERT INTO part (id_user, id_project, funcao, data_inicio)
            VALUES (?, ?, ?, ?)
        """, (
            participante.id_user,
            participante.id_project,
            participante.funcao,
            participante.data_inicio
        ))
        conexao.commit()
        participante.id_part = cursor.lastrowid
        return participante
    except sqlite3.Error as e:
        print(f"Erro ao inserir participante: {e}")
        return None

def getParticipantes():
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM part')
        rows = cursor.fetchall()
        participantes = []
        for row in rows:
            participantes.append(Participante(
                id_user=row[1],
                id_project=row[2],
                funcao=row[3],
                inicio=row[4],
                id_part=row[0]
            ))
        return participantes
    except sqlite3.Error as e:
        print(f"Erro ao consultar participantes: {e}")

def updateParticipante(participante):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE part
            SET id_user = ?, id_project = ?, funcao = ?, data_inicio = ?
            WHERE id_part = ?
        """, (
            participante.id_user,
            participante.id_project,
            participante.funcao,
            participante.data_inicio,
            participante.id_part
        ))
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar participante: {e}")

def getParticipanteById(id_part):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM part WHERE id_part = ?', (id_part,))
        row = cursor.fetchone()
        if row:
            return Participante(
                id_user=row[1],
                id_project=row[2],
                funcao=row[3],
                inicio=row[4],
                id_part=row[0]
            )
        return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar participante: {e}")

def getParticipantesByProject(id_project):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM part WHERE id_project = ?', (id_project,))
        rows = cursor.fetchall()
        participantes = []
        for row in rows:
            participantes.append(Participante(
                id_user=row[1],
                id_project=row[2],
                funcao=row[3],
                inicio=row[4],
                id_part=row[0]
            ))
        return participantes
    except sqlite3.Error as e:
        print(f"Erro ao consultar participantes do projeto: {e}")

def getParticipantesByUser(id_user):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM part WHERE id_user = ?', (id_user,))
        rows = cursor.fetchall()
        participantes = []
        for row in rows:
            participantes.append(Participante(
                id_user=row[1],
                id_project=row[2],
                funcao=row[3],
                inicio=row[4],
                id_part=row[0]
            ))
        return participantes
    except sqlite3.Error as e:
        print(f"Erro ao consultar projetos do usuário: {e}")

def deleteParticipante(id_part):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('DELETE FROM part WHERE id_part = ?', (id_part,))
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao deletar participante: {e}") 