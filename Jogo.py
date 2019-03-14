from GuiJogo import *
import Backend as core

app = None
entidade = 'jogo'

def view_command():
    rows = core.viewJogo()
    app.listJogo.delete(0, tk.END)
    for r in rows:
        app.listJogo.insert(tk.END, r)

def search_command():
    app.listJogo.delete(0, tk.END)
    rows = core.searchJogo(app.txtNome.get(), app.txtData.get())
    for r in rows:
        app.listJogo.insert(tk.END, r)

def insert_command():
    core.insertJogo(app.txtNome.get(), app.txtData.get(), app.txtQtde.get())
    view_command()

def update_command():
    core.updateJogo(selected[0],app.txtNome.get(), app.txtData.get(), app.txtQtde.get())
    view_command()

def del_command():
    id = selected[0]
    core.deleteJogo(id)
    view_command()

def getSelectedRow(event):
    global selected
    index = app.listJogo.curselection()[0]
    selected = app.listJogo.get(index)
    app.entNome.delete(0, tk.END)
    app.entNome.insert(tk.END, selected[1])
    app.entData.delete(0, tk.END)
    app.entData.insert(tk.END, selected[2])
    app.entQtde.delete(0, tk.END)
    app.entQtde.insert(tk.END, selected[3])
    return selected


if __name__ == "__main__":
    app = GuiJogo()
    app.listJogo.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()
