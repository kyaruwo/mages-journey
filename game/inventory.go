package game

import (
	"database/sql"
	"fmt"
	"mages-journey/gamemod"
)

func Inventory(db *sql.DB) {
	gamemod.Title()

	fmt.Println("\n    - inventory -")
}
