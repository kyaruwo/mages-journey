import os
import sqlite3

try:
    os.chdir("Mage's Journey/dbuild")
except:
    pass

#database
db = sqlite3.connect("db.sqlite")
c = db.cursor()
c.executescript("""
    drop table if exists Mage;
    drop table if exists Stat;
    drop table if exists Bag;
    create table Mage(
        id integer primary key autoincrement not null unique,
        name text unique,
        role text,
        lvl integer);
    create table Stat(
        mage_id integer,
        gold integer,
        exp integer,
        hp integer,
        atk integer,
        def integer);
    create table Bag(
        mage_id integer,
        item_id integer unique,
        count integer);
""")
db.commit()
c.close()
#https://github.com/kyaruwo