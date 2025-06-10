import streamlit as st
from app.Views.utils import login_user, register_user, delete_user

st.set_page_config(page_title="Login/Registro", layout="wide")

st.title("Login / Registro")

# Bloquear acesso à tela de login se já estiver logado
if 'user' in st.session_state and st.session_state['user'] is not None:
    st.switch_page("pages/Projects.py")
    st.stop()

# Criar duas colunas para login e registro
col1, col2 = st.columns(2)

with col1:
    st.header("Login")
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Entrar")
        
        if submitted:
            user = login_user(email, password)
            if user:
                st.session_state['user'] = user
                st.success("Login realizado com sucesso!")
                st.info('Use o menu lateral para navegar entre as páginas.')
            else:
                st.error("Email ou senha inválidos")
    # Se o usuário estiver logado, permitir exclusão
    if 'user' in st.session_state and st.session_state['user'] is not None:
        st.markdown("---")
        st.warning(f"Excluir usuário: {st.session_state['user'].name} ({st.session_state['user'].email})")
        if st.button("Excluir minha conta", type="primary"):
            delete_user(st.session_state['user'].id_user)
            st.success("Usuário excluído com sucesso!")
            del st.session_state['user']
            st.rerun()

with col2:
    st.header("Registro")
    with st.form("register_form"):
        name = st.text_input("Nome")
        email = st.text_input("Email")
        password = st.text_input("Senha", type="password")
        confirm_password = st.text_input("Confirmar Senha", type="password")
        submitted = st.form_submit_button("Registrar")
        
        if submitted:
            if password != confirm_password:
                st.error("As senhas não coincidem")
            else:
                user, error = register_user(name, email, password)
                if user:
                    st.success("Registro realizado com sucesso! Faça login para continuar.")
                else:
                    st.error(error or "Email já cadastrado")

def logout():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.switch_page("pages/Login.py")
