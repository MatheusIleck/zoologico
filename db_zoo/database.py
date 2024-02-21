import sqlite3

conexao = sqlite3.connect('zoologico.db')

cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Cpf TEXT not null,
    Senha TEXT NOT NULL
)               
''')

print("Conexão ao banco feita com sucesso!")