package game

import (
	"database/sql"
	"fmt"

	"github.com/kyaruwo/mages-journey/gamemod"
)

func Travel(db *sql.DB) {
	gamemod.Title()

	fmt.Println("\n     - travel -")
}
