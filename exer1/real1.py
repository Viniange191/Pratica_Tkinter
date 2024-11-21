import tkinter as Tk

def soma():
    resultado.set( float(n1.get()) + float(n2.get()))

def multiplique():
    resultado.set( float(n1.get()) * float(n2.get()) )

def divide():
    resultado.set( float(n1.get()) / float(n2.get()) )

def subtraia():
    resultado.set( float(n1.get()) - float(n2.get()))
    



janela = Tk.Tk()
janela.title("Calculadora")

n1 = Tk.Entry()
n1.grid(row=1,column=0)
n2 = Tk.Entry()
n2.grid(row=1,column=1)


resultado = Tk.StringVar()
Tk.Label(janela,textvariable=resultado).grid(row=2,column=0)


somar = Tk.Button(janela,text="Soma", command=soma,width=10,height=3).grid(row=3,column=0,sticky='NSEW')
multiplicar = Tk.Button(janela,text="multiplique", command=multiplique,width=10,height=3).grid(row=3,column=1,sticky='NSEW')
dividir = Tk.Button(janela,text="divide", command=divide,width=10,height=3).grid(row=4,column=0,sticky='NSEW')
subtrair = Tk.Button(janela,text="subtraia", command=subtraia,width=10,height=3).grid(row=4,column=1,sticky='NSEW')
janela.mainloop()