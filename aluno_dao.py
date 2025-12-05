# Módulo: aluno_dao.py
from conexao import conectar, fechar_conexao

class AlunoDAO:
    
    # ----------------------------------------------------
    # C - CREATE (Criar)
    # Sintaxe SQL: INSERT INTO ALUNO (nome, cpf, email, data_nascimento) VALUES (..., ..., ..., ...);
    def inserir(self, nome, cpf, email, data_nascimento):
        sql = "INSERT INTO ALUNO (nome, cpf, email, data_nascimento) VALUES (%s, %s, %s, %s)"
        conn = conectar()
        if conn is None: return
        
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (nome, cpf, email, data_nascimento))
            conn.commit()
            print(f"\n[SUCESSO] Aluno '{nome}' inserido com ID: {cursor.lastrowid}")
        except Error as e:
            print(f"\n[ERRO] Falha ao inserir aluno: {e}")
        finally:
            cursor.close()
            fechar_conexao(conn)

    # ----------------------------------------------------
    # R - READ (Consultar)
    # Sintaxe SQL: SELECT id, nome, cpf, email, data_nascimento FROM ALUNO WHERE id = %s;
    def consultar_por_id(self, aluno_id):
        sql = "SELECT id, nome, cpf, email, data_nascimento FROM ALUNO WHERE id = %s"
        # O restante do código de SELECT...
        conn = conectar()
        if conn is None: return None
        
        cursor = conn.cursor(dictionary=True) # Retorna como dicionário para fácil leitura
        try:
            cursor.execute(sql, (aluno_id,))
            resultado = cursor.fetchone()
            return resultado
        except Error as e:
            print(f"\n[ERRO] Falha ao consultar aluno: {e}")
            return None
        finally:
            cursor.close()
            fechar_conexao(conn)
            
    # Sintaxe SQL: SELECT id, nome, cpf, email, data_nascimento FROM ALUNO;
    def consultar_todos(self):
        sql = "SELECT id, nome, cpf, email, data_nascimento FROM ALUNO"
        # O restante do código de SELECT ALL...
        conn = conectar()
        if conn is None: return []
        
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as e:
            print(f"\n[ERRO] Falha ao consultar todos os alunos: {e}")
            return []
        finally:
            cursor.close()
            fechar_conexao(conn)

    # ----------------------------------------------------
    # U - UPDATE (Atualizar)
    # Sintaxe SQL: UPDATE ALUNO SET email = %s WHERE id = %s;
    def atualizar_email(self, aluno_id, novo_email):
        sql = "UPDATE ALUNO SET email = %s WHERE id = %s"
        # O restante do código de UPDATE...
        conn = conectar()
        if conn is None: return
        
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (novo_email, aluno_id))
            conn.commit()
            print(f"\n[SUCESSO] E-mail do Aluno ID {aluno_id} atualizado.")
        except Error as e:
            print(f"\n[ERRO] Falha ao atualizar email: {e}")
        finally:
            cursor.close()
            fechar_conexao(conn)
            
    # ----------------------------------------------------
    # D - DELETE (Deletar)
    # Sintaxe SQL: DELETE FROM ALUNO WHERE id = %s;
    def deletar(self, aluno_id):
        sql = "DELETE FROM ALUNO WHERE id = %s"
        # O restante do código de DELETE...
        conn = conectar()
        if conn is None: return
        
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (aluno_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[SUCESSO] Aluno ID {aluno_id} deletado.")
            else:
                print(f"\n[AVISO] Aluno ID {aluno_id} não encontrado.")
        except Error as e:
            print(f"\n[ERRO] Falha ao deletar aluno: {e}")
        finally:
            cursor.close()
            fechar_conexao(conn)