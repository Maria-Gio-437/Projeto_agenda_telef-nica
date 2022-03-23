from tkinter import *
import tkinter as tk


janela = tk.Tk()
janela.iconbitmap('telefone_icon.ico')
janela.title('Agenda')
janela.geometry('1000x600+200+80')
janela.resizable(0, 0)
janela.configure(bg='RoyalBlue3')


# funcoes
def informacao_user():
    nome_recebido = nome.get()
    telefone1 = contato.get()
    telefone2 = contato2.get()
    telefone3 = contato3.get()
    print(nome_recebido, telefone1, telefone2, telefone3)
    


#quadrados brancos/frames
q1 = Label(janela, text='', bg='azure2')
q1.place(x=50, y=150, height=400, width=400)

q2 = Label(janela, text='', bg='azure2')
q2.place(x=500, y=30, height=520, width=450)


#textos
texto_saudacao = Label(janela, font=['Arial', 20, 'bold'], text='AGENDA TELEFÔNICA', bg='lightsteelblue', fg='gray12')
texto_saudacao.place(x=50, y=30, height=100, width=400)

texto_nome = Label(janela, text='Nome', bg='azure2', font=['Helvetica', 14])
texto_nome.place(x=60, y=155)

texto_telefone = Label(janela, text='Telefone', bg='azure2', font=['Helvetica', 14])
texto_telefone.place(x=60, y=250)


#caixas de texto
nome = Entry(janela, font=['Calibri', 16], border=2)
nome.place(x=62, y=185, height=35, width=360)

contato=Entry(janela, font=['Calibri', 16], border=2)
contato.place(x=62, y=280, height=35, width=360)

contato2 = Entry(janela, font=['Calibri', 16], border=2)
contato2.place(x=62, y=340, height=35, width=360)

contato3 = Entry(janela, font=['Calibri', 16], border=2)
contato3.place(x=62, y=400, height=35, width=360)


#botoes
adicionar = Button(janela, text='Adicionar', border=2, bg='gray25', command=informacao_user)
adicionar.place(x=320, y=480, height=30, width=80)

lista = Button(janela, text='Contatos salvos', font=['Calibri', 15], bg='gray25', border=0)
lista.place(x=515, y=50, height=35, width=200)

alterar = Button(janela, text='Alterar contatos', font=['Calibri', 15], bg='gray25', border=0)
alterar.place(x=725, y=50, height=35, width=200)


janela.mainloop()