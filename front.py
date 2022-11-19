from tkinter import *
root = Tk()

def send():
    send = "voce=> "+ e.get()
    txt.insert(END, "\n" + send)
    e.delete(0,END)

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
Button(root, text="enviar", command=send).grid(row=1, column=1)
root.title('chatbot')
root.mainloop()