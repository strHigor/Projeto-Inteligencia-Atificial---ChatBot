from tkinter import *
from chatbot import perguntar

cinza = "#abb2b9"
fundo = "#17202a"
cor_txt = "#eaecee"
fonte = "arial 14"
negrito = "arial 14 bold"
 
class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.boas_vindas()
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Helpy")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=850, height=550, bg=fundo)

        head_label = Label(self.window, bg=fundo, fg=cor_txt, text="Helpy v1.0.0", font=negrito, pady=10)
        head_label.place(relwidth=1)

        line = Label(self.window, width=450, bg=cinza)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.text_widget = Text(self.window, width=20, height=2, bg=fundo, fg=cor_txt, font=fonte, padx=10, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        bottom_label = Label(self.window, bg=cinza, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        self.msg_entry = Entry(bottom_label, bg="#2c3e50", fg=cor_txt, font=fonte)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        send_buttom = Button(bottom_label, text="enviar", font=negrito, width=20, bg=cinza,
                             command=lambda: self._on_enter_pressed(None))
        send_buttom.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "\nvoce")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"\n{sender}: {msg}\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f'Helpy: {perguntar(msg)}'
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)
    
    def boas_vindas(self):
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, f'Helpy: Olá, eu sou o Helpy e estou aqui para te ajudar com python.')
        self.text_widget.insert(END, f'\nHelpy: Qual a sua dúvida relacionada á python?')
        self.text_widget.configure(state = DISABLED)

front = ChatApplication()
front.run()