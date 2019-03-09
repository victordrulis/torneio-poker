import tkinter as tk
import tkinter as tk

class GuiLocal():
    """Classe que define a interface gráfica da aplicação
    """
    x_pad = 5
    y_pad = 3
    width_entry = 30


    #Criando a janela...
    window          = tk.Tk()
    window.wm_title("Cadastro de Local")


    #Criando variáveis que armazenarão o texto inserido pelo usuário...
    txtNome         = tk.StringVar()
    txtData        = tk.StringVar()
    txtQtde          = tk.StringVar()


    #Criando os objetos que estarão na janela...
    lblnome        = tk.Label(window, text="Nome")
    lblemail       = tk.Label(window, text="Data")
    lblqtde         = tk.Label(window, text="Qtde Jogadores")
    entNome        = tk.Entry(window, textvariable=txtNome, width=width_entry)
    entData       = tk.Entry(window, textvariable=txtData, width=width_entry)
    entQtde         = tk.Entry(window, textvariable=txtQtde, width=width_entry)
    listLocal   = tk.Listbox(window, width=100)
    scrollLocal = tk.Scrollbar(window)
    btnViewAll     = tk.Button(window, text="Ver todos")
    btnBuscar      = tk.Button(window, text="Buscar")
    btnInserir     = tk.Button(window, text="Inserir")
    btnUpdate      = tk.Button(window, text="Atualizar Selecionados")
    btnDel         = tk.Button(window, text="Deletar Selecionados")
    btnClose       = tk.Button(window, text="Fechar")


    #Associando os objetos a grid da janela...
    lblnome.grid(row=0,column=0)
    lblemail.grid(row=2,column=0)
    lblqtde.grid(row=3, column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50)
    entData.grid(row=2, column=1)
    entQtde.grid(row=3, column=1)
    listLocal.grid(row=0, column=2, rowspan=10)
    scrollLocal.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)



    #Associando a Scrollbar com a Listbox...
    listLocal.configure(yscrollcommand=scrollLocal.set)
    scrollLocal.configure(command=listLocal.yview)


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
        GuiLocal.window.mainloop()
