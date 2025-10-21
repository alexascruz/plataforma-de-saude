#Criação do banco de dados
import sqlite3

banco = sqlite3.connect('banco.db')
cursor = banco.cursor()

create_tblpacientes = """
  CREATE TABLE IF NOT EXISTS TBLPACIENTES (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  NOME TEXT NOT NULL,
  IDADE TEXT NOT NULL,
  TELEFONE TEXT NOT NULL
  );
  """

create_tblmedicos = """
  CREATE TABLE IF NOT EXISTS TBLMEDICOS (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  NOME TEXT NOT NULL,
  CRM TEXT NOT NULL,
  ESPECIALIDADE TEXT NOT NULL
  );
  """

create_tblexames = """
  CREATE TABLE IF NOT EXISTS TBLEXAMES (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  NOME TEXT NOT NULL,
  VALOR REAL NOT NULL
  );
  """


cursor.execute(create_tblpacientes)
cursor.execute(create_tblmedicos)
cursor.execute(create_tblexames)
banco.commit()
banco.close()