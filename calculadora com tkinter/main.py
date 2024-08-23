from tkinter import *

janela = Tk()
janela.title("Calculadora ")
janela.resizable(False, False)
janela.geometry('280x480')

def igual():
    segundo_numero = int(visor.get())
    visor.delete(0, END)
    
    if matematica == 'soma':
        visor.insert(0, p_numero + segundo_numero)
    elif matematica == 'sub':
        visor.insert(0, p_numero - segundo_numero)
    elif matematica == 'mult':
        visor.insert(0, p_numero * segundo_numero)

def click_soma():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = 'soma'
    p_numero = int(primeiro_numero)
    visor.delete(0, END)

def click_sub():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = 'sub'
    p_numero = int(primeiro_numero)
    visor.delete(0, END)

def click_mult():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = 'mult'
    p_numero = int(primeiro_numero)
    visor.delete(0, END)

def deletar():
    visor.delete(0, END)


def click_button(numero):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual) + str(numero))

visor = Entry(janela, bg="lightblue")
visor.pack()
#fileira 0
bt0 = Button(janela, text="0", pady=14, padx=14, command = lambda: click_button(0))
bt0.place(x=10, y=45)

#fileira 1
bt1 = Button(janela, text="1", pady=14, padx=14, command = lambda: click_button(1))
bt1.place(x=10, y=100)

bt2 = Button(janela, text="2", pady=14, padx=14, command = lambda: click_button(2))
bt2.place(x=55, y=100)

bt3 = Button(janela, text="3", pady=14, padx=14, command = lambda: click_button(3))
bt3.place(x=100, y=100)

btadicao = Button(janela, text="+", pady=14, padx=14, command = click_soma)
btadicao.place(x=145, y=100)

#fileira 2
bt4 = Button(janela, text="4", pady=14, padx=14, command = lambda: click_button(4))
bt4.place(x=10, y=155)

bt5 = Button(janela, text="5", pady=14, padx=14, command = lambda: click_button(5))
bt5.place(x=55, y=155)

bt6 = Button(janela, text="6", pady=14, padx=14, command = lambda: click_button(6))
bt6.place(x=100, y=155)

btsubtracao = Button(janela, text="-", pady=14, padx=14, command = click_sub)
btsubtracao.place(x=145, y=155)

#fileira 3
bt7 = Button(janela, text="7", pady=14, padx=14, command = lambda: click_button(7))
bt7.place(x=10, y=210)

bt8 = Button(janela, text="8", pady=14, padx=14, command = lambda: click_button(8))
bt8.place(x=55, y=210)
          
bt9 = Button(janela, text="9", pady=14, padx=14, command = lambda: click_button(9))
bt9.place(x=100, y=210)

btmultiplicacao = Button(janela, text="x", pady=14, padx=14, command=click_mult)
btmultiplicacao.place(x=145, y=210)

#fileira 4
btigual = Button(janela, text="=", pady=14, padx= 120, command=igual)
btigual.place(x=10, y=270)

#apagar tudo
btCE = Button(janela, text="CE", pady= 70, padx= 14, command=deletar)
btCE.place(x=200, y=100  )

janela.mainloop()
