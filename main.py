import os
import sqlite3


def clear(): return os.system("cls")


if not os.path.isfile("db.sqlite"):
    from reset import reset
    reset()

# database
db = sqlite3.connect("db.sqlite")
c = db.cursor()


# functions
class mage:

    def title():
        clear()
        print("=o= Mage's Journey =o=\n")

    def id(mage_name):
        c.execute("select id from Mage where name = ?", (mage_name, ))
        mage_id = c.fetchone()[0]
        return mage_id

    def stat(mage_id):
        # 0 name, 1 role, 2 lvl, 3 gold ,4 exp, 5 hp, 6 atk, 7 def, 8 lvup
        for i in c.execute(
            "select Mage.name, Mage.role, Mage.lvl, Stat.gold, Stat.exp, Stat.hp, Stat.atk, Stat.def from Mage join Stat on Mage.id = Stat.mage_id where mage_id = ?",
                (mage_id, )):
            return [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[2] * 12]

    def printstat():
        s = mage.stat(mage_id)
        # 0 name, 1 role, 2 lvl, 3 gold, 4 exp, 5 hp, 6 atk, 7 def, 8 lvup
        print(f"\nName: {s[0]}\nrole: {s[1]} {s[2]}")
        print(f"gold: {s[3]} exp: {s[4]}/{s[8]}")
        print(f"atk: {s[6]} hp: {s[5]} def: {s[7]}")

    def bag(mage_id):
        print("=o= Bag =o=")
        # 0 item, 1 count, 2 atk
        for i in c.execute(
            "select item, count, i_atk from Bag join Shop on Bag.item_id = Shop.id where mage_id = ?",
                (mage_id, )):
            print(
                f"item: {i[0]} atk: {i[2]} count: {i[1]} total atk: {i[2]*i[1]}"
            )

    def update(mage_id, gold, exp):
        # 0 name, 1 role, 2 lvl, 3 gold ,4 exp, 5 hp, 6 atk, 7 def, 8 lvup
        s = mage.stat(mage_id)
        s[3] += gold
        s[4] += exp
        c.execute("update Stat set gold = ? where mage_id = ?",
                  (s[3], mage_id))
        print(f"\n {gold} gold | Gold in Bag {s[3]}")
        print(f" {exp} exp | {s[4]}/{s[8]}")
        if s[4] < s[8]:
            c.execute("update Stat set exp = ? where mage_id = ?",
                      (s[4], mage_id))
            db.commit()
        if (s[4] >= s[8]):
            c.execute("update Mage set lvl = ? where id = ?",
                      (s[2] + 1, mage_id))
            c.execute("update Stat set exp = ? where mage_id = ?",
                      (s[4] - s[8], mage_id))
            c.execute("update Stat set hp = ? where mage_id = ?",
                      (s[5] + 2, mage_id))
            c.execute("update Stat set atk = ? where mage_id = ?",
                      (s[6] + 4, mage_id))
            c.execute("update Stat set def = ? where mage_id = ?",
                      (s[7] + 1, mage_id))
            db.commit()
            print("\nLevel up!", s[2] + 1)
            mage.printstat()

    def reset():
        db.close()
        from reset import resetgame
        resetgame()


class travel:

    def shop(mage_id):
        print("=o= Shop =o=")
        # 0 name, 1 role, 2 lvl, 3 gold ,4 exp, 5 hp, 6 atk, 7 def, 8 lvup
        s = mage.stat(mage_id)  # mage gold
        gold = s[3]
        atk = s[6]
        item = []
        ipa = []
        for i in c.execute(
                "select price, i_atk, item, id from Shop order by id asc"):
            print(f"\nprice: {i[0]} i_atk: {i[1]} item: {i[2]}")
            item.append(i[2])
            ipa.append(i)
        print(f"\ngold in bag {gold}")
        buy = input("\nhome | item: ")
        buy = buy.lower()
        if buy in ["home", "h"]:
            return mage.title(), mage.printstat()
        elif buy not in item:
            mage.title()
            return print("No such item exists!")
        for i in ipa:  # 0 price, 1 i_atk, 2 item, 3 id
            if i[2] == buy:
                mage.title()
                mage.bag(mage_id)
                print("\n=o= Shop =o=")
                print(f"price: {i[0]} i_atk: {i[1]} item: {i[2]}")
                print(f"\ngold in bag {gold}")
                buy_count = input("\nhome | - sell | buy: ")
                buy_count = buy_count.lower()
                if buy_count in ["home", "h"]:
                    return mage.title(), mage.printstat()
                # default buy_count
                try:
                    buy_count = int(buy_count)
                except:
                    buy_count = 1
                print(f"\nExchanging {buy_count} {buy}")
                # sell and gold check
                if buy_count < 1:
                    None
                elif gold < (i[0] * buy_count):
                    return print("Not enough gold!")
                try:  # Bag item count
                    c.execute(
                        "select count from Bag where mage_id = ? and item_id = ?",
                        (mage_id, i[3]))
                    count = c.fetchone()[0]
                except:
                    count = 0
                print(f"worth {i[0] * buy_count} gold")
                # deduct gold from Stat
                c.execute("update Stat set gold = ? where mage_id = ?",
                          (gold - (i[0] * buy_count), mage_id))
                # add or update the Bag item
                c.execute(
                    "insert or replace into Bag (mage_id, count, item_id) values (?, ?, ?)",
                    (mage_id, count + (1 * buy_count), i[3]))
                # add atk
                c.execute("update Stat set atk = ? where mage_id = ?",
                          (atk + (i[1] * buy_count), mage_id))
                db.commit()
                print(f"\nBought {buy_count} of {buy}")
                print(f"\ngold in bag: {gold - (i[0] * buy_count)}")

    def battle(mage_id):
        print("=o=            In a Journey            =o=\n")
        # difficulty dictionary
        diff = {
            "E": 1,
            "D": 2,
            "C": 4,
            "B": 6,
            "A": 8,
            "S": 10,
            "SS": 12,
            "SSS": 14
        }
        # difficulty input
        print("        =o= default difficulty is E =o=")
        tier = input("home | E to A, S to SSS enemy difficulty: ")
        tier = tier.upper()
        if tier in ["HOME", "H"]:
            return mage.title(), mage.printstat()
        # default difficulty
        if tier not in diff:
            m = diff["E"]
            print("\nDifficulty set to E")
        else:
            m = diff[tier]
            print("\nDifficulty set to", tier)
        ent = ["normal", "n", "demon", "d", "mage", "m"]
        etype = input("\n=o= home | normal | demon | mage =(?)= ")
        etype = etype.lower()
        if etype in ["home", "h"]:
            return mage.title(), mage.printstat()
        # default enemies
        if etype not in ent:
            etype = "normal"
        enemy = []
        elist = []
        # 0 role, 1 lvl, 2 exp, 3 gold, 4 hp, 5 atk, 6 def
        for i in c.execute(
                "select Enemy.role, EStat.lvl, EStat.exp, EStat.gold, EStat.hp, EStat.atk, EStat.def from Enemy join EStat where Enemy.id = EStat.enemy_id"
        ):
            j = i[0].split()
            if etype == "normal" and j[0] != "demon" and j[0] != "mage":
                print(
                    f"\nrole: {i[0]} lvl: {i[1]*m} exp: {i[2]*m} gold: {i[3]*m} hp: {i[4]*m} atk: {i[5]*m} def: {i[6]*m}"
                )
            elif i[0].startswith(etype):
                print(
                    f"\nrole: {i[0]} lvl: {i[1]*m} exp: {i[2]*m} gold: {i[3]*m} hp: {i[4]*m} atk: {i[5]*m} def: {i[6]*m}"
                )
            enemy.append(i[0])
            elist.append(i)
        role = input("\nhome | choose enemy to attack: ")
        if role in ["home", "h"]:
            return mage.title(), mage.printstat()
        if role not in enemy:  # default to slime
            role = "slime"
        print("\n=o= Chosen foe is a", role, "=o=")
        start = input("\npress Enter to battle: ")
        for i in elist:
            # instance battle
            if i[0] == role:
                # 0 role, 1 lvl, 2 exp, 3 gold, 4 hp, 5 atk, 6 def
                elvl = i[1] * m
                eexp = i[2] * m
                egold = i[3] * m
                ehp = i[4] * m
                eatk = i[5] * m
                edef = i[6] * m
                # 0 name,1 role,2 lvl,3 gold,4 exp,5 hp,6 atk,7 def,8 lvup
                s = mage.stat(mage_id)
                hp = s[5]
                mage.title()
                print("Battle Begins!")
                while True:
                    # mage status
                    print(f"\nName: {s[0]}\nrole: {s[1]} {s[2]}")
                    print(f"gold: {s[3]} exp: {s[4]}/{s[8]}")
                    print(f"atk: {s[6]} hp: {hp} def: {s[7]}")

                    # attack result
                    if hp != s[5]:
                        print("\n=o=        o        =o=")
                        print(f"You took {s[5]-hp} damage")
                        print(f"Enemy took {(i[4] * m)-ehp} damage")
                        print("=o=        o        =o=")

                    # enemy status
                    print(f"\nrole: {i[0]} {elvl}")
                    print(f"gold: {egold} exp: {eexp}")
                    print(f"atk: {eatk} hp: {ehp} def: {edef}")

                    act = input("\nhome | attack(Enter): ")
                    if act in ["home", "h"]:
                        mage.title()
                        print("A wise choice indeed!")
                        return mage.printstat()
                    hp -= (eatk - s[7])
                    ehp -= (s[6] - edef)
                    mage.title()
                    # hp check, egold, eexp
                    if hp < 1:
                        print("You Died")
                        mage.update(mage_id, -egold, 0)
                        return
                    if ehp < 1:
                        print("Enemy Felled")
                        mage.update(mage_id, egold, eexp)
                        return


# Start Menu
while True:
    mage.title()
    mage_name = input("Name: ")
    try:  # Old Mage
        mage_id = mage.id(mage_name)
        mage.title()
        print("Welcome!", mage_name)
        mage.printstat()
        break
    except:  # New Mage
        new_journey = input("A new Mage has come, Begin Journey y|n? ")
        if new_journey != "y":
            continue
        c.execute("insert into Mage (name,role,lvl) values (?,?,?)",
                  (mage_name, "mage", 1))
        mage_id = mage.id(mage_name)
        c.execute(
            "insert into Stat (mage_id,gold,exp,hp,atk,def) values (?,0,0,4,8,1)",
            (mage_id, ))
        db.commit()
        mage.title()
        print("Welcome!", mage_name)
        mage.printstat()
        break

# Main Menu
while True:
    mage_id = mage_id
    act = input("\n=o= home | bag | travel | shop =(?)= ")
    act = act.upper()
    if act == "RESETGAME":
        mage.reset()
        break
    elif act in ["BAG", "B"]:
        mage.title()
        mage.bag(mage_id)
    elif act in ["TRAVEL", "T"]:
        mage.title()
        travel.battle(mage_id)
    elif act in ["SHOP", "S"]:
        mage.title()
        travel.shop(mage_id)
    else:  # home
        mage.title()
        mage.printstat()

# https://github.com/kyaruwo
