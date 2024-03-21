package gamemod

import (
	"database/sql"
	"errors"
	"fmt"
	"log"
	"os"
	"time"
)

func Initialize(DB_FILENAME string) {
	_, err := os.Stat(DB_FILENAME)
	if err == nil {
		return
	}
	if !errors.Is(err, os.ErrNotExist) {
		log.Fatal(err)
	}

	Clear()

	db, err := sql.Open("sqlite", DB_FILENAME)
	if err != nil {
		db.Close()
		os.Remove(DB_FILENAME)
		log.Fatal(err)
	}
	defer db.Close()
	fmt.Println("Created Database")

	InventoryInit(DB_FILENAME, db)
	MarketInit(DB_FILENAME, db)
	EnemiesInit(DB_FILENAME, db)
	MageInit(DB_FILENAME, db)

	time.Sleep(4269 * time.Millisecond)
}

func InventoryInit(DB_FILENAME string, db *sql.DB) {
	_, err := db.Exec(`
	create table inventory(mage_id int, item_id int, count int);
	`)
	if err != nil {
		db.Close()
		os.Remove(DB_FILENAME)
		log.Fatal(err)
	}
	fmt.Println("Created Inventory Table")
}

type Item struct {
	name  string
	atk   int
	price int
}

func MarketInit(DB_FILENAME string, db *sql.DB) {
	_, err := db.Exec(`
	create table market(
		"name" varchar(69) unique,
		atk int,
		price int
	);
	`)
	if err != nil {
		db.Close()
		os.Remove(DB_FILENAME)
		log.Fatal(err)
	}
	fmt.Println("Created Market Table")

	ITEMS := []Item{
		{"stick", 1, 10},
		{"branch", 12, 120},
		{"staff", 44, 440},
		{"staff of sloth", 100, 1000},
		{"staff of wrath", 200, 2000},
		{"staff of gluttony", 300, 3000},
		{"staff of envy", 400, 4000},
		{"staff of lust", 600, 6000},
		{"staff of pride", 800, 8000},
		{"staff of greed", 1000, 10000},
	}

	for _, item := range ITEMS {
		stmt, err := db.Prepare(`
		insert into
			market("name", atk, price)
		values
			(?, ?, ?);
		`)
		if err != nil {
			db.Close()
			os.Remove(DB_FILENAME)
			log.Fatal(err)
		}
		_, err = stmt.Exec(&item.name, &item.atk, &item.price)
		if err != nil {
			db.Close()
			os.Remove(DB_FILENAME)
			log.Fatal(err)
		}
		stmt.Close()

		fmt.Println("Created", item.name)
	}
}

type Enemy struct {
	name string
	xp   int
	gold int
	hp   int
	atk  int
}

func EnemiesInit(DB_FILENAME string, db *sql.DB) {
	_, err := db.Exec(`
	create table enemies(
		"name" varchar(69) unique,
		xp int,
		gold int,
		hp int,
		atk int
	);
	`)
	if err != nil {
		db.Close()
		os.Remove(DB_FILENAME)
		log.Fatal(err)
	}
	fmt.Println("Created Enemies Table")

	ENEMIES := []Enemy{
		{"slime", 2, 1, 10, 2},
		{"wolf", 6, 2, 26, 6},
		{"goblin", 4, 10, 40, 12},
		{"skeleton", 14, 12, 100, 24},
		{"ghost", 24, 6, 200, 40},
		{"demon knight", 36, 40, 480, 80},
		{"demon general", 160, 100, 1200, 260},
		{"demon lord", 400, 400, 6000, 600},
		{"demon king", 999, 999, 9999, 999},
		{"mage of sloth", 2000, 2000, 10000, 2000},
		{"mage of wrath", 3000, 3000, 15000, 3000},
		{"mage of gluttony", 4000, 6000, 30000, 3000},
		{"mage of envy", 8000, 8000, 60000, 6000},
		{"mage of lust", 10000, 12000, 100000, 12000},
		{"mage of pride", 60000, 40000, 600000, 100000},
		{"mage of greed", 999999, 999999, 9999999, 999999},
	}

	for _, enemy := range ENEMIES {
		stmt, err := db.Prepare(`
		insert into
			enemies("name", xp, gold, hp, atk)
		values
			(?, ?, ?, ?, ?);
		`)
		if err != nil {
			db.Close()
			os.Remove(DB_FILENAME)
			log.Fatal(err)
		}
		_, err = stmt.Exec(&enemy.name, &enemy.xp, &enemy.gold, &enemy.xp, &enemy.atk)
		if err != nil {
			db.Close()
			os.Remove(DB_FILENAME)
			log.Fatal(err)
		}
		stmt.Close()

		fmt.Println("Summoned", enemy.name)
	}
}

type Mage struct {
	lvl  int
	xp   int
	gold int
}

func MageInit(DB_FILENAME string, db *sql.DB) {
	_, err := db.Exec(`
	create table mages(lvl int, xp int, gold int);
	`)
	if err != nil {
		db.Close()
		os.Remove(DB_FILENAME)
		log.Fatal(err)
	}
	fmt.Println("Created Mages Table")

	stmt, err := db.Prepare(`
	insert into
		mages(lvl, xp, gold)
	values
		(?, ?, ?);
	`)
	if err != nil {
		db.Close()
		os.Remove(DB_FILENAME)
		log.Fatal(err)
	}
	MAGE := Mage{1, 0, 0}
	_, err = stmt.Exec(&MAGE.lvl, &MAGE.xp, &MAGE.gold)
	if err != nil {
		db.Close()
		os.Remove(DB_FILENAME)
		log.Fatal(err)
	}
	stmt.Close()

	fmt.Println("Summoned Mage")
}
