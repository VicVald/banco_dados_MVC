import sys
import os
import streamlit as st

# Adicionar o diretório raiz ao path para importar os módulos do back
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Controllers.UsuarioController import (
    includeUser, getUsers, getUserById, getUserByEmail,
    updateUser, deleteUser, searchUsersByName
)
from Controllers.ProjetoController import (
    includeProject, getProjects, getProjectById, deleteProject, updateProject
)
from Controllers.TarefaController import (
    includeTask, getTasks, getTaskById,
    getTasksByProject, getTasksByParticipant
)
from Controllers.ParticipanteController import (
    includeParticipante, getParticipantesByProject, getParticipantesByUser
)
from Models.Usuario import User
from Models.Projeto import Project
from Models.Tarefa import Task
from Models.Participante import Participante

# Funções para usuários
def login_user(email, password):
    user = getUserByEmail(email)
    if user and user.password == password:
        return user
    return None

def register_user(name, email, password):
    # Verificar se usuário já existe
    if getUserByEmail(email):
        return None
    new_user = User(name, email, password)
    return includeUser(new_user)

def delete_user(id_user):
    return deleteUser(id_user)

# Funções para projetos
def get_all_projects():
    user_id = st.session_state['user'].id_user if 'user' in st.session_state and st.session_state['user'] is not None else None
    projetos = getProjects()
    # Projetos onde o usuário é dono
    meus_projetos = [p for p in projetos if hasattr(p, 'owner_id') and p.owner_id == user_id]
    # Projetos onde o usuário é participante
    participantes = getParticipantesByUser(user_id)
    ids_participante = {p.id_project for p in participantes}
    projetos_participante = [p for p in projetos if p.id_project in ids_participante]
    # Unir e remover duplicados
    return list({p.id_project: p for p in meus_projetos + projetos_participante}.values())

def create_project(name, description, status, start_date, end_date):
    project = Project(name, description)
    project.status = status
    project.start_date = start_date
    project.end_date = end_date
    # Adicionar owner_id ao projeto
    if 'user' in st.session_state and st.session_state['user'] is not None:
        project.owner_id = st.session_state['user'].id_user
    return includeProject(project)

def get_project_by_id(project_id):
    return getProjectById(project_id)

def delete_project(project_id):
    return deleteProject(project_id)

def get_project_participants(project_id):
    user_id = st.session_state['user'].id_user if 'user' in st.session_state and st.session_state['user'] is not None else None
    participantes = getParticipantesByProject(project_id)
    # Filtra participantes para garantir que só veja participantes de projetos do usuário logado
    projetos_usuario = [p.id_project for p in get_all_projects()]
    return [p for p in participantes if p.id_project in projetos_usuario]

# Funções para tarefas
def get_project_tasks(project_id):
    user_id = st.session_state['user'].id_user if 'user' in st.session_state and st.session_state['user'] is not None else None
    projetos_usuario = [p.id_project for p in get_all_projects()]
    if project_id not in projetos_usuario:
        return []
    return getTasksByProject(project_id)

def create_task(project_id, name, description, state):
    projetos_usuario = [p.id_project for p in get_all_projects()]
    if project_id not in projetos_usuario:
        return None
    task = Task(None, project_id, name, description, state)
    return includeTask(task)

def update_project(project):
    return updateProject(project)

def logout():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.switch_page("pages/Login.py") 