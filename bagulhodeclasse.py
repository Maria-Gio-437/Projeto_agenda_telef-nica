import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

azul = 'Royalblue3'

class Agenda:
    def __init__(self):
        self.Template()
        self.Frames()
        self.Labels()
        self.Entradas()
        self.Botao()

    def Template(self):
        self.janela=tk.Tk()
        self.janela.geometry('1000x600+200+50')
        self.janela.title('Agenda Telefônica')
        self.janela.configure(bg=azul)
        self.janela.resizable(0, 0)
        self.janela.iconbitmap('telefone_icon.ico')

        self.conexao = sqlite3.connect('mariagio.db')
        self.cursor = self.conexao.cursor()
        self.conexao.commit()
        self.cursor.execute('''SELECT * FROM agenda_telefonica''')
        dados = self.cursor.fetchall()
        print(dados)

    def Frames(self):
        self.frame0 = tk.Frame(self.janela, bg='lightsteelblue')
        self.frame0.place(x=50, y=30, height=100, width=400)

        self.frame1 = tk.Frame(self.janela, bg='azure2')
        self.frame1.place(x=50, y=150, height=400, width=400)

        self.frame2 = tk.Frame(self.janela, bg='azure2')
        self.frame2.place(x=500, y=30, height=520, width=450)

        self.frame_base = tk.Frame(self.frame2, bg='mintcream', border=2, highlightbackground='gray25', highlightthickness=4)
        self.frame_base.place(x=20, y=70, height=430, width=410)

        self.frame_lista = tk.Frame(self.frame_base, bg='mintcream', border=2, highlightbackground='gray25', highlightthickness=4)
        self.frame_lista.place(x=-6, y=-6, height=430, width=410)

        self.frame_modificar = tk.Frame(self.frame_base, bg='mintcream', border=2, highlightbackground='gray25', highlightthickness=4)
        self.frame_modificar.place(x=-6, y=-6, height=430, width=410)

    def Labels(self):
        self.texto_saudacao = tk.Label(self.frame0, font=['Arial', 20, 'bold'], text='AGENDA TELEFÔNICA', bg='lightsteelblue', fg='gray12')
        self.texto_saudacao.place(x=45, y=30)

        self.texto_nome = tk.Label(self.janela, text='Nome', bg='azure2', font=['Helvetica', 14])
        self.texto_nome.place(x=60, y=155)

        self.texto_telefone = tk.Label(self.janela, text='Telefone', bg='azure2', font=['Helvetica', 14])
        self.texto_telefone.place(x=60, y=250)

        self.texto_nome_modifica = tk.Label(self.frame_modificar, text='Selecione o nome:', bg='mintcream', font=['Helvetica', 14])
        self.texto_nome_modifica.place(x=10, y=10)

        self.texto_novo_nome_modifica = tk.Label(self.frame_modificar, text='Novo nome:', bg='mintcream', font=['Helvetica', 14])
        self.texto_novo_nome_modifica.place(x=10, y=50)

        self.texto_novo_cont_modifica = tk.Label(self.frame_modificar, text='Novo telefone:', bg='mintcream', font=['Helvetica', 14])
        self.texto_novo_cont_modifica.place(x=10, y=100)

    def Entradas(self):
        self.nome = tk.Entry(self.janela, font=['Calibri', 16], border=2)
        self.nome.place(x=62, y=185, height=35, width=360)

        self.contato = tk.Entry(self.janela, font=['Calibri', 16], border=2)
        self.contato.place(x=62, y=280, height=35, width=360)

        self.contato2 = tk.Entry(self.janela, font=['Calibri', 16], border=2)
        self.contato2.place(x=62, y=340, height=35, width=360)

        self.contato3 = tk.Entry(self.janela, font=['Calibri', 16], border=2)
        self.contato3.place(x=62, y=400, height=35, width=360)

        self.nome_modifica = tk.Entry(self.frame_modificar, font=['Calibri', 14], border=1)
        self.nome_modifica.place(x=180, y=10, height=30, width=200)

        self.novo_nome_modifica = tk.Entry(self.frame_modificar, font=['Calibri', 14], border=1)
        self.novo_nome_modifica.place(x=120, y=55, height=30, width=260)

        self.cont_modifica = tk.Entry(self.frame_modificar, font=['Calibri', 14], border=1)
        self.cont_modifica.place(x=150, y=100, height=30, width=200)

        self.cont2_modifica = tk.Entry(self.frame_modificar, font=['Calibri', 14], border=1)
        self.cont2_modifica.place(x=150, y=150, height=30, width=200)

        self.cont3_modifica = tk.Entry(self.frame_modificar, font=['Calibri', 14], border=1)
        self.cont3_modifica.place(x=150, y=200)

    def Botao(self):
        self.adicionar = tk.Button(self.janela, text='Adicionar', border=2, bg='gray25', command=self.conecta_Bd)
        self.adicionar.place(x=320, y=480, height=30, width=80)

        self.lista = tk.Button(self.janela, text='Contatos salvos', font=['Calibri', 15], bg='gray25', border=0, command=self.Tabela)
        self.lista.place(x=520, y=50, height=35, width=200)

        self.modificar = tk.Button(self.janela, text='Modificar contatos', font=['Calibri', 15], bg='gray25', border=0, command=self.destruir_frame_lista)
        self.modificar.place(x=730, y=50, height=35, width=200)

        self.deletar_dados = tk.Button(self.frame_modificar, text='Deletar', border=2, bg='gray25', command=self.Deletar)
        self.deletar_dados.place(x=150, y=300, height=30, width=80)

        self.alterar_dados = tk.Button(self.frame_modificar, text='Alterar', border=2, bg='gray25', command=self.ALterar)
        self.alterar_dados.place(x=280, y=300, height=30, width=80)

    def conecta_Bd(self):
        self.valor1 = self.nome.get()
        self.valor2 = self.contato.get()
        self.valor3 = self.contato2.get()
        self.valor4 = self.contato3.get()

        self.conexao = sqlite3.connect('mariagio.db')
        self.cursor = self.conexao.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS agenda_telefonica(
            IP INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT(26) NOT NULL,
            Tel_1 BIGINT(11)NOT NULL,
            Tel_2 BIGINT(11),
            Tel_3 BIGINT(11)
        )''')
        self.cursor.execute(f'''INSERT INTO agenda_telefonica(Nome, Tel_1, Tel_2, Tel_3) VALUES ('{self.valor1}',' {self.valor2}', '{self.valor3}', '{self.valor4}')''')
        self.cursor.execute('''SELECT * FROM agenda_telefonica''')
        #self.cursor.execute('''DROP TABLE agenda_telefonica''')

        self.conexao.commit()

        #desconecta bd
        self.nome.delete(0, tk.END)
        self.contato.delete(0, tk.END)
        self.contato2.delete(0, tk.END)
        self.contato3.delete(0, tk.END)
        self.Tabela()

    def Tabela(self):
        if self.frame_modificar.winfo_exists() == 1:
            self.frame_modificar.destroy()

        self.frame_lista = tk.Frame(self.frame_base, bg='mintcream', border=2, highlightbackground='gray25', highlightthickness=4)
        self.frame_lista.place(x=-6, y=-6, height=430, width=410)

        self.tabela = ttk.Treeview(self.frame_lista, columns=['col_nome', 'col_cont', 'col_cont2', 'col_cont3'], show='headings')
        self.tabela.column('col_nome', minwidth=0, width=87)
        self.tabela.column('col_cont', minwidth=0, width=87)
        self.tabela.column('col_cont2', minwidth=0, width=87)
        self.tabela.column('col_cont3', minwidth=0, width=87)
        self.tabela.heading('col_nome', text='Nome')
        self.tabela.heading('col_cont', text='Telefone')
        self.tabela.heading('col_cont2', text='Telefone 2')
        self.tabela.heading('col_cont3', text='Telefone 3')

        self.conexao = sqlite3.connect('mariagio.db')
        self.cursor = self.conexao.cursor()

        mostrar = self.cursor.execute('''SELECT Nome, Tel_1, Tel_2, Tel_3 FROM agenda_telefonica''')
        self.conexao.commit()
        c = 0
        for i in mostrar:
            self.tabela.insert(parent='', index='end', iid=c, text='poha', values=(i))
            c += 1

        self.tabela.place(x=-3, y=-3, height=423, width=385)

        self.rolagem = ttk.Scrollbar(self.frame_lista, orient='vertical')
        self.tabela.configure(yscroll=self.rolagem.set)
        self.rolagem.place(x=382, y=-3, width=17, height=420)

        #mostra dados na tabela
        
    def destruir_frame_lista(self):
        if self.frame_lista.winfo_exists() == 1:
            self.frame_lista.destroy()

        self.frame_modificar = tk.Frame(self.frame_base, bg='mintcream', border=2, highlightbackground='gray25', highlightthickness=4)
        self.frame_modificar.place(x=-6, y=-6, height=430, width=410)

        self.nome_modifica = tk.Entry(self.frame_modificar, font=['Calibri', 14], border=1)
        self.nome_modifica.place(x=180, y=10, height=30, width=200)
        self.novo_nome_modifica = tk.Entry(self.frame_modificar, font=['Calibri', 14], border=1)
        self.novo_nome_modifica.place(x=120, y=55, height=30, width=260)
        self.cont_modifica = tk.Entry(self.frame_modificar, font=['Calibri', 14], border=1)
        self.cont_modifica.place(x=150, y=100, height=30, width=200)
        self.cont2_modifica = tk.Entry(self.frame_modificar, font=['Calibri', 14], border=1)
        self.cont2_modifica.place(x=150, y=150, height=30, width=200)
        self.cont3_modifica = tk.Entry(self.frame_modificar, font=['Calibri', 14], border=1)
        self.cont3_modifica.place(x=150, y=200)

        self.texto_nome_modifica = tk.Label(self.frame_modificar, text='Selecione o nome:', bg='mintcream', font=['Helvetica', 14])
        self.texto_nome_modifica.place(x=10, y=10)
        self.texto_novo_nome_modifica = tk.Label(self.frame_modificar, text='Novo nome:', bg='mintcream', font=['Helvetica', 14])
        self.texto_novo_nome_modifica.place(x=10, y=50)
        self.texto_novo_cont_modifica = tk.Label(self.frame_modificar, text='Novo telefone:', bg='mintcream', font=['Helvetica', 14])
        self.texto_novo_cont_modifica.place(x=10, y=100)

        self.deletar_dados = tk.Button(self.frame_modificar, text='Deletar', border=2, bg='gray25', command=self.Deletar)
        self.deletar_dados.place(x=150, y=300, height=30, width=80)
        self.alterar_dados = tk.Button(self.frame_modificar, text='Alterar', border=2, bg='gray25', command=self.ALterar)
        self.alterar_dados.place(x=280, y=300, height=30, width=80)
        
    def Deletar(self):
        self.nome_excluido = self.nome_modifica.get()

        self.conexao = sqlite3.connect('mariagio.db')
        self.cursor = self.conexao.cursor()

        self.cursor.execute(f''' DELETE FROM agenda_telefonica WHERE Nome='{self.nome_excluido}' ''')
        self.conexao.commit()

        self.nome_modifica.delete(0, tk.END)

    def ALterar(self):
        self.nome_tabela = self.nome_modifica.get()
        self.nome_alterado = self.novo_nome_modifica.get()
        self.tel1_alterado = self.cont_modifica.get()
        self.tel2_alterado = self.cont2_modifica.get()
        self.tel3_alterado = self.cont3_modifica.get()

        self.conexao = sqlite3.connect('mariagio.db')
        self.cursor = self.conexao.cursor()

        self.cursor.execute(f''' UPDATE agenda_telefonica SET Nome='{self.nome_alterado}', Tel_1='{self.tel1_alterado}', Tel_2='{self.tel2_alterado}', Tel_3='{self.tel3_alterado}' WHERE Nome='{self.nome_tabela}' ''')
        self.conexao.commit()

        self.nome_modifica.delete(0, tk.END)
        self.novo_nome_modifica.delete(0, tk.END)
        self.cont_modifica.delete(0, tk.END)
        self.cont2_modifica.delete(0, tk.END)
        self.cont3_modifica.delete(0, tk.END)

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    windows = Agenda()
    windows.run()