package game

import (
	"database/sql"
	"fmt"
	"log"
	"mages-journey/gamemod"
)

func Status(db *sql.DB) {
	gamemod.Title()

	var id, lvl, xp, g int
	err := db.QueryRow(`
	select
		rowid, *
	from
		mages
	`).Scan(&id, &lvl, &xp, &g)
	if err != nil {
		log.Fatal(err)
	}

	var hp = 6 + lvl

	var atk = 3 + lvl
	var item_atk sql.NullInt64
	err = db.QueryRow(`
	select
		sum(atk * count)
	from
		inventory
		join market on item_id = market.ROWID
	where
		mage_id = ?
	`, id).Scan(&item_atk)
	if err != nil {
		log.Fatal(err)
	}
	if item_atk.Valid {
		atk = atk + int(item_atk.Int64)
	}

	fmt.Println("\n     - status -")
	fmt.Println("   lvl", lvl, "   xp", xp)
	fmt.Println("    hp", hp, "  atk", atk)
	fmt.Println("     g", g)
}
