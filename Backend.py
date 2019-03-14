import sqlite3 as sql

class TransactionObject():
    database    = "torneio-poker.db"
    conn        = None
    cur         = None
    connected   = False

    def connect(self):
        TransactionObject.conn      = sql.connect(TransactionObject.database)
        TransactionObject.cur       = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False


def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS jogador (id INTEGER PRIMARY KEY , nome TEXT, sobrenome TEXT)")
    trans.persist()
    trans.execute("CREATE TABLE IF NOT EXISTS local (id INTEGER PRIMARY KEY , nome TEXT, data TEXT, qtd_jogadores INTEGER)")
    trans.persist()
    trans.execute("CREATE TABLE IF NOT EXISTS jogo (id INTEGER PRIMARY KEY , jogador_id INTEGER, local_id INTEGER, buy_in REAL, cash_out REAL, pts REAL, rank INTEGER)")
    trans.persist()
    trans.disconnect()

def insertJogador(nome, sobrenome):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO jogador VALUES(NULL, ?, ?)", (nome, sobrenome))
    trans.persist()
    trans.disconnect()

def insertJogo(jogador_id, local_id, buy_in):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO jogo VALUES(NULL, ?, ?, ?)", (jogador_id, local_id, buy_in))
    trans.persist()
    trans.disconnect()

def insertLocal(nome, data, qtd_jogadores):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO local VALUES(NULL, ?, ?, ?)", (nome, data, qtd_jogadores))
    trans.persist()
    trans.disconnect()

def updateJogador(id, nome, sobrenome):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE jogador SET nome = ?, sobrenome = ? WHERE id = ?", (nome, sobrenome, id))
    trans.persist()
    trans.disconnect()

def updateJogo(id, jogador_id, local_id, buy_in, cash_out, pts, rank):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE jogo SET jogador_id = ?, local_id = ?, buy_in = ?, cash_out = ?, pts = ?, rank = ? WHERE id = ?", (jogador_id, local_id, buy_in, cash_out, pts, rank, id))
    trans.persist()
    trans.disconnect()

def updateLocal(id, nome, data, qtd_jogadores):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE local SET nome = ?, data = ?, qtd_jogadores = ? WHERE id = ?", (nome, data, qtd_jogadores, id))
    trans.persist()
    trans.disconnect()

def viewJogador():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM jogador")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def viewJogo():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM jogo")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def viewLocal():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM local")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def searchJogador(id = 0, nome = "", sobrenome = ""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM jogador WHERE id = ? or nome LIKE ? or sobrenome LIKE ?", (id, nome, sobrenome))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def searchJogo(id = 0, nome = "", sobrenome = ""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM jogo WHERE id = ? or nome LIKE ? or sobrenome LIKE ?", (id, nome, sobrenome))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def searchLocal(id = 0, nome = "", data = "", idLocal = 0):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM local WHERE id = ? or nome LIKE ? or data BETWEEN ? AND date('now')", (id, nome, data))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def deleteJogador(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM jogador WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

def deleteLocal(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM local WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

def deleteJogo(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM jogo WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

def classificar(idLocal):
    # jogadores[] = searchJogador
    # sorted(student_tuples, key=lambda student: student[2])   # sort por saldo
    print("Ola")

def calculaPontosJogadores(idLocal):
    pontuacao = ((qtdJogadores - classificacao) + (saldo/4))

initDB()
