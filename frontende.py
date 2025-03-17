co0 ='#F8F8F2'
co1 ='#D5D8E4'
co2 ='#519ABA'
co3 ='#FF79C6'
co4 ='#33C481'
# cores
from back import*
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
import requests
import json


    

# inicio
janela= Tk()
janela.title('CEP Facil')
janela.geometry('900x600')
janela.configure(background= co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')
# divisão da interface
frame_cima = Frame(janela, width=1061, height=60, bg=co0, relief='flat')
frame_cima.grid(row=0, column=0)

frame_meio = Frame(janela, width=1043, height=350, bg=co0, pady=20, relief='raised')
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=1045, height=450, bg=co0, relief='flat')
frame_baixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)
# imagem inicial
img_logo = Image.open('cep.png')
img_logo = img_logo.resize((60,50))
img_logo = ImageTk.PhotoImage(img_logo)

app_logo = Label(frame_cima, image=img_logo, text=' Consuta CEP', width=900, compound=LEFT, padx=5, relief=RAISED,anchor=NW, font=('Verdana 20 bold') )
app_logo.place(x=0, y=0)
# criar botoes
l_digita = Label(frame_meio, text= 'Digite o cep:', height=1, anchor=NW, font='Ivy 13 bold', bg=co0)
l_digita.place(x=10, y=100)
e_digita = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_digita.place(x=130,y=101)

def pes():
    var = e_digita.get()
    CWP = var 

    requisicao= requests.get(F"https://cep.awesomeapi.com.br/json/{CWP}")
    dict_ = requisicao.json()

    cidade = dict_['city']
    rua = dict_['address']
    uf = dict_['state']
    bairro = dict_['district']
    ddd = dict_['ddd']
    latit = dict_['lat']

    
    
    

    l_cidade = Label(frame_meio, text= 'CIDADE:', height=1, anchor=NW, font='Ivy 10 bold', bg=co0)
    l_cidade.place(x=330, y=40)
    e_cidade = Label(frame_meio, text=cidade, width=30, justify='left', relief=SOLID)
    e_cidade.place(x=389,y=41)

    l_rua = Label(frame_meio, text= 'RUA:', height=1, anchor=NW, font='Ivy 10 bold', bg=co0)
    l_rua.place(x=351, y=70)
    e_rua = Label(frame_meio, text=rua, width=30, justify='left', relief=SOLID)
    e_rua.place(x=389,y=71)

    l_bairro = Label(frame_meio, text= 'BAIRRO:', height=1, anchor=NW, font='Ivy 10 bold', bg=co0)
    l_bairro.place(x=330, y=100)
    e_bairro = Label(frame_meio, text=bairro, width=30, justify='left', relief=SOLID)
    e_bairro.place(x=389,y=101)

    l_uf = Label(frame_meio, text= 'UF:', height=1, anchor=NW, font='Ivy 10 bold', bg=co0)
    l_uf.place(x=363, y=130)
    e_uf = Label(frame_meio, text=uf, width=30, justify='left', relief=SOLID)
    e_uf.place(x=389,y=131)

    l_lat = Label(frame_meio, text= 'LATITUDE:', height=1, anchor=NW, font='Ivy 10 bold', bg=co0)
    l_lat.place(x=317, y=160)
    e_lat = Label(frame_meio, text=latit, width=30, justify='left', relief=SOLID)
    e_lat.place(x=389,y=161)

    l_ddd = Label(frame_meio, text= 'DDD:', height=1, anchor=NW, font='Ivy 10 bold', bg=co0)
    l_ddd.place(x=353, y=190)
    e_ddd = Label(frame_meio, text=ddd, width=30, justify='left', relief=SOLID)
    e_ddd.place(x=389,y=191)
    #limpar
    def limp():
        e_cidade.config(text='')
        e_rua.config(text='')
        e_uf.config(text='')
        e_bairro.config(text='')
        e_lat.config(text='')
        e_ddd.config(text='')
        e_digita.delete(0,'end')
        b_limpa.destroy()


    b_limpa = Button(frame_meio,command=limp, width=30,  text='Limpar', compound=LEFT, anchor=CENTER, overrelief=RIDGE, font='Ivy 10', bg=co2, fg=co0)
    b_limpa.place(x=103, y=10)
    
    
b_pesquisar = Button(frame_meio,command=pes, width=30,  text='Pesquisar o Endereço', compound=LEFT, anchor=CENTER, overrelief=RIDGE, font='Ivy 10', bg='#DCDAD5', fg='#0096EE')
b_pesquisar.place(x=103, y=10)







janela.mainloop()
