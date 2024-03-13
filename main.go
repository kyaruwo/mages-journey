package main

import (
	"fmt"
	"mages-journey/game"
	"mages-journey/gamemod"
)

func main() {
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
		game.Status()
	case "1", "i", "inventory":
		game.Inventory()
	case "2", "m", "market":
		game.Market()
	case "3", "t", "travel":
		game.Travel()
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
