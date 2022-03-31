from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3

janela = tk.Tk()
janela.iconbitmap('telefone_icon.ico')
janela.title('Agenda')
janela.geometry('1000x600+200+80')
janela.resizable(0, 0)
janela.configure(bg='RoyalBlue3')


#banco de dados
def bd():
    global usuario, telefone1, telefone2, telefone3
    usuario = str(nome.get())
    telefone1 = str(contato.get())
    telefone2 = str(contato2.get())
    telefone3 = str(contato3.get())


    #conectar bd
    conexao = sqlite3.connect('mariagio')
    cursor = conexao.cursor()

    #criar self.tabela
    cursor.execute('''CREATE TABLE IF NOT EXISTS agenda_telefonica(
        IP INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT(26) NOT NULL,
        Tel_1 BIGINT(11)NOT NULL,
        Tel_2 BIGINT(11),
        Tel_3 BIGINT(11)
    )''')
    cursor.execute(f'''INSERT INTO agenda_telefonica(Nome, Tel_1, Tel_2, Tel_3) VALUES ('{usuario}',' {telefone1}', '{telefone2}', '{telefone3}')''')
    dados = cursor.execute('SELECT * FROM agenda_telefonica')
    print(dados)

    conexao.commit()
    print(usuario, telefone1, telefone2, telefone3)

    #desconectar bd
    conexao.close()



def lista_cont_salvo():
    lista_cont_salvos = ttk.Treeview(frame2, columns=["colu_nome", "colu_tel", "colu_tel2", "colu_tel3"])
    lista_cont_salvos.heading("#0", text='Nome')
    lista_cont_salvos.heading("#1", text='Telefone')
    lista_cont_salvos.heading("#2", text='Telefone 2')
    lista_cont_salvos.heading("#3", text='Telefone 3')
    lista_cont_salvos.column("#0", width=95)
    lista_cont_salvos.column("#1", width=95)
    lista_cont_salvos.column("#2", width=95)
    lista_cont_salvos.column("#3", width=95)
    lista_cont_salvos.place(x=24, y=74, width=401, height=420)

    rolagem = Scrollbar(frame2, orient='vertical')
    lista_cont_salvos.configure(yscroll=rolagem.set)
    rolagem.place(x=401, y=75, width=25, height=420)

    bd()
    informacoes = ['Maria Giovanna', '64992042732']
    lista_cont_salvos.insert('', END, values=informacoes)


def limpa_dados():
    nome.delete(0, END)
    contato.delete(0, END)
    contato2.delete(0, END)
    contato3.delete(0, END)


# frames
frame1 = Frame(janela, bg='azure2')
frame1.place(x=50, y=150, height=400, width=400)

frame2 = Frame(janela, bg='azure2')
frame2.place(x=500, y=30, height=520, width=450)

frame_contatos_salvos = Frame(frame2, bg='mintcream', border=2, highlightbackground='gray25', highlightthickness=4)
frame_contatos_salvos.place(x=20, y=70, height=430, width=410)

# caixas de texto
texto_saudacao = Label(janela, font=['Arial', 20, 'bold'], text='AGENDA TELEFÔNICA', bg='lightsteelblue', fg='gray12')
texto_saudacao.place(x=50, y=30, height=100, width=400)

texto_nome = Label(janela, text='Nome', bg='azure2', font=['Helvetica', 14])
texto_nome.place(x=60, y=155)

texto_telefone = Label(janela, text='Telefone', bg='azure2', font=['Helvetica', 14])
texto_telefone.place(x=60, y=250)

# caixas de entrada
nome = Entry(janela, font=['Calibri', 16], border=2)
nome.place(x=62, y=185, height=35, width=360)

contato = Entry(janela, font=['Calibri', 16], border=2)
contato.place(x=62, y=280, height=35, width=360)

contato2 = Entry(janela, font=['Calibri', 16], border=2)
contato2.place(x=62, y=340, height=35, width=360)

contato3 = Entry(janela, font=['Calibri', 16], border=2)
contato3.place(x=62, y=400, height=35, width=360)

# botoes
limpar = Button(janela, text='Limpar', border=2, bg='gray25', command=limpa_dados)
limpar.place(x=220, y=480, height=30, width=80)

adicionar = Button(janela, text='Adicionar', border=2, bg='gray25', command=bd)
adicionar.place(x=320, y=480, height=30, width=80)

lista = Button(janela, text='Contatos salvos', font=['Calibri', 15], bg='gray25', border=0, command=lista_cont_salvo)
lista.place(x=520, y=50, height=35, width=200)

alterar = Button(janela, text='Alterar contatos', font=['Calibri', 15], bg='gray25', border=0)
alterar.place(x=730, y=50, height=35, width=200)

janela.mainloop()