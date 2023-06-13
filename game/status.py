def status():
    from main import line
    from lib import DB

    (db, c) = DB.connect()
    (atk) = c.execute("").fetchone()
    (lvl, xp, gold) = c.execute("select * from mages").fetchone()
    db.close()

    line()
    print((8 * " ") + "STATUS")
    line()
    print("     atk", atk)
    print("     lvl", lvl)
    print("      xp", xp)
    print("       g", gold)
    line()
    print("     <?> return")
    line()
    input(" >>>> ")
