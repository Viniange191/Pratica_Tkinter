import tkinter as Tk

def fahrenheit():
    celsius = float(num.get())
    ft = ((celsius/5)*9)+32
    resultado.set(ft)
def celsius():
    farhr = float(num.get())
    cs = ((farhr-32)/9)*5
    resultado.set(cs)
janela = Tk.Tk()
janela.title("Convetor")
janela.resizable(False,False)

num = Tk.Entry()
num.grid(column=0,row=0,sticky='NSEW')
fahrenheit = Tk.Button(text="Converter em Fahrenheit", command=fahrenheit).grid(column=0,row=1,sticky='NSEW')
celsius = Tk.Button(text="Converter em Celsius",command=celsius).grid(column=0,row=2,sticky='NSEW')
resultado = Tk.StringVar()
Tk.Label(janela,textvariable=resultado).grid(row=3,column=0)
janela.mainloop()
