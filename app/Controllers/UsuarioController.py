import sqlite3
from Models.Usuario import User

def conectBD():
    conexao = sqlite3.connect("Trello.db")
    return conexao

def includeUser(user):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO user (name, email)
            VALUES (?, ?)
        """, (
            user.name,
            user.email
        ))
        conexao.commit()
        user.id_user = cursor.lastrowid
        return user
    except sqlite3.Error as e:
        print(f"Erro ao inserir usuário: {e}")

def getUsers():
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM user')
        rows = cursor.fetchall()
        users = []
        for row in rows:
            users.append(User(
                name=row[1],
                email=row[2],
                id_user=row[0]
            ))
        return users
    except sqlite3.Error as e:
        print(f"Erro ao consultar usuários: {e}")

def updateUser(user):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE user
            SET name = ?, email = ?
            WHERE id_user = ?
        """, (
            user.name,
            user.email,
            user.id_user
        ))
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar usuário: {e}")

def getUserById(id_user):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM user WHERE id_user = ?', (id_user,))
        row = cursor.fetchone()
        if row:
            return User(
                name=row[1],
                email=row[2],
                id_user=row[0]
            )
        return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar usuário: {e}")

def getUserByEmail(email):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM user WHERE email = ?', (email,))
        row = cursor.fetchone()
        if row:
            return User(
                name=row[1],
                email=row[2],
                id_user=row[0]
            )
        return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar usuário por email: {e}")

def deleteUser(id_user):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('DELETE FROM user WHERE id_user = ?', (id_user,))
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao deletar usuário: {e}")

def searchUsersByName(name):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM user WHERE name LIKE ?', (f'%{name}%',))
        rows = cursor.fetchall()
        users = []
        for row in rows:
            users.append(User(
                name=row[1],
                email=row[2],
                id_user=row[0]
            ))
        return users
    except sqlite3.Error as e:
        print(f"Erro ao buscar usuários por nome: {e}")

if __name__ == "__main__":
    # Teste de inclusão
    print("\nTeste de inclusão de usuário:")
    novo_usuario = User("Teste Usuario", "teste@email.com")
    usuario_inserido = includeUser(novo_usuario)
    print(f"Usuário inserido: {usuario_inserido.name} - {usuario_inserido.email}")

    # Teste de busca por ID
    print("\nTeste de busca por ID:")
    usuario = getUserById(usuario_inserido.id_user)
    print(f"Usuário encontrado: {usuario.name} - {usuario.email}")

    # Teste de atualização
    print("\nTeste de atualização:")
    usuario.name = "Teste Usuario Atualizado"
    updateUser(usuario)
    usuario_atualizado = getUserById(usuario.id_user)
    print(f"Usuário atualizado: {usuario_atualizado.name} - {usuario_atualizado.email}")

    # Teste de busca por nome
    print("\nTeste de busca por nome:")
    usuarios = searchUsersByName("Teste")
    for u in usuarios:
        print(f"Usuário encontrado: {u.name} - {u.email}")

    # Teste de deleção
    print("\nTeste de deleção:")
    deleteUser(usuario.id_user)
    usuario_deletado = getUserById(usuario.id_user)
    print(f"Usuário deletado: {'Sim' if usuario_deletado is None else 'Não'}")
