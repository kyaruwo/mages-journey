package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
gameloop:
	title()

	fmt.Println("\n     0 - status")

	fmt.Print("\n>>>> ")
	var op string
	fmt.Scanln(&op)

	switch op {
	case "0":
		status()
	default:
		goto gameloop
	}

	fmt.Scanln()
	goto gameloop
}

func title() {
	var clear = exec.Command("cmd", "/c", "cls")
	clear.Stdout = os.Stdout
	clear.Run()
	fmt.Println("=o= mages journey =o=")
}

func status() {
	title()

	// todo; fetch from database
	var lvl, xp, g, hp, atk = 1, 0, 0, 8, 4

	fmt.Println("\n      - stats -        ")
	fmt.Println("    lvl", lvl, "   xp", xp)
	fmt.Println("     hp", hp, "  atk", atk)
	fmt.Println("      g", g)
}
