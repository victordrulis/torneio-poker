# from GuiMain import *
# from GuiJogo import *
from GuiLocal import *
# from GuiLocal import *
import Backend as core

app = None
entidade = 'local'

def view_command():
    rows = core.viewLocal()
    app.listLocal.delete(0, tk.END)
    for r in rows:
        app.listLocal.insert(tk.END, r)

def search_command():
    app.listLocal.delete(0, tk.END)
    rows = core.searchLocal(app.txtNome.get(), app.txtData.get())
    for r in rows:
        app.listLocal.insert(tk.END, r)

def insert_command():
    core.insertLocal(app.txtNome.get(), app.txtData.get(), app.txtQtde.get())
    view_command()

def update_command():
    core.updateLocal(selected[0],app.txtNome.get(), app.txtData.get(), app.txtQtde.get())
    view_command()

def del_command():
    id = selected[0]
    core.deleteLocal(id)
    view_command()

def getSelectedRow(event):
    global selected
    index = app.listLocal.curselection()[0]
    selected = app.listLocal.get(index)
    app.entNome.delete(0, tk.END)
    app.entNome.insert(tk.END, selected[1])
    app.entData.delete(0, tk.END)
    app.entData.insert(tk.END, selected[2])
    app.entQtde.delete(0, tk.END)
    app.entQtde.insert(tk.END, selected[3])
    return selected


if __name__ == "__main__":
    app = GuiLocal()
    app.listLocal.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()
