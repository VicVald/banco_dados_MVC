import sys
import os

# Adicionar o diretório raiz ao path para importar os módulos do back
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Controllers.UsuarioController import (
    includeUser, getUsers, getUserById, getUserByEmail,
    updateUser, deleteUser, searchUsersByName
)
from Controllers.ProjetoController import (
    includeProject, getProjects, getProjectById, deleteProject
)
from Controllers.TarefaController import (
    includeTask, getTasks, getTaskById,
    getTasksByProject, getTasksByParticipant
)
from Models.Usuario import User
from Models.Projeto import Project
from Models.Tarefa import Task

# Funções para usuários
def login_user(email, password):
    user = getUserByEmail(email)
    if user:
        # TODO: Implementar verificação de senha quando adicionar autenticação
        return user
    return None

def register_user(name, email, password):
    # Verificar se usuário já existe
    if getUserByEmail(email):
        return None
    
    new_user = User(name, email)
    return includeUser(new_user)

# Funções para projetos
def get_all_projects():
    return getProjects()

def create_project(name, description, status, start_date, end_date):
    project = Project(name, description)
    return includeProject(project)

def get_project_by_id(project_id):
    return getProjectById(project_id)

def delete_project(project_id):
    return deleteProject(project_id)

# Funções para tarefas
def get_project_tasks(project_id):
    return getTasksByProject(project_id)

def create_task(project_id, name, description, state):
    # TODO: Implementar quando tiver sistema de participantes
    task = Task(None, project_id, name, description, state)
    return includeTask(task) 