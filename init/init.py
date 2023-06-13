def initialize():
    import os, json
    from lib import DB

    if os.path.exists(DB.gamedata):
        return

    (db, c) = DB.connect()

    # TABLES
    c.executescript(
        """
    create table mages(
        lvl int,
        xp int,
        gold int
    );
    create table enemies(
        `name` varchar(69) unique,
        xp int,
        gold int,
        hp int,
        atk int,
        def int
    );
    create table market(
        `name` varchar(69) unique,
        atk int,
        price int
    );
    create table inventory (
        mageid int,
        itemid int key,
        `count` int
    );
    create trigger itemzero
    after update on inventory
    begin
        delete from inventory where `count` = 0;
    end;
        """
    )

    # MAGE
    c.execute(
        """
    insert into mages
    values
    (1,0,0);
        """
    )

    # ENEMIES
    for e in json.loads(open("init/enemies.json").read()):
        c.execute(
            "insert into enemies values (?,?,?,?,?,?)",
            [e["name"], e["xp"], e["gold"], e["hp"], e["atk"], e["def"]],
        )

    # ITEMS
    for i in json.loads(open("init/items.json").read()):
        c.execute(
            "insert into market values (?,?,?)",
            [i["name"], i["atk"], i["price"]],
        )

    db.commit()
    db.close()
