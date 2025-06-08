import streamlit as st
from utils import create_project

st.set_page_config(page_title="Criar Projeto", layout="wide")

# Verificar se o usuário está logado
if 'user' not in st.session_state:
    st.warning("Por favor, faça login para criar um projeto.")
    st.switch_page("Login")

st.title("Criar Novo Projeto")

# Formulário para criar projeto
with st.form("create_project_form"):
    name = st.text_input("Nome do Projeto")
    description = st.text_area("Descrição")
    status = st.selectbox(
        "Status Inicial",
        ["Não Iniciado", "Em Andamento", "Concluído", "Em Pausa"]
    )
    
    # Campos adicionais
    st.subheader("Configurações Adicionais")
    start_date = st.date_input("Data de Início")
    end_date = st.date_input("Data de Término Prevista")
    
    submitted = st.form_submit_button("Criar Projeto")
    
    if submitted:
        if not name:
            st.error("O nome do projeto é obrigatório!")
        else:
            project = create_project(name, description, status, start_date, end_date)
            if project:
                st.success("Projeto criado com sucesso!")
                st.session_state['current_project'] = project
                # st.switch_page("ProjectDetail")  # Implemente se necessário
            else:
                st.error("Erro ao criar projeto")

# Botão para voltar à página de projetos
if st.button("Voltar para Projetos"):
    st.switch_page("Projects") 