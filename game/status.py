def magestats():
    from lib import DB

    (db, c) = DB.connect()

    (lvl, xp, gold) = c.execute("select * from mages").fetchone()

    hp = int(6 + lvl)

    baseatk = int(3 + lvl)
    (atk) = c.execute(
        """
    select sum(atk*count)
    from inventory join market
    on itemid = market.ROWID
        """
    ).fetchone()[0]
    if atk != None:
        atk += baseatk
    else:
        atk = baseatk

    db.close()

    return (lvl, xp, gold, hp, atk)


def status():
    from main import line

    (lvl, xp, gold, hp, atk) = magestats()

    line()
    print((8 * " ") + "STATUS")
    line()
    print("     lvl", lvl)
    print("      xp", xp)
    print("       g", gold)
    print("      hp", hp)
    print("     atk", atk)
    line()
    print("     <?> return")
    line()
    input(" >>>> ")
