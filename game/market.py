def line():
    from main import line

    line(48)


def title():
    line()
    print((21 * " ") + "MARKET")
    line()


def showitems(items):
    title()
    print(f"    {'name':<24}{'atk':<11}{'price':<11}\n")
    for name, atk, price in items:
        print(f"    {name:<24}{atk:<11}{price:<11}")
    line()


def invalid():
    from main import clear, pause

    clear()
    line()
    print("\n" + (12 * " ") + "<!> Invalid Input <!>" + "\n")
    line()
    pause()


def market():
    from main import clear, pause
    from lib import DB

    (db, c) = DB.connect()

    (mageid, gold) = c.execute("select ROWID, gold from mages").fetchone()

    showitems(c.execute("select * from market").fetchall())
    print("  g", gold)
    line()
    q = input(" >> ")
    item = c.execute(
        "select ROWID, * from market where name like ?",
        [f"%{q}%"],
    ).fetchone()

    if item == None:
        invalid()
        return
    (itemid, name, atk, price) = item

    clear()
    showitems([(name, atk, price)])
    print("  g", gold)
    line()
    q = input("    count >> ")
    try:
        count = int(q)
    except:
        invalid()
        return

    total = price * count
    if total > gold:
        line()
        print("\n" + (12 * " ") + "<!> Not enough gold <!>" + "\n")
        line()
        pause()
        return

    c.execute(
        "update mages set gold=(gold-?) where ROWID=?",
        [total, mageid],
    )

    res = c.execute(
        "update inventory set count=(count+?) where itemid=? and mageid=?",
        [count, itemid, mageid],
    )
    if res.rowcount == 0:
        c.execute(
            "insert into inventory values (?,?,?)",
            [mageid, itemid, count],
        )

    db.commit()
    db.close()

    clear()
    title()
    print("\n" + (14 * " ") + "Transaction Success" + "\n")
    line()
    pause()
