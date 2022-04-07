import sqlite3

def mostra_dados():
    conexao = sqlite3.connect('mariagio.db')
    cursor = conexao.cursor()
    conexao.commit()
    cursor.execute('''SELECT * FROM agenda_telefonica''')
    dados = cursor.fetchall()
    print(dados)

    return