import streamlit as st
from app.Views.utils import create_task, get_project_by_id, logout

st.set_page_config(page_title="Criar Tarefa", layout="wide")

# Verificar se o usuário está logado
if 'user' not in st.session_state or st.session_state['user'] is None:
    st.warning("Por favor, faça login para criar tarefas.")
    st.info('Use o menu lateral para navegar entre as páginas.')
    st.switch_page("pages/Login.py")

# Verificar se há um projeto selecionado
if 'current_project' not in st.session_state or st.session_state['current_project'] is None:
    st.error("Nenhum projeto selecionado.")
    st.info('Volte para a lista de projetos e selecione um projeto para criar uma tarefa.')
    st.switch_page("pages/Projects.py")

project = st.session_state['current_project']

st.title(f"Criar Tarefa para: {project.name}")

# Formulário para criar tarefa
with st.form("create_task_form"):
    name = st.text_input("Nome da Tarefa")
    description = st.text_area("Descrição")
    state = st.selectbox(
        "Estado",
        ["Não Iniciado", "Em Andamento", "Concluído", "Em Pausa"]
    )
    
    submitted = st.form_submit_button("Criar Tarefa")
    
    if submitted:
        if not name:
            st.error("O nome da tarefa é obrigatório!")
        else:
            task = create_task(project.id_project, name, description, state)
            if task:
                st.success("Tarefa criada com sucesso!")
                st.switch_page("pages/ProjectDetail.py")
            else:
                st.error("Erro ao criar tarefa")

# Botão para voltar aos detalhes do projeto
if st.button("Voltar para Detalhes do Projeto"):
    st.switch_page("pages/ProjectDetail.py")

if st.button("Logout"):
    logout() 