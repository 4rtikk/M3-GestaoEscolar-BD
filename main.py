# Módulo: main.py
from aluno_dao import AlunoDAO
from curso_dao import CursoDAO
from matricula_dao import MatriculaDAO
from datetime import date # Para usar a data atual na matrícula

# Instanciação dos DAOs
aluno_dao = AlunoDAO()
curso_dao = CursoDAO()
matricula_dao = MatriculaDAO()

def menu_principal():
    print("\n" + "="*50)
    print("        Sistema de Gestão Escolar - CRUD")
    print("="*50)
    print("1. Gerenciar Alunos (CRUD)")
    print("2. Gerenciar Cursos (CRUD)")
    print("3. Gerenciar Matrículas (CRUD)")
    print("4. Sair")
    return input("Escolha uma opção: ")

# --- Funções CRUD de ALUNO ---
def crud_aluno():
    while True:
        print("\n--- Gerenciar Alunos ---")
        print("1. Inserir Aluno (Create)")
        print("2. Consultar Todos (Read)")
        print("3. Atualizar Email (Update)")
        print("4. Deletar Aluno (Delete)")
        print("5. Voltar")
        escolha = input("Opção: ")
        
        if escolha == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            data_nascimento = input("Data Nascimento (AAAA-MM-DD): ")
            aluno_dao.inserir(nome, cpf, email, data_nascimento)
        elif escolha == '2':
            alunos = aluno_dao.consultar_todos()
            if alunos:
                print("\n--- Lista de Alunos ---")
                for a in alunos:
                    print(f"ID: {a['id']}, Nome: {a['nome']}, Email: {a['email']}")
        elif escolha == '3':
            aluno_id = input("ID do Aluno para atualizar: ")
            novo_email = input("Novo Email: ")
            aluno_dao.atualizar_email(aluno_id, novo_email)
        elif escolha == '4':
            aluno_id = input("ID do Aluno para deletar: ")
            aluno_dao.deletar(aluno_id)
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")

# --- Funções CRUD de CURSO ---
def crud_curso():
    while True:
        print("\n--- Gerenciar Cursos ---")
        print("1. Inserir Curso (Create)")
        print("2. Consultar Todos (Read)")
        print("3. Atualizar Valor (Update)")
        print("4. Deletar Curso (Delete)")
        print("5. Voltar")
        escolha = input("Opção: ")
        
        if escolha == '1':
            nome = input("Nome do Curso: ")
            carga_horaria = input("Carga Horária: ")
            valor = input("Valor: ")
            data_inicio = input("Data Início (AAAA-MM-DD): ")
            curso_dao.inserir(nome, carga_horaria, valor, data_inicio)
        elif escolha == '2':
            cursos = curso_dao.consultar_todos()
            if cursos:
                print("\n--- Lista de Cursos ---")
                for c in cursos:
                    print(f"ID: {c['id']}, Nome: {c['nome']}, Valor: R${c['valor']}, Carga Horária: {c['carga_horaria']}h")
        elif escolha == '3':
            curso_id = input("ID do Curso para atualizar: ")
            novo_valor = input("Novo Valor: ")
            curso_dao.atualizar_valor(curso_id, novo_valor)
        elif escolha == '4':
            curso_id = input("ID do Curso para deletar: ")
            curso_dao.deletar(curso_id)
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")
            
# --- Funções CRUD de MATRICULA ---
def crud_matricula():
    while True:
        print("\n--- Gerenciar Matrículas ---")
        print("1. Registrar Matrícula (Create)")
        print("2. Consultar Todas (Read)")
        print("3. Atualizar Situação (Update)")
        print("4. Cancelar Matrícula (Delete)")
        print("5. Voltar")
        escolha = input("Opção: ")
        
        if escolha == '1':
            fk_aluno = input("ID do Aluno: ")
            fk_curso = input("ID do Curso: ")
            # Data de matrícula automática, ou pedir ao usuário:
            data_matricula = date.today().strftime("%Y-%m-%d")
            print(f"Data da Matrícula: {data_matricula}")
            matricula_dao.inserir(fk_aluno, fk_curso, data_matricula, 'ATIVA')
        elif escolha == '2':
            matriculas = matricula_dao.consultar_todos()
            if matriculas:
                print("\n--- Matrículas Registradas (Detalhes) ---")
                for m in matriculas:
                    print(f"ID: {m['id']} | Aluno: {m['aluno_nome']} | Curso: {m['curso_nome']} | Situação: {m['situacao']} | Data: {m['data_matricula']}")
        elif escolha == '3':
            mat_id = input("ID da Matrícula para atualizar: ")
            nova_situacao = input("Nova Situação (ATIVA, CONCLUIDA, TRANCADA): ")
            matricula_dao.atualizar_situacao(mat_id, nova_situacao)
        elif escolha == '4':
            mat_id = input("ID da Matrícula para deletar: ")
            matricula_dao.deletar(mat_id)
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")
            
# --- Execução Principal ---
if __name__ == '__main__':
    while True:
        opcao = menu_principal()
        if opcao == '1':
            crud_aluno()
        elif opcao == '2':
            crud_curso()
        elif opcao == '3':
            crud_matricula()
        elif opcao == '4':
            print("Saindo do Sistema. Obrigado!")
            break
        else:
            print("Opção inválida.")