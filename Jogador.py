# from GuiMain import *
# from GuiJogo import *
from GuiJogador import *
# from GuiLocal import *
import Backend as core

app = None
entidade = "jogador"

def view_command():
    rows = core.viewJogador()
    app.listJogador.delete(0, tk.END)
    for r in rows:
        app.listJogador.insert(tk.END, r)

def search_command():
    app.listJogador.delete(0, tk.END)
    rows = core.searchJogador(app.txtNome.get(), app.txtSobrenome.get())
    for r in rows:
        app.listJogador.insert(tk.END, r)

def insert_command():
    core.insertJogador(app.txtNome.get(), app.txtSobrenome.get())
    view_command()

def update_command():
    core.updateJogador(selected[0],app.txtNome.get(),app.txtSobrenome.get())
    view_command()

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()


def getSelectedRow(event):
    global selected
    index = app.listJogador.curselection()
    selected = app.listJogador.get(index)
    app.entNome.delete(0, tk.END)
    app.entNome.insert(tk.END, selected[1])
    app.entSobrenome.delete(0, tk.END)
    app.entSobrenome.insert(tk.END, selected[2])
    return selected


if __name__ == "__main__":
    app = GuiJogador()
    app.listJogador.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()
