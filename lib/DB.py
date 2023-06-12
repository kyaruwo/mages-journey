gamedata = "game.dat"


def connect():
    import sqlite3

    db = sqlite3.connect(gamedata)
    c = db.cursor()
    return (db, c)
