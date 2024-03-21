package game

import (
	"database/sql"
	"fmt"
	"mages-journey/gamemod"
)

func Market(db *sql.DB) {
	gamemod.Title()

	fmt.Println("\n     - market -")
}
