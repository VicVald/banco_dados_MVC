import streamlit as st
from app.Views.utils import get_project_by_id, get_project_tasks, get_project_participants, getUsers, get_all_projects, logout

# Carregar todos os usuários uma única vez para uso global
users = getUsers()
user_dict = {u.id_user: u for u in users}

st.set_page_config(page_title="Detalhes do Projeto", layout="wide")

# Verificar se o usuário está logado
if 'user' not in st.session_state or st.session_state['user'] is None:
    st.warning("Por favor, faça login para ver os detalhes do projeto.")
    st.info('Use o menu lateral para navegar entre as páginas.')
    st.switch_page("pages/Login.py")

# Verificar se há um projeto selecionado e se ele ainda existe
if 'current_project' not in st.session_state or st.session_state['current_project'] is None:
    st.error("Nenhum projeto selecionado.")
    st.info('Volte para a lista de projetos e selecione um projeto para ver seus detalhes.')
    st.switch_page("pages/Projects.py")
else:
    # Verifica se o projeto ainda existe no banco
    all_projects = get_all_projects()
    current_id = getattr(st.session_state['current_project'], 'id_project', None)
    if not any(p.id_project == current_id for p in all_projects):
        del st.session_state['current_project']
        st.warning("O projeto selecionado foi excluído.")
        st.switch_page("pages/Projects.py")

project = st.session_state['current_project']

# Título e informações básicas
st.title(f"Detalhes do Projeto: {project.name}")

# Layout em colunas para informações principaisimage.png
col1, col2 = st.columns(2)

with col1:
    st.subheader("Informações Gerais")
    st.markdown(f"**Descrição:** {project.desc or 'Sem descrição'}")
    st.markdown(f"**Status:** {project.status or 'Não definido'}")
    if hasattr(project, 'start_date'):
        st.markdown(f"**Data de Início:** {project.start_date}")
    if hasattr(project, 'end_date'):
        st.markdown(f"**Data de Término Prevista:** {project.end_date}")

with col2:
    st.subheader("Participantes")
    try:
        participants = get_project_participants(project.id_project)
        if participants:
            for participant in participants:
                user = user_dict.get(int(participant.id_user))
                nome = user.name if user else f"Usuário {participant.id_user} (não encontrado)"
                st.markdown(f"- {nome} ({participant.funcao})")
        else:
            st.info("Nenhum participante adicionado ao projeto.")
    except Exception as e:
        st.error(f"Erro ao carregar participantes: {str(e)}")

    # Formulário para adicionar participante
    st.markdown("---")
    st.markdown("**Adicionar Participante**")
    participants = get_project_participants(project.id_project)
    ids_participantes = [p.id_user for p in participants]
    user_options = {f"{u.name} ({u.email})": u.id_user for u in users if u.id_user != st.session_state['user'].id_user and u.id_user not in ids_participantes}
    if user_options:
        with st.form("add_participant_form"):
            selected_user = st.selectbox("Selecione o usuário", list(user_options.keys()))
            funcao = st.text_input("Função no projeto")
            data_inicio = st.date_input("Data de início")
            add_participant = st.form_submit_button("Adicionar Participante")
            if add_participant:
                from app.Models.Participante import Participante
                novo_participante = Participante(
                    id_user=user_options[selected_user],
                    id_project=project.id_project,
                    funcao=funcao,
                    inicio=str(data_inicio)
                )
                from app.Views.utils import includeParticipante
                includeParticipante(novo_participante)
                st.success(f"Participante {selected_user} adicionado!")
                st.rerun()
    else:
        st.info("Não há outros usuários disponíveis para adicionar.")

# Seção de Tarefas
st.subheader("Tarefas do Projeto")
try:
    tasks = get_project_tasks(project.id_project)
    if tasks:
        for task in tasks:
            with st.expander(f"{task.name} - {task.state}"):
                st.markdown(f"**Descrição:** {task.desc}")
                if hasattr(task, 'assigned_to'):
                    st.markdown(f"**Atribuído a:** {task.assigned_to}")
    else:
        st.info("Nenhuma tarefa criada para este projeto.")
except Exception as e:
    st.error(f"Erro ao carregar tarefas: {str(e)}")

# Botões de ação
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Voltar para Projetos"):
        st.switch_page("pages/Projects.py")
with col2:
    if st.button("Editar Projeto"):
        st.switch_page("pages/EditProject.py")
with col3:
    if st.button("Adicionar Tarefa"):
        st.switch_page("pages/CreateTask.py")

if st.button("Logout"):
    logout() 