package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
gameloop:
	title()

	fmt.Print("\n     0 - status")
	fmt.Print("\n     1 - inventory")
	fmt.Print("\n     2 - market")
	fmt.Print("\n     3 - travel")
	fmt.Print("\n     4 - sleep")

	fmt.Print("\n\n>>>> ")
	var op string
	fmt.Scanln(&op)

	switch op {
	case "0", "s":
		status()
	case "1", "i":
		inventory()
	case "2", "m":
		market()
	case "3", "t":
		travel()
	case "4", "q":
		sleep()
		return
	default:
		goto gameloop
	}

	fmt.Print("\nreturn")
	fmt.Scanln()
	goto gameloop
}

func clear() {
	var clear = exec.Command("cmd", "/c", "cls")
	clear.Stdout = os.Stdout
	clear.Run()
}

func title() {
	clear()
	fmt.Println("=o= mages journey =o=")
}

func status() {
	title()

	// todo; fetch from database
	var lvl, xp, g, hp, atk = 1, 0, 0, 8, 4

	fmt.Println("\n      - status -       ")
	fmt.Println("    lvl", lvl, "   xp", xp)
	fmt.Println("     hp", hp, "  atk", atk)
	fmt.Println("      g", g)
}

func inventory() {
	title()

	fmt.Println("\n    - inventory -     ")
}

func market() {
	title()

	fmt.Println("\n     - market -       ")
}

func travel() {
	title()

	fmt.Println("\n     - travel -       ")
}

func sleep() {
	clear()

	fmt.Print("\n\tJourney's End\n")
}
