import streamlit as st
from utils import login_user, register_user

st.set_page_config(page_title="Login/Registro", layout="wide")

st.title("Login / Registro")

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
                st.switch_page("Projects")
            else:
                st.error("Email ou senha inválidos")

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
                user = register_user(name, email, password)
                if user:
                    st.success("Registro realizado com sucesso! Faça login para continuar.")
                else:
                    st.error("Email já cadastrado")

# Botão para voltar à página inicial
if st.button("Voltar para Home"):
    st.switch_page("Home") 