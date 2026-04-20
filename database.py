import sqlite3

def get_conn():
    conn = sqlite3.connect("torneo.db")
    return conn

def init_db():
    conn = get_conn()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS inscritos(
            id        INTEGER PRIMARY KEY,
            nombre    TEXT NOT NULL,
            correo    TEXT NOT NULL,
            invocador TEXT NOT NULL,
            rango     TEXT NOT NULL,
            equipo    TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()