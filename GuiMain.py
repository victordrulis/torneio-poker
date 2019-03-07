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


    #Criando variáveis que armazenarão o texto inserido pelo usuário...
    txtNome         = tk.StringVar()
    txtSobrenome    = tk.StringVar()
    txtEmail        = tk.StringVar()
    txtCPF          = tk.StringVar()


    #Criando os objetos que estarão na janela...
    lblnome        = tk.Label(window, text="Nome")
    lblsobrenome   = tk.Label(window, text="Sobrenome")
    lblemail       = tk.Label(window, text="Email")
    lblcpf         = tk.Label(window, text="CPF")
    entNome        = tk.Entry(window, textvariable=txtNome, width=width_entry)
    entSobrenome   = tk.Entry(window, textvariable=txtSobrenome, width=width_entry)
    entEmail       = tk.Entry(window, textvariable=txtEmail, width=width_entry)
    entCPF         = tk.Entry(window, textvariable=txtCPF, width=width_entry)
    listClientes   = tk.Listbox(window, width=100)
    scrollClientes = tk.Scrollbar(window)
    btnViewAll     = tk.Button(window, text="Ver todos")
    btnBuscar      = tk.Button(window, text="Buscar")
    btnInserir     = tk.Button(window, text="Inserir")
    btnUpdate      = tk.Button(window, text="Atualizar Selecionados")
    btnDel         = tk.Button(window, text="Deletar Selecionados")
    btnClose       = tk.Button(window, text="Fechar")


    #Associando os objetos a grid da janela...
    lblnome.grid(row=0,column=0)
    lblsobrenome.grid(row=1,column=0)
    lblemail.grid(row=2,column=0)
    lblcpf.grid(row=3, column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)
    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)



    #Associando a Scrollbar com a Listbox...
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)


    #Adicionando um pouco de SWAG a interface...
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')




    def run(self):
        GuiMain.window.mainloop()
