import tkinter as inicio

def submit():
    if name_var.get() != "":
        name = name_var.get()
        name_var.set("")
        master.destroy()

def show_entry_fields():
    print(e1.get())

master = inicio.Tk()
master.title('Helpy')
master.eval('tk::PlaceWindow . center')
master.resizable(False, False)

name_var = inicio.StringVar()

inicio.Label(master, text='Qual o seu nome?').grid(row=0)

e1 = inicio.Entry(master, textvariable = name_var, width=40)

e1.grid(row=1, padx=5, pady=5)

inicio.Button(master, 
          text='Continuar', 
          command=submit, width=12).grid(row=2)

inicio.mainloop()