import os
import sqlite3
import json

try:
    os.chdir("Mage's Journey/dbuild")
except:
    pass

#database
db = sqlite3.connect("db.sqlite")
c = db.cursor()
c.executescript("""
    drop table if exists Enemy;
    drop table if exists EStat;
    create table Enemy(
        id integer primary key autoincrement not null unique,
        role text unique);
    create table EStat(
        enemy_id integer,
        lvl integer,
        exp integer,
        gold integer,
        hp integer,
        atk integer,
        def integer);
""")
e_json = open("enemy.json").read()
enemies = json.loads(e_json)
for e in enemies:  #enemy; role lvl xp gold hp atk def
    c.execute("insert into Enemy (role) values (?)", (e["role"], ))
    c.execute("select id from Enemy where role = ?", (e["role"], ))
    enemy_id = c.fetchone()[0]
    c.execute(
        "insert into EStat (enemy_id,lvl,exp,gold,hp,atk,def) values (?,?,?,?,?,?,?)",
        (enemy_id, e["lvl"], e["exp"], e["gold"], e["hp"], e["atk"], e["def"]))
    db.commit()
c.close()
#https://github.com/kyaruwo