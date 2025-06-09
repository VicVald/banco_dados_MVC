import streamlit as st
from app.Views.utils import create_project, logout

st.set_page_config(page_title="Criar Projeto", layout="wide")

# Verificar se o usuário está logado
if 'user' not in st.session_state or st.session_state['user'] is None:
    st.switch_page("pages/Login.py")

st.title("Criar Novo Projeto")

# Controle de fluxo para evitar forms aninhados
if 'project_created' not in st.session_state:
    st.session_state['project_created'] = False

if not st.session_state['project_created']:
    with st.form("create_project_form"):
        name = st.text_input("Nome do Projeto")
        description = st.text_area("Descrição")
        status = st.selectbox(
            "Status Inicial",
            ["Não Iniciado", "Em Andamento", "Concluído", "Em Pausa"]
        )
        start_date = st.date_input("Data de Início")
        end_date = st.date_input("Data de Término Prevista")
        submitted = st.form_submit_button("Criar Projeto")
        if submitted:
            if not name:
                st.error("O nome do projeto é obrigatório!")
            else:
                current_user = st.session_state['user']
                project = create_project(name, description, status, start_date, end_date)
                if project:
                    st.success("Projeto criado com sucesso!")
                    st.session_state['current_project'] = project
                    st.session_state['project_created'] = True
                else:
                    st.error("Erro ao criar projeto")

# Formulário para adicionar participantes (fora do form de criar projeto)
if st.session_state['project_created']:
    st.markdown('---')
    st.markdown('**Adicionar Participantes ao Projeto**')
    from app.Views.utils import getUsers, includeParticipante
    from app.Models.Participante import Participante
    users = getUsers()
    current_user = st.session_state['user']
    project = st.session_state['current_project']
    user_options = {f"{u.name} ({u.email})": u.id_user for u in users if u.id_user != current_user.id_user}
    if user_options:
        with st.form("add_participant_form"):
            selected_user = st.selectbox("Selecione o usuário", list(user_options.keys()))
            funcao = st.text_input("Função no projeto")
            data_inicio = st.date_input("Data de início")
            add_participant = st.form_submit_button("Adicionar Participante")
            if add_participant:
                novo_participante = Participante(
                    id_user=user_options[selected_user],
                    id_project=project.id_project,
                    funcao=funcao,
                    inicio=str(data_inicio)
                )
                includeParticipante(novo_participante)
                st.success(f"Participante {selected_user} adicionado!")
                st.rerun()
        if st.button("Finalizar e ir para detalhes do projeto"):
            st.session_state['project_created'] = False
            st.switch_page("pages/ProjectDetail.py")
    else:
        st.info("Não há outros usuários disponíveis para adicionar.")

# Botão para voltar à página de projetos
if st.button("Voltar para Projetos"):
    st.switch_page("pages/Projects.py")

# Botão de logout global
if st.button("Logout"):
    logout() 