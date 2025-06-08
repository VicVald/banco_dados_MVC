import streamlit as st

st.set_page_config(page_title="Trello Clone - Home", layout="wide")

st.title("Trello Clone - Sistema de Gerenciamento de Projetos")

# Sidebar para navegação
st.sidebar.title("Navegação")
page = st.sidebar.radio(
    "Escolha uma página:",
    ["Login/Registro", "Projetos", "Criar Projeto"]
)

# Redirecionamento baseado na escolha
if page == "Login/Registro":
    st.switch_page("Login")
elif page == "Projetos":
    st.switch_page("Projects")
elif page == "Criar Projeto":
    st.switch_page("CreateProject")

# Conteúdo da página inicial
st.markdown("""
### Bem-vindo ao Sistema de Gerenciamento de Projetos

Este sistema permite:
- Gerenciar seus projetos de forma visual
- Organizar tarefas em boards e cards
- Colaborar com sua equipe
- Acompanhar o progresso dos projetos

Use o menu lateral para navegar entre as diferentes funcionalidades.
""") 