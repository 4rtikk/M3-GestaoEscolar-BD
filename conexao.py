# Módulo: conexao.py

import mysql.connector
from mysql.connector import Error

# Configurações do Banco de Dados (Use suas credenciais)
DB_CONFIG = {
    "host": "localhost",
    "database": "GestaoEscolarDB",
    "user": "root",  # Mude para o seu usuário MySQL
    "password": "193838" # Mude para sua senha
}

def conectar():
    """Tenta estabelecer a conexão com o MySQL."""
    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            print("Conexão com MySQL estabelecida com sucesso!")
        return conn
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def fechar_conexao(conn):
    """Fecha a conexão com o banco de dados."""
    if conn and conn.is_connected():
        conn.close()
        # print("Conexão com MySQL encerrada.")

if __name__ == '__main__':
    # Teste de conexão (opcional)
    conn = conectar()
    fechar_conexao(conn)