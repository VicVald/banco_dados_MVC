import streamlit as st
from utils import get_all_projects, delete_project

st.set_page_config(page_title="Projetos", layout="wide")

# Verificar se o usuário está logado
if 'user' not in st.session_state:
    st.warning("Por favor, faça login para ver seus projetos.")
    st.switch_page("Login")

st.title("Meus Projetos")

# Barra de pesquisa
search_query = st.text_input("🔍 Pesquisar projetos", "")

# Botão para criar novo projeto
if st.button("➕ Criar Novo Projeto"):
    st.switch_page("CreateProject")

# Buscar projetos
try:
    projects = get_all_projects()
    
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
                            # st.switch_page("ProjectDetail")  # Implemente se necessário
                    with col2:
                        if st.button("Excluir", key=f"delete_{project.id_project}"):
                            if st.button("Confirmar exclusão?", key=f"confirm_{project.id_project}"):
                                if delete_project(project.id_project):
                                    st.success("Projeto excluído com sucesso!")
                                    st.experimental_rerun()
                                else:
                                    st.error("Erro ao excluir projeto")

except Exception as e:
    st.error(f"Erro ao carregar projetos: {str(e)}")

# Botão para voltar à página inicial
if st.button("Voltar para Home"):
    st.switch_page("Home") 