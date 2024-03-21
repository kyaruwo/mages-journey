package game

import (
	"database/sql"
	"fmt"
	"mages-journey/gamemod"
)

func Travel(db *sql.DB) {
	gamemod.Title()

	fmt.Println("\n     - travel -")
}
