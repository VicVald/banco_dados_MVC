import streamlit as st
from app.Views.utils import get_project_by_id, update_project, get_project_participants, getUsers, includeParticipante, get_all_projects, logout, get_project_tasks
from app.Controllers.ParticipanteController import deleteParticipante
from app.Controllers.TarefaController import updateTask, deleteTask
from app.Models.Tarefa import Task

st.set_page_config(page_title="Editar Projeto", layout="wide")

# Verificar se o usuário está logado
if 'user' not in st.session_state or st.session_state['user'] is None:
    st.warning("Por favor, faça login para editar um projeto.")
    st.info('Use o menu lateral para navegar entre as páginas.')
    st.switch_page("pages/Login.py")

# Verificar se há um projeto selecionado
if 'current_project' not in st.session_state or st.session_state['current_project'] is None:
    st.error("Nenhum projeto selecionado.")
    st.info('Volte para a lista de projetos e selecione um projeto para editar.')
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

st.title(f"Editar Projeto: {project.name}")

# Formulário para editar projeto
with st.form("edit_project_form"):
    name = st.text_input("Nome do Projeto", value=project.name)
    description = st.text_area("Descrição", value=project.desc or "")
    status = st.selectbox(
        "Status",
        ["Não Iniciado", "Em Andamento", "Concluído", "Em Pausa"],
        index=["Não Iniciado", "Em Andamento", "Concluído", "Em Pausa"].index(project.status) if project.status in ["Não Iniciado", "Em Andamento", "Concluído", "Em Pausa"] else 0
    )
    
    # Campos adicionais
    st.subheader("Configurações Adicionais")
    start_date = st.date_input("Data de Início", value=project.start_date if project.start_date else None)
    end_date = st.date_input("Data de Término Prevista", value=project.end_date if project.end_date else None)
    
    submitted = st.form_submit_button("Salvar Alterações")
    
    if submitted:
        if not name:
            st.error("O nome do projeto é obrigatório!")
        else:
            # Atualizar o projeto
            project.name = name
            project.desc = description
            project.status = status
            project.start_date = start_date
            project.end_date = end_date
            update_project(project)
            st.success("Projeto atualizado com sucesso!")
            st.session_state['current_project'] = project
            st.switch_page("pages/ProjectDetail.py")

# Botão para voltar aos detalhes do projeto
if st.button("Voltar para Detalhes do Projeto"):
    st.switch_page("pages/ProjectDetail.py")

st.subheader("Participantes do Projeto")
project_participants = get_project_participants(project.id_project)
users = getUsers()
user_dict = {u.id_user: u for u in users}
# Listar participantes atuais com opção de remover
if project_participants:
    for p in project_participants:
        colp1, colp2 = st.columns([3,1])
        with colp1:
            user = user_dict.get(int(p.id_user))
            nome = user.name if user else f"Usuário {p.id_user} (não encontrado)"
            st.markdown(f"- {nome} ({p.funcao})")
        with colp2:
            if st.button(f"Remover", key=f"remover_{p.id_part}"):
                deleteParticipante(p.id_part)
                st.success("Participante removido!")
                st.rerun()
else:
    st.info("Nenhum participante no projeto.")
# Adicionar novo participante
st.markdown("---")
st.markdown("**Adicionar Novo Participante**")
user_options = {f"{u.name} ({u.email})": u.id_user for u in users if u.id_user != st.session_state['user'].id_user and u.id_user not in [p.id_user for p in project_participants]}
if user_options:
    selected_label = st.selectbox("Selecione o usuário", list(user_options.keys()))
    selected_user_id = user_options[selected_label]
    funcao = st.text_input("Função no projeto")
    data_inicio = st.date_input("Data de início")
    if st.button("Adicionar Participante"):
        from app.Models.Participante import Participante
        novo_participante = Participante(
            id_user=selected_user_id,
            id_project=project.id_project,
            funcao=funcao,
            inicio=str(data_inicio)
        )
        includeParticipante(novo_participante)
        st.success("Participante adicionado!")
        st.rerun()
else:
    st.info("Não há outros usuários disponíveis para adicionar.")

# Seção de Tarefas
st.markdown("---")
st.subheader("Tarefas do Projeto")
tasks = get_project_tasks(project.id_project)

if tasks:
    for task in tasks:
        with st.expander(f"{task.name} - {task.state}"):
            with st.form(f"edit_task_form_{task.id_task}"):
                task_name = st.text_input("Nome da Tarefa", value=task.name, key=f"name_{task.id_task}")
                task_description = st.text_area("Descrição", value=task.desc, key=f"desc_{task.id_task}")
                task_state = st.selectbox(
                    "Estado",
                    ["Não Iniciado", "Em Andamento", "Concluído", "Em Pausa"],
                    index=["Não Iniciado", "Em Andamento", "Concluído", "Em Pausa"].index(task.state) if task.state in ["Não Iniciado", "Em Andamento", "Concluído", "Em Pausa"] else 0,
                    key=f"state_{task.id_task}"
                )
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.form_submit_button("Salvar Alterações"):
                        task.name = task_name
                        task.desc = task_description
                        task.state = task_state
                        updateTask(task)
                        st.success("Tarefa atualizada com sucesso!")
                        st.rerun()
                with col2:
                    if st.form_submit_button("Excluir Tarefa"):
                        deleteTask(task.id_task)
                        st.success("Tarefa excluída com sucesso!")
                        st.rerun()
else:
    st.info("Nenhuma tarefa criada para este projeto.")

if st.button("Logout"):
    logout() 