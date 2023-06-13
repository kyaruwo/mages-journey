def line():
    from main import line

    line(48)


def title():
    line()
    print((19 * " ") + "INVENTORY")
    line()


def showitems(items):
    if len(items) == 0:
        print("\n" + (21 * " ") + "Empty" + "\n")
        return
    print(f"    {'name':<24}{'atk':<11}{'count':<11}\n")
    for name, atk, count in items:
        print(f"    {name:<24}{atk:<11}{count:<11}")


def inventory():
    from main import pause
    from lib import DB

    title()

    (db, c) = DB.connect()
    showitems(
        c.execute(
            """
        select name, atk, count
        from inventory join market
        on itemid = market.ROWID
            """
        ).fetchall()
    )

    line()
    pause()
