import streamlit as st
from app.Views.utils import get_all_projects, delete_project, logout

st.set_page_config(page_title="Projetos", layout="wide")

# Verificar se o usuário está logado
if 'user' not in st.session_state:
    st.warning("Por favor, faça login para ver seus projetos.")
    st.info('Use o menu lateral para navegar entre as páginas.')
    st.switch_page("pages/Login.py")

st.title("Meus Projetos")

# Barra de pesquisa
search_query = st.text_input("🔍 Pesquisar projetos", "")

# Botão para criar novo projeto
if st.button("➕ Criar Novo Projeto"):
    st.switch_page("pages/CreateProject.py")

# Exibir botão de logout global
if 'user' in st.session_state and st.session_state['user'] is not None:
    if st.button("Logout"):
        logout()
else:
    st.switch_page("pages/Login.py")

try:
    projects = get_all_projects()
    user_id = st.session_state['user'].id_user
    projects = [p for p in projects if hasattr(p, 'owner_id') and p.owner_id == user_id]

    # Filtrar projetos baseado na pesquisa
    if search_query:
        projects = [p for p in projects if search_query.lower() in p.name.lower()]

    if not projects:
        st.info("Nenhum projeto encontrado.")
    else:
        # Criar cards para cada projeto
        cols = st.columns(3)
        for idx, project in enumerate(projects):
            with cols[idx % 3]:
                with st.container():
                    st.markdown(f"### {project.name}")
                    st.markdown(f"**Descrição:** {project.desc or 'Sem descrição'}")
                    
                    # Botões de ação
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("Ver Detalhes", key=f"view_{project.id_project}"):
                            st.session_state['current_project'] = project
                            st.switch_page("pages/ProjectDetail.py")
                    with col2:
                        if st.button("Excluir", key=f"delete_{project.id_project}"):
                            st.info("Processo de exclusão iniciado...")
                            if delete_project(project.id_project):
                                # Limpar o projeto selecionado do session_state se for o excluído
                                if 'current_project' in st.session_state and getattr(st.session_state['current_project'], 'id_project', None) == project.id_project:
                                    del st.session_state['current_project']
                                st.success("Projeto excluído com sucesso!")
                                st.rerun()
                            else:
                                st.error("Erro ao excluir projeto")
except Exception as e:
    st.error(f"Erro ao carregar projetos: {str(e)}") 