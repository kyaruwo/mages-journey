package main

import (
	"database/sql"
	"fmt"
	"log"
	"mages-journey/game"
	"mages-journey/gamemod"

	_ "github.com/glebarez/go-sqlite"
)

func main() {

	const DB_FILENAME = "journey.sqlite"
	gamemod.Initialize(DB_FILENAME)
	db, err := sql.Open("sqlite", DB_FILENAME)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

gameloop:
	gamemod.Title()

	fmt.Print("\n     0 - status")
	fmt.Print("\n     1 - inventory")
	fmt.Print("\n     2 - market")
	fmt.Print("\n     3 - travel")
	fmt.Print("\n     4 - sleep")

	fmt.Print("\n\n>>>> ")
	var op string
	fmt.Scanln(&op)

	switch op {
	case "0", "s", "status":
		game.Status(db)
	case "1", "i", "inventory":
		game.Inventory(db)
	case "2", "m", "market":
		game.Market(db)
	case "3", "t", "travel":
		game.Travel(db)
	case "4", "q", "sleep":
		game.Sleep()
		return
	default:
		goto gameloop
	}

	fmt.Print("\nreturn")
	fmt.Scanln()
	goto gameloop
}
