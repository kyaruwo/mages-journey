import sqlite3

gamedata = "game.dat"


def connect():
    db = sqlite3.connect(gamedata)
    c = db.cursor()
    return (db, c)
