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
    drop table if exists Shop;
    create table Shop(
        id integer primary key autoincrement not null unique,
        price integer,
        i_atk integer,
        item text unique);
""")

i_json = open("item.json").read()
item = json.loads(i_json)
for i in item:  #enemy; item i_atk price
    c.execute("insert into Shop (item,i_atk,price) values (?,?,?)",
              (i["item"], i["i_atk"], i["price"]))
    db.commit()
c.close()
#https://github.com/kyaruwo