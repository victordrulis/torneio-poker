import tkinter as tk

class GuiMain():
    """Classe que define a interface gráfica da aplicação
    """
    x_pad = 5
    y_pad = 3
    width_entry = 30


    #Criando a janela...
    window          = tk.Tk()
    window.wm_title("Torneio - Poker")

    #Criando os objetos que estarão na janela...
    btnJogador     = tk.Button(window, text="Jogador")
    btnJogo        = tk.Button(window, text="Jogo")
    btnLocal       = tk.Button(window, text="Local")
    btnClose       = tk.Button(window, text="Fechar")


    #Associando os objetos a grid da janela...
    btnJogador.grid(row=4, column=0, columnspan=2)
    btnJogo.grid(row=5, column=0, columnspan=2)
    btnLocal.grid(row=6, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    #Adicionando um pouco de SWAG a interface...
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')


    def run(self):
        GuiMain.window.mainloop()
