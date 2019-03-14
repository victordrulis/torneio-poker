import tkinter as tk

class GuiJogo():
    """Classe que define a interface gráfica da aplicação
    """
    x_pad = 5
    y_pad = 3
    width_entry = 30

    # Criando a janela...
    window = tk.Tk()
    window.wm_title("Poker - Jogo")

    # Criando variáveis que armazenarão o texto inserido pelo usuário...
    txtJogo = tk.StringVar()
    txtJogador = tk.StringVar()
    txtBuyIn = tk.StringVar()
    txtCashOut = tk.StringVar()
    txtSaldo = tk.StringVar()
    txtPontos = tk.StringVar()
    txtRank = tk.StringVar()

    # Criando os objetos que estarão na janela...
    lblLocal = tk.Label(window, text = "Evento/Local")
    lblJogador = tk.Label(window, text = "Jogador")
    lblBuyin = tk.Label(window, text = "BuyIn")
    lblCashOut = tk.Label(window, text = "CashOut")
    lblSaldo = tk.Label(window, text = "Saldo")
    lblPontos = tk.Label(window, text = "Pontos")
    lblRank = tk.Label(window, text = "Rank")
    entJogo = tk.Entry(window, textvariable = txtJogo, width = width_entry)
    entJogador = tk.Entry(window, textvariable = txtJogador, width = width_entry)
    entBuyIn = tk.Entry(window, textvariable = txtBuyIn, width = width_entry)
    entCashOut = tk.Entry(window, textvariable = txtCashOut, width = width_entry)
    entSaldo = tk.Entry(window, textvariable = txtSaldo, width = width_entry)
    entPontos = tk.Entry(window, textvariable = txtPontos, width = width_entry)
    entRank = tk.Entry(window, textvariable = txtRank, width = width_entry)
    listJogo = tk.Listbox(window, width = 100)
    scrollJogo = tk.Scrollbar(window)
    btnViewAll = tk.Button(window, text = "Ver todos")
    btnBuscar = tk.Button(window, text = "Buscar")
    btnInserir = tk.Button(window, text = "Inserir")
    btnUpdate = tk.Button(window, text = "Atualizar Selecionados")
    btnDel = tk.Button(window, text = "Deletar Selecionados")
    btnClose = tk.Button(window, text = "Fechar")

    # Associando os objetos a grid da janela...
    lblLocal.grid(row = 0,column = 0)
    lblJogador.grid(row = 1,column = 0)
    lblBuyin.grid(row = 2,column = 0)
    lblCashOut.grid(row = 3, column = 0)
    lblSaldo.grid(row = 4, column = 0)
    lblPontos.grid(row = 5, column = 0)
    lblRank.grid(row = 6, column = 0)
    entJogo.grid(row=0, column=1, padx = 50, pady = 50)
    entJogador.grid(row = 1, column = 1)
    entBuyIn.grid(row = 2, column = 1)
    entCashOut.grid(row = 3, column = 1)
    entSaldo.grid(row = 4, column = 1)
    entPontos.grid(row = 5, column = 1)
    entRank.grid(row = 6, column = 1)
    listJogo.grid(row = 0, column = 2, rowspan = 10)
    scrollJogo.grid(row = 0, column = 6, rowspan = 10)
    btnViewAll.grid(row = 7, column = 0, columnspan = 2)
    btnBuscar.grid(row = 8, column = 0, columnspan = 2)
    btnInserir.grid(row = 9, column = 0, columnspan = 2)
    btnUpdate.grid(row = 10, column = 0, columnspan = 2)
    btnDel.grid(row = 11, column = 0, columnspan = 2)
    btnClose.grid(row = 12, column = 0, columnspan = 2)

    # buy_in REAL, cash_out REAL, pts REAL, rank INTEGER

    # Associando a Scrollbar com a Listbox...
    listJogo.configure(yscrollcommand=scrollJogo.set)
    scrollJogo.configure(command=listJogo.yview)


    # Adicionando um pouco de SWAG a interface...
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky = 'WE', padx = x_pad, pady = y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx = 0, pady = 0, sticky = 'NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx = 0, pady = 0, sticky = 'NS')
        else:
            child.grid_configure(padx = x_pad, pady = y_pad, sticky = 'N')


    def run(self):
        GuiJogo.window.mainloop()