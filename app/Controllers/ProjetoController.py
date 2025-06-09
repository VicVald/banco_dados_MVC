import sqlite3
from Models.Projeto import Project

def conectBD():
    conexao = sqlite3.connect("Trello.db")
    return conexao

def includeProject(project):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO project (name, desc, status, start_date, end_date, owner_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            project.name,
            project.desc,
            project.status,
            project.start_date,
            project.end_date,
            project.owner_id
        ))
        conexao.commit()
        project.id_project = cursor.lastrowid
        return project
    except sqlite3.Error as e:
        print(f"Erro ao inserir projeto: {e}")

def getProjects():
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM project')
        rows = cursor.fetchall()
        projects = []
        for row in rows:
            owner_id = row[6] if len(row) > 6 else None
            projects.append(Project(
                name=row[1],
                desc=row[2],
                status=row[3],
                start_date=row[4],
                end_date=row[5],
                id_project=row[0],
                owner_id=owner_id
            ))
        return projects
    except sqlite3.Error as e:
        print(f"Erro ao consultar projetos: {e}")

def updateProject(project):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE project
            SET name = ?, desc = ?, status = ?, start_date = ?, end_date = ?
            WHERE id_project = ?
        """, (
            project.name,
            project.desc,
            project.status,
            project.start_date,
            project.end_date,
            project.id_project
        ))
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar projeto: {e}")

def getProjectById(id_project):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM project WHERE id_project = ?', (id_project,))
        row = cursor.fetchone()
        if row:
            return Project(
                name=row[1],
                desc=row[2],
                status=row[3],
                start_date=row[4],
                end_date=row[5],
                id_project=row[0]
            )
        return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar projeto: {e}")

def deleteProject(id_project):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('DELETE FROM project WHERE id_project = ?', (id_project,))
        conexao.commit()
        return True
    except sqlite3.Error as e:
        print(f"Erro ao deletar projeto: {e}")
        return False

if __name__ == "__main__":
    # Teste de inclusão
    print("\nTeste de inclusão de projeto:")
    novo_projeto = Project("Projeto Teste", "Descrição do projeto teste", "Em Andamento", "2024-01-01", "2024-12-31")
    projeto_inserido = includeProject(novo_projeto)
    print(f"Projeto inserido: {projeto_inserido.name} - {projeto_inserido.desc}")

    # Teste de busca por ID
    print("\nTeste de busca por ID:")
    projeto = getProjectById(projeto_inserido.id_project)
    print(f"Projeto encontrado: {projeto.name} - {projeto.desc}")

    # Teste de atualização
    print("\nTeste de atualização:")
    projeto.name = "Projeto Teste Atualizado"
    projeto.desc = "Nova descrição do projeto"
    projeto.status = "Concluído"
    projeto.start_date = "2024-01-01"
    projeto.end_date = "2024-12-31"
    updateProject(projeto)
    projeto_atualizado = getProjectById(projeto.id_project)
    print(f"Projeto atualizado: {projeto_atualizado.name} - {projeto_atualizado.desc}")

    # Teste de listagem
    print("\nTeste de listagem de projetos:")
    projetos = getProjects()
    for p in projetos:
        print(f"Projeto: {p.name} - {p.desc}")

    # Teste de deleção
    print("\nTeste de deleção:")
    deleteProject(projeto.id_project)
    projeto_deletado = getProjectById(projeto.id_project)
    print(f"Projeto deletado: {'Sim' if projeto_deletado is None else 'Não'}") 