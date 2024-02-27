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
	fmt.Println("\n     1 - inventory")
	fmt.Println("\n     2 - market")
	fmt.Println("\n     3 - travel")
	fmt.Println("\n     4 - sleep")

	fmt.Print("\n>>>> ")
	var op string
	fmt.Scanln(&op)

	switch op {
	case "0":
		status()
	case "1":
		inventory()
	case "2":
		market()
	case "3":
		travel()
	case "4":
		sleep()
	default:
		goto gameloop
	}

	fmt.Print("\nreturn")
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

	fmt.Println("\n      - status -       ")
	fmt.Println("    lvl", lvl, "   xp", xp)
	fmt.Println("     hp", hp, "  atk", atk)
	fmt.Println("      g", g)
}

func inventory() {
	title()

	fmt.Println("\n     - inventory -     ")
}

func market() {
	title()

	fmt.Println("\n      - market -       ")
}

func travel() {
	title()

	fmt.Println("\n      - travel -       ")
}

func sleep() {
	title()

	fmt.Println("\n      - sleep -        ")
}
