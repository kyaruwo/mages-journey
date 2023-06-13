def status():
    from main import title, line
    from lib import DB

    (db, c) = DB.connect()
    (atk) = c.execute("").fetchone()
    (lvl, xp, gold) = c.execute("select * from mages").fetchone()
    db.close()

    title()
    print("     atk", atk)
    print("     lvl", lvl)
    print("      xp", xp)
    print("       g", gold)
    line()
    print("     <?> return")
    line()
    input(" >>>> ")
