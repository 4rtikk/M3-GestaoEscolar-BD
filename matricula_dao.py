# Módulo: matricula_dao.py
from conexao import conectar, fechar_conexao
from mysql.connector import Error

class MatriculaDAO:
    
    # C - CREATE (Registrar Matrícula)
    def inserir(self, fk_aluno, fk_curso, data_matricula, situacao):
        sql = "INSERT INTO MATRICULA (fk_aluno, fk_curso, data_matricula, situacao) VALUES (%s, %s, %s, %s)"
        conn = conectar()
        if conn is None: return
        
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (fk_aluno, fk_curso, data_matricula, situacao))
            conn.commit()
            print(f"\n[SUCESSO] Matrícula ID {cursor.lastrowid} registrada (Aluno: {fk_aluno}, Curso: {fk_curso}).")
        except Error as e:
            # Captura erros de FK (ex: Aluno/Curso não existe) ou UNIQUE KEY (aluno já matriculado no curso)
            print(f"\n[ERRO] Falha ao registrar matrícula. Verifique se o Aluno e o Curso existem e se a matrícula já não foi feita: {e}")
        finally:
            cursor.close()
            fechar_conexao(conn)

    # R - READ (Consultar Matrículas Detalhadas)
    # Usa JOIN para trazer o nome do Aluno e do Curso
    def consultar_todos(self):
        sql = """
        SELECT M.id, A.nome AS aluno_nome, C.nome AS curso_nome, M.data_matricula, M.situacao 
        FROM MATRICULA M
        JOIN ALUNO A ON M.fk_aluno = A.id
        JOIN CURSO C ON M.fk_curso = C.id
        ORDER BY M.data_matricula DESC
        """
        conn = conectar()
        if conn is None: return []
        
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as e:
            print(f"\n[ERRO] Falha ao consultar matrículas detalhadas: {e}")
            return []
        finally:
            cursor.close()
            fechar_conexao(conn)

    # U - UPDATE (Atualizar Situação da Matrícula)
    def atualizar_situacao(self, matricula_id, nova_situacao):
        sql = "UPDATE MATRICULA SET situacao = %s WHERE id = %s"
        conn = conectar()
        if conn is None: return
        
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (nova_situacao, matricula_id))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[SUCESSO] Situação da Matrícula ID {matricula_id} atualizada para '{nova_situacao}'.")
            else:
                print(f"\n[AVISO] Matrícula ID {matricula_id} não encontrada.")
        except Error as e:
            print(f"\n[ERRO] Falha ao atualizar situação: {e}")
        finally:
            cursor.close()
            fechar_conexao(conn)
            
    # D - DELETE (Cancelar/Deletar Matrícula)
    def deletar(self, matricula_id):
        sql = "DELETE FROM MATRICULA WHERE id = %s"
        conn = conectar()
        if conn is None: return
        
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (matricula_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[SUCESSO] Matrícula ID {matricula_id} deletada.")
            else:
                print(f"\n[AVISO] Matrícula ID {matricula_id} não encontrada.")
        except Error as e:
            print(f"\n[ERRO] Falha ao deletar matrícula: {e}")
        finally:
            cursor.close()
            fechar_conexao(conn)