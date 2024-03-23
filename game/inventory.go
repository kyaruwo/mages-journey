package game

import (
	"database/sql"
	"fmt"

	"github.com/kyaruwo/mages-journey/gamemod"
)

func Inventory(db *sql.DB) {
	gamemod.Title()

	fmt.Println("\n    - inventory -")
}
