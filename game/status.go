package game

import (
	"database/sql"
	"fmt"
	"mages-journey/gamemod"
)

func Status(db *sql.DB) {
	gamemod.Title()

	// todo; fetch from database
	var lvl, xp, g, hp, atk = 1, 0, 0, 8, 4

	fmt.Println("\n     - status -")
	fmt.Println("   lvl", lvl, "   xp", xp)
	fmt.Println("    hp", hp, "  atk", atk)
	fmt.Println("     g", g)
}
