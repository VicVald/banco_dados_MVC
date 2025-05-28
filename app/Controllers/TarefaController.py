import sqlite3
from Models.Tarefa import Task

def conectBD():
    conexao = sqlite3.connect("Trello.db")
    return conexao

def includeTask(task):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO task (id_part, id_project, name, desc, state)
            VALUES (?, ?, ?, ?, ?)
        """, (
            task.id_part,
            task.id_project,
            task.name,
            task.desc,
            task.state
        ))
        conexao.commit()
        task.id_task = cursor.lastrowid
        return task
    except sqlite3.Error as e:
        print(f"Erro ao inserir tarefa: {e}")

def getTasks():
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM task')
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append(Task(
                id_part=row[1],
                id_project=row[2],
                name=row[3],
                desc=row[4],
                state=row[5],
                id_task=row[0]
            ))
        return tasks
    except sqlite3.Error as e:
        print(f"Erro ao consultar tarefas: {e}")

def updateTask(task):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE task
            SET id_part = ?, id_project = ?, name = ?, desc = ?, state = ?
            WHERE id_task = ?
        """, (
            task.id_part,
            task.id_project,
            task.name,
            task.desc,
            task.state,
            task.id_task
        ))
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar tarefa: {e}")

def getTaskById(id_task):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM task WHERE id_task = ?', (id_task,))
        row = cursor.fetchone()
        if row:
            return Task(
                id_part=row[1],
                id_project=row[2],
                name=row[3],
                desc=row[4],
                state=row[5],
                id_task=row[0]
            )
        return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar tarefa: {e}")

def getTasksByProject(id_project):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM task WHERE id_project = ?', (id_project,))
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append(Task(
                id_part=row[1],
                id_project=row[2],
                name=row[3],
                desc=row[4],
                state=row[5],
                id_task=row[0]
            ))
        return tasks
    except sqlite3.Error as e:
        print(f"Erro ao consultar tarefas do projeto: {e}")

def getTasksByParticipant(id_part):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM task WHERE id_part = ?', (id_part,))
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append(Task(
                id_part=row[1],
                id_project=row[2],
                name=row[3],
                desc=row[4],
                state=row[5],
                id_task=row[0]
            ))
        return tasks
    except sqlite3.Error as e:
        print(f"Erro ao consultar tarefas do participante: {e}")

def deleteTask(id_task):
    conexao = conectBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('DELETE FROM task WHERE id_task = ?', (id_task,))
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao deletar tarefa: {e}")

if __name__ == "__main__":
    # Teste de inclusão
    print("\nTeste de inclusão de tarefa:")
    nova_tarefa = Task(
        id_part=1,
        id_project=1,
        name="Implementar Login",
        desc="Criar sistema de autenticação",
        state="To Do"
    )
    tarefa_inserida = includeTask(nova_tarefa)
    print(f"Tarefa inserida: ID={tarefa_inserida.id_task}, Nome={tarefa_inserida.name}, Estado={tarefa_inserida.state}")

    # Teste de busca por ID
    print("\nTeste de busca por ID:")
    tarefa = getTaskById(tarefa_inserida.id_task)
    print(f"Tarefa encontrada: ID={tarefa.id_task}, Nome={tarefa.name}, Estado={tarefa.state}")

    # Teste de atualização
    print("\nTeste de atualização:")
    tarefa.state = "In Progress"
    updateTask(tarefa)
    tarefa_atualizada = getTaskById(tarefa.id_task)
    print(f"Tarefa atualizada: ID={tarefa_atualizada.id_task}, Nome={tarefa_atualizada.name}, Estado={tarefa_atualizada.state}")

    # Teste de busca por projeto
    print("\nTeste de busca por projeto:")
    tarefas_projeto = getTasksByProject(1)
    for t in tarefas_projeto:
        print(f"Tarefa do projeto: ID={t.id_task}, Nome={t.name}, Estado={t.state}")

    # Teste de busca por participante
    print("\nTeste de busca por participante:")
    tarefas_participante = getTasksByParticipant(1)
    for t in tarefas_participante:
        print(f"Tarefa do participante: ID={t.id_task}, Nome={t.name}, Estado={t.state}")

    # Teste de deleção
    print("\nTeste de deleção:")
    deleteTask(tarefa.id_task)
    tarefa_deletada = getTaskById(tarefa.id_task)
    print(f"Tarefa deletada: {'Sim' if tarefa_deletada is None else 'Não'}") 