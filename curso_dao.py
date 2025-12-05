# Módulo: curso_dao.py
from conexao import conectar, fechar_conexao
from mysql.connector import Error

class CursoDAO:
    
    # C - CREATE (Inserir Curso)
    def inserir(self, nome, carga_horaria, valor, data_inicio):
        sql = "INSERT INTO CURSO (nome, carga_horaria, valor, data_inicio) VALUES (%s, %s, %s, %s)"
        conn = conectar()
        if conn is None: return
        
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (nome, carga_horaria, valor, data_inicio))
            conn.commit()
            print(f"\n[SUCESSO] Curso '{nome}' inserido com ID: {cursor.lastrowid}")
        except Error as e:
            print(f"\n[ERRO] Falha ao inserir curso: {e}")
        finally:
            cursor.close()
            fechar_conexao(conn)

    # R - READ (Consultar Todos os Cursos)
    def consultar_todos(self):
        sql = "SELECT id, nome, carga_horaria, valor, data_inicio FROM CURSO"
        conn = conectar()
        if conn is None: return []
        
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as e:
            print(f"\n[ERRO] Falha ao consultar cursos: {e}")
            return []
        finally:
            cursor.close()
            fechar_conexao(conn)

    # U - UPDATE (Atualizar Valor do Curso)
    def atualizar_valor(self, curso_id, novo_valor):
        sql = "UPDATE CURSO SET valor = %s WHERE id = %s"
        conn = conectar()
        if conn is None: return
        
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (novo_valor, curso_id))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[SUCESSO] Valor do Curso ID {curso_id} atualizado para R${novo_valor}.")
            else:
                print(f"\n[AVISO] Curso ID {curso_id} não encontrado.")
        except Error as e:
            print(f"\n[ERRO] Falha ao atualizar valor: {e}")
        finally:
            cursor.close()
            fechar_conexao(conn)
            
    # D - DELETE (Deletar Curso)
    def deletar(self, curso_id):
        sql = "DELETE FROM CURSO WHERE id = %s"
        conn = conectar()
        if conn is None: return
        
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (curso_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[SUCESSO] Curso ID {curso_id} deletado.")
            else:
                print(f"\n[AVISO] Curso ID {curso_id} não encontrado.")
        except Error as e:
            print(f"\n[ERRO] Falha ao deletar curso: {e}")
        finally:
            cursor.close()
            fechar_conexao(conn)