from Controllers.UsuarioController import *
from Controllers.ProjetoController import *
from Controllers.ParticipanteController import *
from Controllers.TarefaController import *

def test_usuario():
    print("\n=== Testando UsuarioController ===")
    novo_usuario = User("Teste Usuario", "teste@email.com")
    usuario_inserido = includeUser(novo_usuario)
    if usuario_inserido is None:
        print("Erro ao inserir usuário")
        return None
    print(f"Usuário inserido: {usuario_inserido.name} - {usuario_inserido.email}")
    return usuario_inserido

def test_projeto():
    print("\n=== Testando ProjetoController ===")
    novo_projeto = Project("Projeto Teste", "Descrição do projeto teste")
    projeto_inserido = includeProject(novo_projeto)
    if projeto_inserido is None:
        print("Erro ao inserir projeto")
        return None
    print(f"Projeto inserido: {projeto_inserido.name} - {projeto_inserido.desc}")
    return projeto_inserido

def test_participante(usuario, projeto):
    if usuario is None or projeto is None:
        print("Não é possível criar participante: usuário ou projeto não existe")
        return None
    
    print("\n=== Testando ParticipanteController ===")
    novo_participante = Participante(
        id_user=usuario.id_user,
        id_project=projeto.id_project,
        funcao="Desenvolvedor",
        inicio="2024-03-20"
    )
    participante_inserido = includeParticipante(novo_participante)
    if participante_inserido is None:
        print("Erro ao inserir participante")
        return None
    print(f"Participante inserido: ID={participante_inserido.id_part}, Função={participante_inserido.funcao}")
    return participante_inserido

def test_tarefa(participante, projeto):
    if participante is None or projeto is None:
        print("Não é possível criar tarefa: participante ou projeto não existe")
        return None
    
    print("\n=== Testando TarefaController ===")
    nova_tarefa = Task(
        id_part=participante.id_part,
        id_project=projeto.id_project,
        name="Implementar Login",
        desc="Criar sistema de autenticação",
        state="To Do"
    )
    tarefa_inserida = includeTask(nova_tarefa)
    if tarefa_inserida is None:
        print("Erro ao inserir tarefa")
        return None
    print(f"Tarefa inserida: ID={tarefa_inserida.id_task}, Nome={tarefa_inserida.name}, Estado={tarefa_inserida.state}")
    return tarefa_inserida

if __name__ == "__main__":
    print("Executando testes dos controllers...")
    
    # Teste sequencial com verificação de erros
    usuario = test_usuario()
    if usuario is None:
        print("Testes interrompidos: erro ao criar usuário")
        exit(1)
        
    projeto = test_projeto()
    if projeto is None:
        print("Testes interrompidos: erro ao criar projeto")
        exit(1)
        
    participante = test_participante(usuario, projeto)
    if participante is None:
        print("Testes interrompidos: erro ao criar participante")
        exit(1)
        
    tarefa = test_tarefa(participante, projeto)
    if tarefa is None:
        print("Testes interrompidos: erro ao criar tarefa")
        exit(1)
        
    print("\nTodos os testes foram concluídos com sucesso!")
