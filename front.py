from tkinter import *

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
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("CHATBOT")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=fundo)

        head_label = Label(self.window, bg=fundo, fg=cor_txt, text="bem vindo", font=negrito, pady=10)
        head_label.place(relwidth=1)

        line = Label(self.window, width=450, bg=cinza)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.text_widget = Text(self.window, width=20, height=2, bg=fundo, fg=cor_txt, font=fonte, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.991)
        scrollbar.configure(command=self.text_widget.yview)

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
        self._insert_message(msg, "voce")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)


front = ChatApplication()
front.run()
