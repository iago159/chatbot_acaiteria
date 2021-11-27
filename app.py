from tkinter import *
from chat import get_response, bot_name


BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 13"
FONT_BOLD = "Helvetica 12 bold"


class Chat_application:

    def __init__(self) -> None:
        self.window = Tk()
        self._setup_main_window()
        first_msg = "Olá, eu sou a Bia. Como posso te ajudar?"
        self._insert_message(first_msg, bot_name)

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=500, height=600, bg=BG_COLOR)

        # cabeçalho
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Bem Vindo", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # pequeno divisor
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # configurações do texto (largura de 20 caracteres, altura, cor, etc)
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=10, pady=5, wrap=WORD)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # barra de rolagem
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        self.bottom_label = Label(
            self.window, bg=BG_GRAY, height=80)
        self.bottom_label.place(relwidth=1, rely=0.825)

        # entrada de texto para enviar mensagem
        self.msg_entry = Entry(self.bottom_label, bg="#2C3E50", fg=TEXT_COLOR,
                               font=FONT, borderwidth=10, relief=FLAT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06,
                             rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # botão de enviar
        send_button = Button(self.bottom_label, text="Enviar", font=FONT_BOLD,
                             width=20, bg="#FFFFFF", command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "Você")

    def _insert_message(self, msg, sender):

        if not msg:
            return

        self.msg_entry.delete(0, END)

        if not sender == bot_name:
            msg_user = f"{sender}: {msg}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg_user)
            self.text_widget.configure(cursor="arrow", state=DISABLED)

            msg_bot = f"{bot_name}: {get_response(msg)}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg_bot)
            self.text_widget.configure(cursor="arrow", state=DISABLED)
        else:
            msg_bot = f"{sender}: {msg}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg_bot)
            self.text_widget.configure(cursor="arrow", state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = Chat_application()
    app.run()
