import tkinter as Tk
def adicionar_tarefa():
    adc = adicao.get()
    if adc != "":
        lista_tarefa.insert(Tk.END,adc)
        adicao.delete(0,Tk.END)
def remover_tarefa():
    try:
        indice = lista_tarefa.curselection()[0]
        lista_tarefa.delete(indice)
    except:
        pass
janela =Tk.Tk()
janela.title("Tarefas")
janela.resizable(False,False)
adicao = Tk.Entry()
adicao.grid(row=0,column=0,sticky='NSEW')

adicionar = Tk.Button(text="Adicionar",command=adicionar_tarefa)
adicionar.grid(column=0,row=1,sticky='NSEW')
remover = Tk.Button(text="remover",command=remover_tarefa)
remover.grid(column=0,row=2,sticky='NSEW')
lista_tarefa = Tk.Listbox(width=40,height=9)
lista_tarefa.grid(column=0,row=3)
janela.mainloop()