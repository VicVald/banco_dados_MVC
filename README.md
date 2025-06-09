# banco_dados_MVC

## Visão Geral

Este projeto é um sistema de gerenciamento de projetos inspirado no Trello, utilizando arquitetura MVC e banco de dados SQLite. Agora conta com uma interface web moderna desenvolvida em Streamlit, permitindo o gerenciamento visual de projetos, tarefas e equipes.

---

## Funcionalidades Principais

- **Interface Web com Streamlit**: Interação visual para login, cadastro, gerenciamento de projetos, tarefas e participantes.
- **Gestão de Usuários**: 
  - Registro e login de usuários
  - Exclusão de conta
  - Sistema de autenticação seguro
- **Gestão de Projetos**: 
  - Criação de projetos com nome, descrição, status e datas
  - Edição completa de projetos
  - Exclusão de projetos
  - Visualização detalhada de projetos
  - Pesquisa de projetos por nome
- **Gestão de Participantes**: 
  - Atribuição de participantes com função e data de início
  - Remoção de participantes
  - Visualização de equipe por projeto
- **Gestão de Tarefas**: 
  - Criação de tarefas com nome, descrição e estado
  - Edição de tarefas existentes
  - Exclusão de tarefas
  - Visualização de tarefas por projeto
  - Estados: Não Iniciado, Em Andamento, Concluído, Em Pausa
- **Banco de Dados SQLite**: Scripts para criação, limpeza e manipulação das tabelas.

---

## Estrutura do Projeto

```
├── app/
│   ├── Controllers/        # Lógica de controle (Usuário, Projeto, Tarefa, Participante)
│   ├── Models/             # Modelos de dados (User, Project, Task, Participante)
│   ├── Service/            # Scripts de banco e utilidades
│   └── Views/              # Utilitários e integração frontend-backend
├── pages/                  # Páginas Streamlit (Login, Projetos, Detalhes, etc)
├── Trello.db               # Banco de dados SQLite
├── requirements.txt        # Dependências do projeto
├── .gitignore              # Arquivos e pastas ignorados pelo git
├── Home.py                 # Página inicial do sistema
└── README.md               # Este arquivo
```

---

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/VicVald/banco_dados_MVC.git
   cd banco_dados_MVC
   ```
2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate    # Windows
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Execute o sistema:**
   ```bash
   streamlit run Home.py
   ```

---

## Resumo das principais diferenças em relação ao projeto original

- O projeto original era apenas backend (scripts de banco, controllers, models, sem interface web).
- **A principal evolução foi a criação de uma interface web moderna e funcional com Streamlit**, tornando o sistema utilizável por qualquer usuário via navegador.
- Foram implementadas funcionalidades completas de autenticação, CRUD de projetos, gerenciamento de participantes e visualização de tarefas.
- O código foi modularizado e organizado para facilitar manutenção e expansão futura.
- Adicionado sistema de pesquisa de projetos
- Implementado gerenciamento completo de tarefas (CRUD)
- Melhorias na interface do usuário com feedback visual para ações
- Sistema de navegação intuitivo entre páginas
- Gerenciamento de estado da sessão do usuário

---

## Créditos

Desenvolvido por [VicVald](https://github.com/VicVald) e colaboradores.

---

## Como contribuir

Sugestões, melhorias e pull requests são bem-vindos! Sinta-se à vontade para abrir uma issue ou contribuir diretamente.

---

## Contato

Dúvidas ou sugestões? Entre em contato pelo GitHub ou abra uma issue no repositório.
