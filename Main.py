from GuiMain import *
from GuiJogador import *
from GuiJogo import *
from GuiLocal import *

import Backend as core

app = None
appJogador = None
appJogo = None
appLocal = None

def jogadorCommand():
    appJogador.run()

def jogoCommand():
    appJogo.run()

def localCommand():
    appLocal.run()

if __name__ == "__main__":
    app = GuiMain()
    appJogador = GuiJogador()
    appJogo = GuiJogo()
    appLocal = GuiLocal()

    app.btnJogador.configure(command = jogadorCommand)
    app.btnJogo.configure(command = jogoCommand)
    app.btnLocal.configure(command = localCommand)
    app.btnClose.configure(command = app.window.destroy)
    app.run()
